from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class DeleteApplication(object):
    def __init__(self, driver):
        self.driver = driver

        self.Applications = (By.XPATH, Locator.Applications)
        self.application_Settings = (By.XPATH, Locator.application_Settings)
        self.application_Delete = (By.XPATH, Locator.application_Delete)
        self.Application_namebox_D = (By.XPATH, Locator.Application_namebox_D)
        self.Delete_permanently_button = (By.XPATH, Locator.Delete_permanently_button)
        self.Application_Deleted_Success_msg = (By.XPATH, Locator.Application_Deleted_Success_msg)
        self.Application_Initialization_failed = (By.XPATH, Locator.Application_Initialization_failed)
        self.delete_icon = (By.XPATH, Locator.DeleteApp_byIcon)
        self.okay_button = (By.XPATH, Locator.Okay_button)


    def getdelete_icon(self):
        return self.delete_icon
    def getApplication_Initialization_failed(self):
        return self.Application_Initialization_failed

    def getApplications(self):
        return self.Applications

    def getApplication_Settings(self):
        return self.application_Settings

    def getApplication_namebox_D(self):
        return self.Application_namebox_D

    def getDelete_permanently_button(self):
        return self.Delete_permanently_button

    def getApplication_Deleted_Success_msg(self):
        return self.Application_Deleted_Success_msg
