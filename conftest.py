import pytest
from playwright.sync_api import sync_playwright
from pages.start_test import StartTest
from utils.config import CENTRA_USERNAME, CENTRA_PASSWORD, DEVICE_ID, DEVICE_SERIAL, TEMPLATE_NAME, SAME_AS_TEST_NAME, DETACH_ATTACH, IS_SCENARIO, CREATE_TEMPLATE, EDIT_TEMPLATE,FILE_PREFIX
from pages.login import Login
from pages.selectDevice import SelectDevice

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
    device.select_device(DEVICE_ID, DEVICE_SERIAL)
    return device

@pytest.fixture(scope="function")
def start_test(select_device):
    starttest = StartTest(select_device.page)
    starttest.start_test(TEMPLATE_NAME, FILE_PREFIX, DETACH_ATTACH, SAME_AS_TEST_NAME)
    return starttest