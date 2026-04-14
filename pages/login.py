import config
from playwright.sync_api import expect, TimeoutError

class Login:
    def __init__(self, page) -> None:
        self.page = page
        self.username = page.get_by_test_id("testUsername")
        self.password = page.get_by_test_id("testPassword")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error = page.get_by_test_id("error")
        self.title = page.get_by_role("heading", name="Log in to your account")
        self.confirm_btn = page.get_by_role("button", name="Confirm")

    def load_page(self):
        self.page.goto(config.BASE_URL)

    def login(self,username,password):
        # Enter credentials
        self.username.fill(username)
        self.password.fill(password)
        # self.page.wait_for_timeout(5000)

        # Click login
        self.login_btn.click()

        
        try:
            expect(self.confirm_btn).to_be_visible(timeout=3000)
            self.confirm_btn.click()
        except TimeoutError:
            pass



