from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class CreateDatabase(object):
    def __init__(self, driver):
        self.driver = driver

        self.MySQL_button = (By.XPATH, Locator.MySQL_button)
        self.teamBox_database = (By.XPATH, Locator.teamBox_database)
        self.defaultTeam_database = (By.XPATH, Locator.defaultTeam_database)

        self.namespace_first = (By.XPATH, Locator.namespace_first)
        self.database_ServerName = (By.XPATH, Locator.database_ServerName)
        self.initial_AdminPassword = (By.XPATH, Locator.initial_AdminPassword)

        self.confirm_Password = (By.XPATH, Locator.confirm_Password)
        self.selectVersion_box = (By.XPATH, Locator.selectVersion_box)
        self.version_8_0_19 = (By.XPATH, Locator.version_8_0_19)

        self.enableWebClient = (By.XPATH, Locator.enableWebClient)
        self.next_button = (By.XPATH, Locator.next_button)

        self.confirm_button = (By.XPATH, Locator.confirm_button)
        self.Database_CreatedMsg = (By.XPATH, Locator.Database_CreatedMsg)
        self.WaitTo_Create = (By.XPATH, Locator.WaitTo_Create)

        self.Cancel_msg = (By.XPATH, Locator.Cancel_msg)
        self.Event_log = (By.XPATH, Locator.Event_log)

    def getMySQL_button(self):
        return self.MySQL_button

    def getteamBox_database(self):
        return self.teamBox_database

    def getdefaultTeam_database(self):
        return self.defaultTeam_database

    def getnamespace_first(self):
        return self.namespace_first

    def getdatabase_ServerName(self):
        return self.database_ServerName

    def getinitial_AdminPassword(self):
        return self.initial_AdminPassword

    def getconfirm_Password(self):
        return self.confirm_Password

    def gettselectVersion_box(self):
        return self.selectVersion_box

    def getversion_8_0_19(self):
        return self.version_8_0_19

    def getenableWebClient(self):
        return self.enableWebClient

    def getnext_button(self):
        return self.next_button

    def getconfirm_button(self):
        return self.confirm_button

    def getDatabase_CreatedMsg(self):
        return self.Database_CreatedMsg

    def getWaitTo_Create(self):
        return self.WaitTo_Create

    def getCancel_msg(self):
        return self.Cancel_msg

    def getEvent_log(self):
        return self.Event_log
