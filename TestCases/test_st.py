import json
import time
import pytest
from POM.login_page import LoginPage
from POM.checkoupage import CheckoutPage
from Utilities.TestDataReading import load_properties

data = load_properties("TestData/testdata.properties")



@pytest.mark.run(order=1)
def test_login_05(driver):
    # Load test data
    login_page = LoginPage(driver)
    login_page.load_page(data["url"])
    login_page.enter_username(data["username"])
    login_page.enter_password(data["password"])
    login_page.click_login()
    time.sleep(5)
    login_page.click_Add_to_cart()
    login_page.click_Shopping_cart()
    x = CheckoutPage(driver)
    x.click_checkout()
    x.Verify_first_name()