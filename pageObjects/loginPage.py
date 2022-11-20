from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_Email_xpath = "//input[@id='mat-input-0']"  # xpath
    textbox_Password_xpath = "//input[@id='mat-input-1']"  # xpath
    button_ToggleVisibility = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                              "4]/button "  # xpath
    button_SignI_xpath = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"
    alert_LogInAuthenticationError = "//body[1]/kc-toastr[1]/div[1]/div[1]"

    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_linktext = "Logout"

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
