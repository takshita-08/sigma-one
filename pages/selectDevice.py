class SelectDevice:
    def __init__(self, page):
        self.page = page
        self.device_filter_btn = page.get_by_role("button", name="Device Filter")
        self.device = page.get_by_test_id("Sigma-One")
        self.device_id = page.get_by_role("combobox", name="testDeviceId")
        self.phone_id = page.get_by_role("combobox", name="testPhoneId")
        self.apply_btn = page.get_by_role("button", name="Apply")
        self.title = page.get_by_role("heading", name="Select Device")


    def select_device(self, device_id, device_serial):
        self.device_filter_btn.click()
        self.device.click()
        self.page.wait_for_timeout(1000)
        self.device_id.click()
        self.device_id.fill(device_id)
        self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(1000)
        self.phone_id.click()
        self.phone_id.fill(device_serial)
        self.page.keyboard.press("Enter")
        self.apply_btn.click()
        self.page.wait_for_timeout(1000)