from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class CreateApplication(object):
    def __init__(self, driver):
        self.driver = driver

        self.Laravel = (By.XPATH, Locator.Laravel)
        self.ApplicationName_box = (By.XPATH, Locator.ApplicationName_box)
        self.TeamBox_A = (By.XPATH, Locator.TeamBox_A)

        self.Team_Default = (By.XPATH, Locator.Team_Default)
        self.Next_button = (By.XPATH, Locator.Next_button)
        self.Choose_Namespace_one = (By.XPATH, Locator.Choose_Namespace_one)

        self.Save_button_A = (By.XPATH, Locator.Save_button_A)
        self.Create_Application = (By.XPATH, Locator.Create_Application)
        self.New_Git_Commit_Pushed_msg = (By.XPATH, Locator.New_Git_Commit_Pushed_msg)
        self.Application_build_finished_successfully_msg = (By.XPATH, Locator.Application_build_finished_successfully_msg)

        self.wait_ToCreateApplication = (By.XPATH, Locator.wait_ToCreateApplication)
        self.check_create_app = (By.XPATH, Locator.check_create_app)
        self.check_app_status = (By.XPATH, Locator.check_app_status)

    def getLaravel(self):
        return self.Laravel

    def getApplicationName_box(self):
        return self.ApplicationName_box

    def getTeamBox_A(self):
        return self.ApplicationName_box

    def getChoose_Namespace_one(self):
        return self.Choose_Namespace_one

    def getNext_button(self):
        return self.Next_button

    def getTeam_Default(self):
        return self.Team_Default

    def getSave_button_A(self):
        return self.Save_button_A

    def getCreate_Application(self):
        return self.Create_Application

    def getNew_Git_Commit_Pushed_msg(self):
        return self.New_Git_Commit_Pushed_msg

    def getApplication_build_finished_successfully_msg(self):
        return self.Application_build_finished_successfully_msg

    def getwait_ToCreateApplication(self):
        return self.wait_ToCreateApplication

    def getwait_check_create_app(self):
        return self.check_create_app

    def getwait_check_app_status(self):
        return self.check_app_status

