from selenium.webdriver.common.by import By
from Src.Locators import Locator


class LoginPage:
    # Login Page
    def __init__(self, driver):
        self.driver = driver

        self.Email_box = driver.find_element(By.XPATH, Locator.textbox_Email_xpath)
        self.Password_box = driver.find_element(By.XPATH, Locator.textbox_Password_xpath)
        self.Toggle_Visibility_Button = driver.find_element(By.XPATH, Locator.button_ToggleVisibility)
        self.Sign_In_button = driver.find_element(By.XPATH, Locator.button_SignI_xpath)
        self.LogIn_Authentication_Error = driver.find_element(By.XPATH, Locator.alert_LogInAuthenticationError)
        self.user_profile_Icon_xpath = driver.find_element(By.XPATH, Locator.user_profile_Icon_xpath)
        self.button_Logout_xpath = driver.find_element(By.XPATH, Locator.button_Logout_xpath)

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

    def user_profile_Icon_xpath(self):
        return self.Sign_In_button

    def button_Logout_xpath(self):
        return self.LogIn_Authentication_Error

