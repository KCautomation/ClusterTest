from Src.all_locators.Locators import Locator
from selenium.webdriver.common.by import By


class LogInPage(object):
    def __init__(self, driver):
        self.driver = driver

        self.Email_box = driver.find_element(By.XPATH, Locator.Email_box)
        self.Password_box = driver.find_element(By.XPATH, Locator.Password_box)
        self.Toggle_Visibility_Button = driver.find_element(By.XPATH, Locator.Toggle_Visibility_Button)
        self.Sign_In_button = driver.find_element(By.XPATH, Locator.Sign_In_button)
        self.LogIn_Authentication_Error = driver.find_element(By.XPATH, Locator.LogIn_Authentication_Error)

    def get_email(self):
        return self.Email_box

    def get_Password(self):
        return self.Password_box

    def get_Toggle_Visibility_Button(self):
        return self.Password_box

    def get_Sign_In_button(self):
        return self.Sign_In_button

    def LogIn_Authentication_Error(self):
        return self.LogIn_Authentication_Error

