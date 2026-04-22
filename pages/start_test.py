
from datetime import datetime


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

    def start_test(self, template_name, file_prefix="", is_attached=False, same_as_test_name=False):
        self.quick_command_button.click()
        self.start_test_item.click()
        # self.page.wait_for_timeout(1000)
        self.template_dropdown.click()
        # self.page.wait_for_timeout(1000)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.template_dropdown.fill(f"{template_name}-{timestamp}")
        self.page.keyboard.press("Enter")
        # self.page.wait_for_timeout(1000)
        if is_attached:
            self.is_attached_checkbox.check()
        if same_as_test_name:
            self.same_as_test_name_checkbox.check()
        else:
            self.same_as_test_name_checkbox.uncheck()
            self.file_prefix_input.fill(f"{file_prefix}-{timestamp}")
        self.ok_button.click()
        # self.page.pause()

    