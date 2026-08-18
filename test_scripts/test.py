import re

import paramiko
import pytest
import time

REMOTE_DEB_NAME = "sigmaone_beta27.deb"
DEB_LOCAL_PATH = "/home/meritech/Downloads/Sigma-One_25.0.beta-27_aarch64.deb"
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
    IP = "10.97.238.218"        # <--- Change every time if needed
    USER = "meritech"
    PASS = "meritech"

    dev = SSHDevice(IP, USER, PASS).connect()
    yield dev
    dev.close()

@pytest.fixture()
def upload_deb(connect_via_ssh):
    def _uploader(local_path, remote_path):
        is_file_exist = connect_via_ssh.exec(f"if [ -f {remote_path} ]; then echo Already Exist; else echo Missing; fi")
        if "Already Exist" in is_file_exist:
            print("Deb already exist...")
            return False , is_file_exist
        sftp = connect_via_ssh.client.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()
        return True , is_file_exist

    return _uploader

@pytest.fixture()
def nuke_sigmaone(connect_via_ssh):
    is_sigmaone_exist = connect_via_ssh.exec("dpkg-query -W -f='${Status}' sigma-one  2>/dev/null")
    if "install ok installed" not in is_sigmaone_exist:
        return "Sigma-One not installed, so can't be nuked..."
    nuke_output = connect_via_ssh.exec(f"echo 'meritech' | sudo -S sigma-one --nuke ; echo $?")
    exit_code = int(connect_via_ssh.strip_ansi(nuke_output).strip().split("\n")[-1])
    if PURGE_AND_CLEAN:
        print("Cleaning sigma-one-out folder...")
        try:
            connect_via_ssh.exec(f"echo 'meritech' | sudo rm -rf /userdata/sigma-one-out/")
        except Exception as e:
            print(f"Failed to clean! Reason: {e}")

    return exit_code

@pytest.fixture()
def install_sigmaone(connect_via_ssh):
    is_deb_exist = connect_via_ssh.exec(f"ls -lh {DEB_REMOTE_PATH}")
    print("out>>",is_deb_exist)
    if not is_deb_exist:
        return "Deb does not exist!"

    output = connect_via_ssh.exec(f"echo 'meritech' | sudo -S apt install {DEB_REMOTE_PATH} ; echo $?")
    exit_code = int(connect_via_ssh.strip_ansi(output).strip().split("\n")[-1])
    if CONFIGURE_LICENSE_AND_REMOTE_URL:
        print("Configuring License and URL ...")
        try:
            connect_via_ssh.exec(f"echo 'meritech' | sigma-one --activate-license {LICENSE}")
            connect_via_ssh.exec(f"echo 'meritech' | sigma-one --remote-url {REMOTE_URL}")
        except Exception as e:
            print(f"Failed to configure license and remote url {e}")

    return exit_code

#--------------------------------Tests------------------------------------------#

def test_uname(connect_via_ssh):
    """Verify Linux kernel access."""
    output = connect_via_ssh.exec("uname -a")
    print("\n[uname output] =>", output)
    assert "Linux rk3588-meritech" in output
    assert "aarch64" in output

def test_uptime(connect_via_ssh):
    """Check uptime is returning output."""
    output = connect_via_ssh.exec("uptime")
    print("\n[uptime] =>", output)
    assert len(output) > 0

def test_reboot_sequence(connect_via_ssh):
    print("\nTriggering reboot...")
    connect_via_ssh.exec("sudo reboot")

    time.sleep(5)  # wait for disconnect

    # Attempt reconnect
    for i in range(10):
        try:
            test_dev = SSHDevice(connect_via_ssh.ip, connect_via_ssh.username, connect_via_ssh.password).connect()
            print("Reconnected successfully.")
            test_dev.close()
            break
        except:
            print("Waiting for device to boot...")
            time.sleep(3)
    else:
        pytest.fail("Device did not come back after reboot")


def test_install_sigmaone(connect_via_ssh,install_sigmaone):
    assert install_sigmaone == 0, f"Failed to install sigma-one! {install_sigmaone}"
    after_install = connect_via_ssh.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" in after_install

def test_upload_deb(connect_via_ssh, upload_deb):
    is_uploaded = upload_deb(DEB_LOCAL_PATH, DEB_REMOTE_PATH)
    print("Uploaded::", is_uploaded)
    output = connect_via_ssh.exec(f"ls -lh {DEB_REMOTE_PATH}")
    assert REMOTE_DEB_NAME in output

def test_nuke_sigmaone(connect_via_ssh,nuke_sigmaone):
    assert nuke_sigmaone == 0 , f"Nuke failed! {nuke_sigmaone}"
    after_nuke = connect_via_ssh.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" not in after_nuke

def test_deb_exists(connect_via_ssh):
    """Check a file or directory exists on the hardware."""
    output = connect_via_ssh.exec(f"if [ -f {DEB_REMOTE_PATH} ]; then echo OK; fi")
    print("\n[file exists] =>", output)
    assert output == "OK"

def test_sigmaone_installed(connect_via_ssh):
    is_exist = connect_via_ssh.exec(
        "dpkg-query -W -f='${Status}' sigma-one 2>/dev/null"
    )
    assert "install ok installed" in is_exist

def test_configure_license_and_remote_url(connect_via_ssh):
    connect_via_ssh.exec(f"echo 'meritech' | sigma-one --activate-license {LICENSE}")
    connect_via_ssh.exec(f"echo 'meritech' | sigma-one --remote-url {REMOTE_URL}")

def test_upload_deb_nuke_install_sigmaone(connect_via_ssh,upload_deb, nuke_sigmaone, install_sigmaone):
    # Validate Upload
    upload_deb(DEB_LOCAL_PATH, DEB_REMOTE_PATH)
    output = connect_via_ssh.exec(f"ls -lh {DEB_REMOTE_PATH}")
    assert REMOTE_DEB_NAME in output

    # Validate Install







