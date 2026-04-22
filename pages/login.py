import utils.config as config
from playwright.sync_api import expect, TimeoutError

class Login:
    def __init__(self, page) -> None:
        self.page = page
        self.username = page.get_by_test_id("testUsername")
        self.password = page.get_by_test_id("testPassword")
        self.login_btn = page.get_by_role("button", name="Login")
        self.error = page.get_by_test_id("testError")
        self.toast = page.locator(".Toastify__toast")
        self.title = page.get_by_role("heading", name="Log in to your account")
        self.confirm_btn = page.get_by_role("button", name="Confirm")

    def load_page(self):
        self.page.goto(config.BASE_URL, wait_until="domcontentloaded")
        expect(self.title).to_be_visible(timeout=10000)

    def login_fnc(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()

        try:
            self.confirm_btn.wait_for(state="visible", timeout=5000)
            self.confirm_btn.click()
        except (TimeoutError, AssertionError):
            pass  




