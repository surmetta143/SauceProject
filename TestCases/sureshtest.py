from selenium import webdriver
from selenium.webdriver.common.by import By
import  time



driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://www.saucedemo.com/")

time.sleep(5)

driver.find_element(By.ID,"user-name").send_keys("standard_user")

driver.find_element(By.ID,"password").send_keys("secret_sauce")
time.sleep(10)
driver.find_element(By.ID,"login-button").click()
time.sleep(5)
