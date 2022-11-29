class Locator(object):
    # Login Page
    textbox_Email_xpath = "//input[@id='mat-input-0']"  # xpath
    textbox_Password_xpath = "//input[@id='mat-input-1']"  # xpath
    button_ToggleVisibility = "/html/body/kc-root/kc-login/div/div[2]/div/form/div/mat-form-field[2]/div/div[1]/div[" \
                              "4]/button "  # xpath
    button_SignI_xpath = "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]"
    alert_LogInAuthenticationError = "//body[1]/kc-toastr[1]/div[1]/div[1]"
    user_profile_Icon_xpath = "/html/body/kc-root/kc-layout/div/mat-sidenav-container/mat-sidenav-content/kc-toolbar/div/kc-toolbar-user/div"
    button_Logout_xpath = "//span[normalize-space()='LOGOUT']"