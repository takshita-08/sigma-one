
from datetime import datetime
import logging


class StartTest:
    def __init__(self, page):
        
        self.page = page
        self.quick_command_button = page.get_by_role("button", name="Quick Command")
        self.start_test_item = page.get_by_role("listitem", name="Start Test")
        self.template_dropdown = page.get_by_role("combobox", name="testTemplateId")
        self.file_prefix_input = page.get_by_test_id("testFilePrefix")
        self.is_attached_checkbox = page.get_by_test_id("testIsAttached")
        self.same_as_test_name_checkbox = page.get_by_test_id("testFilePrefixAsTemplateName")
        self.ok_button = page.get_by_role("button", name="OK")
        self.success_message = page.get_by_text("Start test notification sent successfully", exact=False)
        self.toast_message = page.get_by_text("Test is already started", exact=False)
        # self.file_name = None
        # self.toast_message = page.locator(".Toastify__toast-body")
        
    def start_test_from_centra(self, template_name, file_name="", is_attached=False, same_as_test_name=False):
        self.quick_command_button.click()
        self.start_test_item.click()

        try:
            self.toast_message.wait_for(state="visible", timeout=5000)
            logging.info("Test already started")
            print("🔹 Start Test: Test is already started. Skipping start test command.")
            return True
        except Exception as e:
            print(f"Toast not visible: {e}")
        
        self.template_dropdown.click()
        # timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        self.template_dropdown.fill(template_name)
        self.page.keyboard.press("Enter")
        if is_attached:
            self.is_attached_checkbox.check()
        if same_as_test_name:
            self.same_as_test_name_checkbox.check()
        else:
            self.same_as_test_name_checkbox.uncheck()
            # self.file_name = f"{file_prefix}-{timestamp}"
            self.file_prefix_input.fill(file_name)
            print(file_name)
        self.ok_button.click()
        logging.info("🔹 Start Test: Starting test with template: %s", template_name)
        # self.page.pause()

    