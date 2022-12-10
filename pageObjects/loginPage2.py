from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class LoginPage:
    # Login Page
    textbox_username_xpath = Locator.Email_box
    textbox_password_xpath = Locator.Password_box
    Toggle_VisibilityButton_xpath = Locator.Toggle_Visibility_Button
    button_login_xpath = Locator.Sign_In_button
    link_logout_xpath = Locator.button_Logout_xpath

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_xpath).clear()
        self.driver.find_element_by_id(self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_xpath).clear()
        self.driver.find_element_by_id(self.textbox_password_xpath).send_keys(password)

    def clickToggleButton(self):
        self.driver.find_element_by_xpath(self.Toggle_VisibilityButton_xpath).click()

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_xpath).click()
