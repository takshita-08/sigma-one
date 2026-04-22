from playwright.sync_api import expect

def test_select_device(select_device):
    print("test_select_device: Device selected and dashboard loaded.")
    expect(select_device.title).not_to_be_visible(timeout=5000)
    assert "dashboard" in select_device.page.url.lower(), "Page should be on the dashboard after device selection"