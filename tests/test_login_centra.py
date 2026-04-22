import re

from playwright.sync_api import expect
import pytest


@pytest.mark.parametrize("username, password", [
    ("testtks", "Meritech@123"),
    ("takshita", "Meritech@123" )
])
def test_login_valid(login,username, password):
    login.login_fnc(username, password)
    expect(login.error).not_to_be_visible(timeout=5000)
    expect(login.title).not_to_be_visible(timeout=5000)
    assert "login" not in login.page.url.lower(), "Page should navigate away from the login screen after successful authentication"

@pytest.mark.parametrize("username, password", [
    ("invalid_user", "invalid_pass"),
    ("testtks", "wrong_password"),])
def test_login_invalid(login, username, password):
    login.login_fnc(username, password)
    expect(login.error).to_be_visible(timeout=5000)
    expect(login.title).to_be_visible(timeout=5000)
    expect(login.toast).to_contain_text(
    re.compile("Username or password|Account locked"))
    assert "login" in login.page.url.lower(), "Page should remain on the login screen after failed authentication"