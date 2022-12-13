from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class CreateCache(object):
    def __init__(self, driver):
        self.driver = driver

        self.redis_button = (By.XPATH, Locator.redis_button)
        self.teamBox_c = (By.XPATH, Locator.teamBox_c)
        self.DefaultTeam_cache = (By.XPATH, Locator.DefaultTeam_cache)
        self.Namespace_c = (By.XPATH, Locator.Namespace_c)

        self.serverNameBox_c = (By.XPATH, Locator.serverNameBox_c)
        self.adminPassword_c = (By.XPATH, Locator.adminPassword_c)
        self.confirmPassword_c = (By.XPATH, Locator.confirmPassword_c)

        self.Cache_Version_6_0_5 = (By.XPATH, Locator.Cache_Version_6_0_5)

        self.Enable_Web_Client_P3_X_Redis = (By.XPATH, Locator.Enable_Web_Client_P3_X_Redis)
        self.Web_Client_Email = (By.XPATH, Locator.Web_Client_Email_cache)
        self.Web_Client_Password = (By.XPATH, Locator.Web_Client_Password_cache)

        self.selectVersion_c = (By.XPATH, Locator.selectVersion_c)
        self.version_6_0_5 = (By.XPATH, Locator.version_6_0_5)
        self.next_button = (By.XPATH, Locator.next_button)

        self.confirm_button = (By.XPATH, Locator.confirm_button)
        self.Cache_createdMsg = (By.XPATH, Locator.Cache_createdMsg)

        # delete cache
        self.Cache_S = (By.XPATH, Locator.Cache_S)
        self.Cache_Settings = (By.XPATH, Locator.Cache_Settings)
        self.Cache_Delete = (By.XPATH, Locator.Cache_Delete)
        self.Cache_namebox_D = (By.XPATH, Locator.Cache_namebox_D)
        self.Cache_Deleted_Success_msg = (By.XPATH, Locator.Cache_Deleted_Success_msg)

        self.Delete_permanently_button = (By.XPATH, Locator.Delete_permanently_button)

    def getCache_Version_6_0_5(self):
        return self.Cache_Version_6_0_5

    def getEnable_Web_Client_P3_X_Redis(self):
        return self.Enable_Web_Client_P3_X_Redis

    def getWeb_Client_Email(self):
        return self.Web_Client_Email

    def getWeb_Client_Password(self):
        return self.Web_Client_Password

    def getredis_button(self):
        return self.redis_button

    def getteamBox_c(self):
        return self.teamBox_c

    def getDefaultTeam_cache(self):
        return self.DefaultTeam_cache

    def getNamespace_c(self):
        return self.Namespace_c

    def getserverNameBox_c(self):
        return self.serverNameBox_c

    def getadminPassword_c(self):
        return self.adminPassword_c

    def getconfirmPassword_c(self):
        return self.confirmPassword_c

    def getselectVersion_c(self):
        return self.selectVersion_c

    def getversion_6_0_5(self):
        return self.version_6_0_5

    def getnext_button(self):
        return self.next_button

    def getconfirm_button(self):
        return self.confirm_button

    def getCache_createdMsg(self):
        return self.Cache_createdMsg

    def getCache_S(self):
        return self.Cache_S

    def getCache_Settings(self):
        return self.Cache_Settings

    def getCache_Delete(self):
        return self.Cache_Delete

    def getCache_namebox_D(self):
        return self.Cache_namebox_D

    def getCache_Deleted_Success_msg(self):
        return self.Cache_Deleted_Success_msg
