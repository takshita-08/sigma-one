import re

import paramiko
import pytest
import time

REMOTE_DEB_NAME = "sigmaone_alpha37.deb"
DEB_LOCAL_PATH = "/home/meritech/Downloads/Sigma-One_25.0.alpha-37_aarch64.deb"
DEB_REMOTE_PATH = f"/userdata/deb/{REMOTE_DEB_NAME}"

PURGE_AND_CLEAN = False
CONFIGURE_LICENSE_AND_REMOTE_URL= False
LICENSE = "somi-oxfd-xau5-akdb"
REMOTE_URL = "https://centra.meritech.co.jp/testingteam/centra.sd/api/"

class SSHDevice:
    def __init__(self, ip: str, username: str, password: str):
        self.ip = ip
        self.username = username
        self.password = password
        self.client = None

    def strip_ansi(self,text):
        ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
        return ansi_escape.sub('', text)

    def connect(self):
        """Open SSH connection with auto-fingerprint acceptance."""
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self.client.connect(
            hostname=self.ip,
            username=self.username,
            password=self.password,
            timeout=10,
            allow_agent=False,
            look_for_keys=False,
        )
        return self

    def exec(self, command: str) -> str:
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode().strip()

    def close(self):
        if self.client:
            self.client.close()


@pytest.fixture(scope="session")
def connect_via_ssh():
    """
    Create an SSH connection once per test session.
    Modify IP, user, password as needed per device.
    """
    IP = "192.168.1.24"        # <--- Change every time if needed
    USER = "meritech"
    PASS = "meritech"

    dev = SSHDevice(IP, USER, PASS).connect()
    yield dev
    dev.close()

@pytest.fixture()
def sigmaone(connect_via_ssh):
    class SigmaManager:
        def __init__(self,device):
            self.device = device

        def upload_deb(self, local_path, remote_path):
            is_file_exist = connect_via_ssh.exec(f"if [ -f {remote_path} ]; then echo Already Exist; else echo Missing; fi")
            if "Already Exist" in is_file_exist:
                print("Deb already exist...")
                return False , is_file_exist
            sftp = connect_via_ssh.client.open_sftp()
            sftp.put(local_path, remote_path)
            sftp.close()

            return True , is_file_exist

        def nuke_sigmaone(self):
            is_sigmaone_exist = connect_via_ssh.exec("dpkg-query -W -f='${Status}' sigma-one  2>/dev/null")
            if "install ok installed" not in is_sigmaone_exist:
                print("Sigma-One not installed, so can't be nuked...")
                return None
            nuke_output = connect_via_ssh.exec(f"echo 'meritech' | sudo -S sigma-one --nuke ; echo $?")
            exit_code = int(connect_via_ssh.strip_ansi(nuke_output).strip().split("\n")[-1])
            if PURGE_AND_CLEAN:
                print("Cleaning sigma-one-out folder...")
                connect_via_ssh.exec(f"echo 'meritech' | sudo -S rm -rf /userdata/sigma-one-out/")

            return exit_code

        def install_sigmaone(self):
            is_deb_exist = connect_via_ssh.exec(f"ls -lh {DEB_REMOTE_PATH}")
            if not is_deb_exist:
                return "Deb does not exist!"

            output = connect_via_ssh.exec(f"echo 'meritech' | sudo -S apt install {DEB_REMOTE_PATH} ; echo $?")
            exit_code = int(connect_via_ssh.strip_ansi(output).strip().split("\n")[-1])
            if CONFIGURE_LICENSE_AND_REMOTE_URL:
                print("Configuring License and URL ...")
                connect_via_ssh.exec(f"echo 'meritech' | sudo -S sigma-one --activate-license {LICENSE}")
                connect_via_ssh.exec(f"echo 'meritech' | sudo -S sigma-one --remote-url {REMOTE_URL}")

            return exit_code

    return SigmaManager(connect_via_ssh)

#--------------------------------Tests------------------------------------------#

def test_uname(sigmaone):
    """Verify Linux kernel access."""
    output = sigmaone.device.exec("uname -a")
    print("\n[uname output] =>", output)
    assert "Linux rk3588-meritech" in output
    assert "aarch64" in output

def test_uptime(sigmaone):
    """Check uptime is returning output."""
    output = sigmaone.device.exec("uptime")
    print("\n[uptime] =>", output)
    assert len(output) > 0

def test_reboot_sequence(sigmaone):
    print("\nTriggering reboot...")
    sigmaone.device.exec("sudo reboot")

    time.sleep(5)  # wait for disconnect

    # Attempt reconnect
    for i in range(10):
        try:
            test_dev = SSHDevice(sigmaone.device.ip, sigmaone.device.username, sigmaone.device.password).connect()
            print("Reconnected successfully.")
            test_dev.close()
            break
        except:
            print("Waiting for device to boot...")
            time.sleep(3)
    else:
        pytest.fail("Device did not come back after reboot")

def test_deb_exists(sigmaone):
    """Check a file or directory exists on the hardware."""
    output = sigmaone.device.exec(f"if [ -f {DEB_REMOTE_PATH} ]; then echo OK; fi")
    print("\n[file exists] =>", output)
    assert output == "OK"

def test_is_sigmaone_installed(sigmaone):
    is_exist = sigmaone.device.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" in is_exist

def test_configure_license_and_remote_url(sigmaone):
    sigmaone.device.exec(f"echo 'meritech' | sudo -S sigma-one --activate-license {LICENSE}")
    sigmaone.device.exec(f"echo 'meritech' | sudo -S sigma-one --remote-url {REMOTE_URL}")

def test_clean_all(sigmaone):
    sigmaone.device.exec(f"echo 'meritech' | sudo -S rm -rf /userdata/sigma-one-out/")


def test_install_sigmaone(sigmaone):
    assert sigmaone.install_sigmaone() == 0, f"Failed to install sigma-one! {sigmaone.install_sigmaone()}"
    after_install = sigmaone.device.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" in after_install

def test_upload_deb(sigmaone):
    is_uploaded = sigmaone.upload_deb(DEB_LOCAL_PATH, DEB_REMOTE_PATH)
    print("Uploaded::", is_uploaded)
    output = sigmaone.device.exec(f"ls -lh {DEB_REMOTE_PATH}")
    assert REMOTE_DEB_NAME in output

def test_nuke_sigmaone(sigmaone):
    assert sigmaone.nuke_sigmaone() == 0 , f"Nuke failed! {sigmaone.nuke_sigmaone}"
    after_nuke = sigmaone.device.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" not in after_nuke

def test_upload_deb_nuke_install_sigmaone(sigmaone):
    # Validate Upload
    assert sigmaone.upload_deb(DEB_LOCAL_PATH, DEB_REMOTE_PATH)
    output = sigmaone.device.exec(f"ls -lh {DEB_REMOTE_PATH}")
    assert REMOTE_DEB_NAME in output

    result = sigmaone.nuke_sigmaone()
    assert result == 0 or result is None

    after_nuke = sigmaone.device.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" not in after_nuke

    assert sigmaone.install_sigmaone() == 0
    is_exist = sigmaone.device.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" in is_exist






