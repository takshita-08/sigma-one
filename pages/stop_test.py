import logging


class StopTest:
    def __init__(self, page):
        self.page = page
        self.quick_command_button = page.get_by_role("button", name="Quick Command")
        self.stop_test_item = page.get_by_role("listitem", name="Stop Test")
        self.toast_message = page.get_by_text("already stopped", exact=False)
        self.success_toast_message = page.get_by_text("Stop test notification sent successfully", exact=False)

    def stop_test_from_centra(self):
        try:
            self.toast_message.wait_for(state="visible", timeout=1000)
            logging.info("Test already stopped")
            print("🔹 Stop Test: Test is already stopped. Skipping stop test command.")
            return
        except:
            pass
        
        self.quick_command_button.click()
        self.stop_test_item.click()
        # self.page.pause()
        logging.info("🔹 Stop Test: Stop command executed.")