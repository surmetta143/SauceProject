import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.__checkout = (By.ID, "checkout")
        self.__first_name = (By.ID, "first-name")
        self.__last_name = (By.ID,"last-name")

    def click_checkout(self):
        self.driver.find_element(*self.__checkout).click()
        time.sleep(5)
    def Verify_first_name(self):
        return self.driver.find_element(*self.__first_name).is_displayed()

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.__first_name).send_keys(firstname)
    def enter_last_name(self, lastname):
        self.driver.find_element(*self.__last_name).send_keys(lastname)

