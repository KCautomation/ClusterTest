from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class Login3(object):
    def __init__(self, driver):
        self.driver = driver

        self.useremail = driver.find_element(By.XPATH, Locator.textbox_Email_xpath)
        self.password = driver.find_element(By.XPATH, Locator.textbox_Password_xpath)
        self.signin_button = driver.find_element(By.XPATH, Locator.Sign_In_button)

    def User_Name(self):
        return self.useremail

    def getVisit_Us(self):
        return self.useremail

    def get_SignIn(self):
        return self.signin_button

    def ToggleVisibility(self):
        return self.ToggleVisibility
