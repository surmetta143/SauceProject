import json
import time
import pytest
from POM.login_page import LoginPage
from Utilities.TestDataReading import load_properties
from POM.logoutpage import LogoutPage

data = load_properties("TestData/testdata.properties")


@pytest.mark.smoke
@pytest.mark.run(order=4)

def test_logout_30(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    assert login_page.is_username_displayed(), "Username field is not displayed"
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()

    logout_page=LogoutPage(driver)
    logout_page.click_threelines_button()
    logout_page.click_logout_button()
    login_page.Verify_login_btn()
