import logging

from playwright.sync_api import expect


def test_start_test(start_test):
    print("🔹 test_start_test: Test started and test details page loaded.")
    starttest, _ = start_test
    expect(starttest.ok_button).not_to_be_visible(timeout=5000)
    try:
        expect(starttest.success_message).to_be_visible(timeout=5000)
        logging.info("Test started successfully")

    except:
        expect(starttest.toast_message).to_be_visible(timeout=5000)
        logging.info("Test already started")

    expect(starttest.template_dropdown).not_to_be_visible(timeout=5000)