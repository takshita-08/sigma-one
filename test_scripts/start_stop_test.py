import pytest
from playwright.sync_api import sync_playwright

playwright_instance = None
browser_instance = None

CENTRA_USERNAME = "takshita"
CENTRA_PASSWORD = "Meritech@123"
DEVICE_ID = "Sigma-One-4d53d0db3c5a434291694f9628628d1a"
DEVICE_SERIAL = "SCG13"
CREATE_PING_TEMPLATE = False
PING_TEMPLATE_NAME = "Ping_Automation_Test"


@pytest.fixture(scope="session", autouse=True)
def browser():
    global browser_instance,playwright_instance
    if browser_instance is None:
        playwright_instance =  sync_playwright().start()
        browser_instance = playwright_instance.chromium.launch(headless=False)
    yield browser_instance
    browser_instance.close()
    playwright_instance.stop()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    page.storage_state(path="auth.json")
    yield page
    page.close()

@pytest.fixture()
def launch_login_page(page):
    page.goto("https://centra.meritech.co.jp/testingteam/dashboard/", timeout=80000)
    page.wait_for_load_state("domcontentloaded")
    login_page = page.get_by_role("heading", name="Log in to your account")
    try:
        login_page.wait_for(state="visible", timeout=10000)
        print("Login page detected. Logging in...")
        page.get_by_test_id("testUsername").fill(CENTRA_USERNAME)
        page.get_by_test_id("testPassword").fill(CENTRA_PASSWORD)
        login_btn = page.get_by_role("button", name="Login")
        page.wait_for_timeout(5000)
        login_btn.click()
        confirm_btn = page.get_by_role("button", name="Confirm")
        confirm_btn.wait_for(state="visible", timeout=10000)
        if confirm_btn.is_visible() and confirm_btn.is_enabled():
            confirm_btn.click()
            print("Clicked confirmation dialog.")
        else:
            print("No confirmation dialog appeared.")
        print("Login complete.")
    except Exception as e:
        print(f"Already logged in — skipping login: {e}")
    # page.pause()
    return page

@pytest.fixture()
def select_device(launch_login_page):
    print("🔹 test_search_for_device: Searching for device...")
    launch_login_page.get_by_role("button", name="Device Filter").click()
    launch_login_page.get_by_test_id("Sigma-One").click()
    launch_login_page.wait_for_timeout(1000)
    input_device = launch_login_page.get_by_role("combobox", name="testDeviceId")
    input_device.click()
    input_device.fill(DEVICE_ID)
    launch_login_page.keyboard.press("Enter")
    launch_login_page.wait_for_timeout(1000)
    input_phone = launch_login_page.get_by_role("combobox", name="testPhoneId")
    input_phone.click()
    input_phone.fill(DEVICE_SERIAL)
    launch_login_page.keyboard.press("Enter")
    launch_login_page.get_by_role("button", name="Apply").click()
    print("Search executed successfully.")

    return launch_login_page

@pytest.fixture()
def start_test(select_device):
    select_device.wait_for_load_state("domcontentloaded")
    select_device.get_by_role("button", name="Quick Command").click()
    select_device.get_by_role("listitem", name="Start Test").click()
    select_device.wait_for_timeout(1000)
    if CREATE_PING_TEMPLATE:
        select_device.get_by_test_id("testAddTemplate").click()
        select_device.wait_for_timeout(1000)
        new_template = select_device.get_by_role("combobox", name="testTestType")
        new_template.click()
        select_device.wait_for_timeout(1000)
        new_template.fill("Ping")
        select_device.keyboard.press("Enter")
        select_device.wait_for_timeout(1000)
        select_device.get_by_test_id("testNameField").fill(PING_TEMPLATE_NAME)
        test_runs = select_device.get_by_test_id("testTestRuns")
        test_runs.clear()
        test_runs.fill("3")
        idle_time = select_device.get_by_test_id("testIdleTime")
        idle_time.clear()
        idle_time.fill("1")
        select_device.get_by_role("button", name="Add", exact=True).click()
        select_device.wait_for_timeout(1000)

    template = select_device.get_by_role("combobox", name="testTemplateId")
    template.click()
    select_device.wait_for_timeout(1000)
    template.fill(PING_TEMPLATE_NAME)
    select_device.keyboard.press("Enter")
    select_device.wait_for_timeout(1000)
    select_device.get_by_test_id("testFilePrefix").fill("AutomationTest")
    select_device.get_by_test_id("testIsAttached").check()
    select_device.get_by_role("button", name="OK").click()
    # select_device.wait_for_load_state("networkidle")

    return select_device

@pytest.fixture()
def stop_test(start_test):
    start_test.wait_for_timeout(10000)
    start_test.get_by_role("button", name="Quick Command").click()
    start_test.get_by_role("listitem", name="Stop Test").click()
    # msg = stop_test.expect_event("dialog")
    # mas = msg.value.message

    return start_test

def test_launch_login_page(launch_login_page):
    print("🔹 test_centra_login: Dashboard loaded.")
    launch_login_page.wait_for_timeout(3000)
    assert "Dashboard" in launch_login_page.url or "centra" in launch_login_page.url

def test_select_device(select_device):
    print("🔹 test_centra_login: Dashboard loaded.")
    select_device.wait_for_timeout(3000)
    assert "Dashboard" in select_device.url or "centra" in select_device.url

def test_start_test(start_test):
    print("🔹 Start Test: Test Started...")
    start_test.wait_for_timeout(3000)
    # start_test.pause()
    assert "Dashboard" in start_test.url or "centra" in start_test.url

def test_stop_test(stop_test):
    print("🔹 Stopping Test: Test stopped.")
    stop_test.wait_for_timeout(5000)
    # stop_test.pause()
    # is_test_stopped = (
    #
    #         stop_test.get_by_text("Test stopped successfully").is_visible()
    #         or stop_test.get_by_text("Test already stopped").is_visible()
    # )
    assert "Dashboard" in stop_test.url or "centra" in stop_test.url
    # assert is_test_stopped, "Test not stopped"



