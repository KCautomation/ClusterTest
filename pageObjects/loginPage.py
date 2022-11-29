from selenium.webdriver.common.by import By
from Src.Locators import Locator


class LoginPage:
    # Login Page
    textbox_Email_xpath = Locator.textbox_Email_xpath
    textbox_Password_xpath = Locator.textbox_Password_xpath
    button_ToggleVisibility = Locator.textbox_Password_xpath
    button_SignI_xpath = Locator.button_SignI_xpath
    alert_LogInAuthenticationError = Locator.alert_LogInAuthenticationError
    user_profile_Icon_xpath = Locator.user_profile_Icon_xpath
    button_Logout_xpath = Locator.button_Logout_xpath

    # textbox_Email_xpath = "//input[@id='mat-input-0']"  # xpath
    # textbox_Password_xpath = "//input[@id='mat-input-1']"  # xpath
    # button_ToggleVisibility = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
    #                           "4]/button "  # xpath
    # button_SignI_xpath = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"
    # alert_LogInAuthenticationError = "//body[1]/kc-toastr[1]/div[1]/div[1]"
    # user_profile_Icon_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/kc-toolbar-user/div"
    # button_Logout_xpath = "//span[normalize-space()='LOGOUT']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, useremail):
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Email_xpath).send_keys(useremail)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_SignI_xpath).click()

    def clickSignIn(self):
        self.driver.find_element(By.XPATH, self.button_ToggleVisibility).click()

    def CheckAuthenticationError(self):
        self.driver.find_element(By.XPATH, self.alert_LogInAuthenticationError)

    def ClickProfile(self):
        self.driver.find_element(By.XPATH, self.user_profile_Icon_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_Logout_xpath).click()

