from utils.config import UPLOAD_URL


class UploadedFiles:
    def __init__(self, page):
        self.page = page
        self.search_input = page.get_by_test_id("searchInput")
        self.search_data_btn = page.get_by_test_id("searchDataBtn")
        self.uploaded_files_table = page.get_by_role("table")
        self.rows = page.locator("tbody tr")
        self.file_type_col = page.locator("td:nth-child(4)")
        self.file_types = []


    def navigate_to_uploaded_files(self):
        self.page.goto(UPLOAD_URL)
        self.search_input.wait_for(state="visible", timeout=10000)
        
    def search_files(self, filename):
        self.search_input.fill(filename)
        self.search_data_btn.click()
        self.page.wait_for_timeout(5000)
        count = self.file_type_col.count()
        for i in range(count):
            cell = self.file_type_col.nth(i)
            self.file_types.append(cell.inner_text().strip().lower())

        return self.file_types