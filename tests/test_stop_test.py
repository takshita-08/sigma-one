from playwright.sync_api import expect
import logging

from pages.stop_test import StopTest


def test_stop_only(select_device):
    stop_test = StopTest(select_device.page)
    stop_test.stop_test_from_centra()
    print("🔹 test_stop_test: Stop test command executed."  )
    try:
        expect(stop_test.success_toast_message).to_be_visible(timeout=5000)
    except:
        expect(stop_test.toast_message).to_be_visible(timeout=5000)
        logging.info("Test already stopped")        
    expect(stop_test.stop_test_item).not_to_be_visible()


def test_stop_test(stop_test):
    print("🔹 test_stop_test: Stop test command executed."  )
    try:
        stoptest, _ = stop_test
        expect(stoptest.success_toast_message).to_be_visible(timeout=5000)
        logging.info("Test stopped successfully")
    except:
        expect(stoptest.toast_message).to_be_visible(timeout=5000)
        logging.info("Test already stopped")
    expect(stoptest.stop_test_item).not_to_be_visible()