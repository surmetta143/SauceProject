import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators



        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.sort_dropdown = (By.XPATH, "//*[@data-test='product-sort-container']")
        self.Add_to_cart_btn =(By.XPATH, "//*[@name='add-to-cart-sauce-labs-backpack']")
        self.remove_btn = (By.ID,"remove-sauce-labs-backpack")
        self.Shopping_cart = (By.XPATH, "//*[@data-test='shopping-cart-link']")


    def load_page(self, url):
        self.driver.get(url)
        time.sleep(5)

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(5)

    def is_username_displayed(self):
        return self.driver.find_element(*self.username_field).is_displayed()

    def select_sort_option(self, option_text):
        dropdown = self.driver.find_element(*self.sort_dropdown)
        Select(dropdown).select_by_visible_text(option_text)
        time.sleep(5)
    def click_Add_to_cart(self):
        self.driver.find_element(*self.Add_to_cart_btn).click()
        time.sleep(5)

    def Verify_Remove_btn(self):
        return self.driver.find_element(*self.remove_btn).is_displayed()

    def Verify_login_btn(self):
        return self.driver.find_element(*self.login_button).is_displayed()

    def click_Shopping_cart(self):
        self.driver.find_element(*self.Shopping_cart).click()
        time.sleep(5)


