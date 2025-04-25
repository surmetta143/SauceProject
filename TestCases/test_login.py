import json
import time
import pytest
from POM.login_page import LoginPage
from POM.checkoupage import CheckoutPage
from Utilities.TestDataReading import load_properties

data = load_properties("TestData/testdata.properties")


@pytest.mark.smoke
@pytest.mark.run(order=4)

def test_login_01(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    assert login_page.is_username_displayed(), "Username field is not displayed"
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    print("Login test passed")
    login_page.select_sort_option("Price (high to low)")
    print("Sort dropdown test passed")

@pytest.mark.smoke
@pytest.mark.run(order=3)

def test_login_02(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    assert login_page.is_username_displayed(), "Username field is not displayed"
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    print("Login test passed")
    login_page.select_sort_option("Price (high to low)")
    print("Sort dropdown test passed")

def test_loginb_03(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    assert login_page.is_username_displayed(), "Username field is not displayed"
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    print("Login test passed")
    login_page.select_sort_option("Price (high to low)")
    print("Sort dropdown test passed")


@pytest.mark.run(order=-1)
def test_logina_04(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    time.sleep(5)
    login_page.click_Add_to_cart()
    login_page.Verify_Remove_btn()


@pytest.mark.run(order=-1)
def test_logina_04(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    time.sleep(5)
    login_page.click_Add_to_cart()
    login_page.Verify_Remove_btn()


