import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.Locators import Locators  # if in a separate file

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("https://jovial-buttercream-da99f3.netlify.app/")
    driver.maximize_window()
    time.sleep(2)

    obj = Locators(driver)
    obj.ClickLoginButton()
    time.sleep(1)

    obj.EnterUsername("sureshff")
    obj.EnterPassword("passpr22")
    obj.ClickSubmit()
    time.sleep(2)

    obj.VerifyLoginSuccess()
    driver.quit()

def test_login_Fail():
    driver = webdriver.Chrome()
    driver.get("https://jovial-buttercream-da99f3.netlify.app/")
    driver.maximize_window()
    time.sleep(2)

    obj = Locators(driver)
    obj.ClickLoginButton()

    driver.find_element(By.XPATH, "//button[text()='Loged in']").click()

    time.sleep(1)


    obj.ClickSubmit()
    time.sleep(2)


    driver.quit()

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://jovial-buttercream-da99f3.netlify.app/")
    time.sleep(5)
    driver.find_element(By.ID,"Courses").is_displayed()

    driver.find_element(By.ID,"Courses").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"//button[@onclick='openForm('login')']").is_displayed()
    driver.quit()



