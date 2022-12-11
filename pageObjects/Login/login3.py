from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.useremail = driver.find_element(By.XPATH, Locator.textbox_Email_xpath)
        self.password = driver.find_element(By.XPATH, Locator.textbox_Password_xpath)
        self.signin_button = driver.find_element(By.XPATH, Locator.Sign_In_button)

    def getSearchText(self):
        return self.useremail

    def getSubmit(self):
        return self.password

    def getWebPageLogo(self):
        return self.signin_button
