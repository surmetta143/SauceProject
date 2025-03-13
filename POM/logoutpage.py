import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators



        self.threelines_button = (By.ID, "react-burger-menu-btn")
        self.logout_button= (By.ID, "logout_sidebar_link")





    def click_threelines_button(self):
        self.driver.find_element(*self.threelines_button).click()
        time.sleep(5)

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()
        time.sleep(5)




