from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class PHP(object):
    def __init__(self, driver):
        self.driver = driver

        self.Laravel = (By.XPATH, Locator.Laravel)
        self.ApplicationName_box = (By.XPATH, Locator.ApplicationName_box)
        self.TeamBox_A = (By.XPATH, Locator.TeamBox_A)

    def getLaravel(self):
        return self.Laravel

    def getApplicationName_box(self):
        return self.ApplicationName_box

    def getTeamBox_A(self):
        return self.ApplicationName_box
