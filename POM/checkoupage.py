import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.checkout = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID,"last-name")
        self.zip_code = (By.NAME,"postalCode")
        self.continue_button = (By.ID,"continue")


    def click_checkout(self):
        self.driver.find_element(*self.checkout).click()
        time.sleep(5)
    def Verify_first_name(self):
        return self.driver.find_element(*self.first_name).is_displayed()

    def enter_first_name(self, firstname):
        self.driver.find_element(*self.first_name).send_keys(firstname)
    def enter_last_name(self, lastname):
        self.driver.find_element(*self.last_name).send_keys(lastname)
    def enter_zip_code(self, zipcode):
        self.driver.find_element(*self.zip_code).send_keys(zipcode)
    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

