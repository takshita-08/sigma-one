import base64
from datetime import datetime
import logging

import pytest
from playwright.sync_api import sync_playwright
from pages.start_test import StartTest
from utils import config
from utils.config import CENTRA_USERNAME, CENTRA_PASSWORD, DEVICE_ID, DEVICE_SERIAL, TEMPLATE_NAME, SAME_AS_TEST_NAME, DETACH_ATTACH, IS_SCENARIO, CREATE_TEMPLATE, EDIT_TEMPLATE,FILE_PREFIX, UPDATE_URL
from pages.login import Login
from pages.selectDevice import SelectDevice
from pages.stop_test import StopTest
from pages.uploaded_files import UploadedFiles
from pages.context_menu import ContextMenu
import pytest_html


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page") or item.funcargs.get("logged_in_page")

        if page:
            screenshot_bytes = page.screenshot()

            screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.png(screenshot_base64, name="Failure Screenshot"))
            report.extra = extra

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
        ignore_https_errors=True)
        page = context.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def login(page):
    centra = Login(page)
    centra.load_page()
    return centra

@pytest.fixture(scope="function")
def logged_in_user(login):
    login.login_fnc(CENTRA_USERNAME, CENTRA_PASSWORD)
    return login

@pytest.fixture(scope="function")
def select_device(logged_in_user):
    device= SelectDevice(logged_in_user.page)
    device.select_device(DEVICE_ID,DEVICE_SERIAL)
    return device

@pytest.fixture(scope="function")
def file_name():
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_name = f"{FILE_PREFIX}-{timestamp}"
    
    # file_name_obj = StartTest()       
    return file_name

@pytest.fixture(scope="function")
def start_test(select_device,file_name):
    starttest = StartTest(select_device.page)
    is_already_started = starttest.start_test_from_centra(TEMPLATE_NAME, file_name, DETACH_ATTACH, SAME_AS_TEST_NAME)
    return starttest, is_already_started

@pytest.fixture(scope="function")
def stop_test(start_test):
    starttest, is_already_started = start_test
    stoptest = StopTest(starttest.page)
    starttest.page.wait_for_timeout(50000)
    stoptest.stop_test_from_centra()
    return stoptest , is_already_started

@pytest.fixture(scope="function")
def check_uploaded_files(stop_test,file_name):
    stoptest, is_already_started = stop_test
    upload = UploadedFiles(stoptest.page)
    if is_already_started:
        logging.info("🔹 Skipping file search as the test was already started.")
        return upload, None
    upload.page.wait_for_timeout(30000)
    upload.navigate_to_uploaded_files()
    logging.info(f"🔹 Searching for '{file_name}'")
    files = upload.search_files(file_name)
    return upload, files

@pytest.fixture(scope="function")
def context_menu(select_device):
    context_menu = ContextMenu(select_device.page)
    return context_menu

@pytest.fixture(scope="function")
def override_config_for_update_url(monkeypatch):
    print("🔹 override_config_for_update_url: Overriding BASE_URL for update URL test.")
    monkeypatch.setattr(config, "BASE_URL", UPDATE_URL)