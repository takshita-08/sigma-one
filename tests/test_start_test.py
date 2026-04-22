from playwright.sync_api import expect


def test_start_test(start_test):
    print("🔹 test_start_test: Test started and test details page loaded.")
    # Assert that the OK button is no longer visible, indicating the dialog has closed
    expect(start_test.ok_button).not_to_be_visible(timeout=5000)
    # Assert that the template dropdown is not visible
    expect(start_test.template_dropdown).not_to_be_visible(timeout=5000)
    # Assert that the page URL indicates navigation to test details
    assert "testdetails" in start_test.page.url.lower(), "Page should navigate to test details after starting a test"