from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class CreateNamespace(object):
    def __init__(self, driver):
        self.driver = driver

        self.CreateNew_H = (By.XPATH, Locator.CreateNew_H)
        self.NamespaceButton = (By.CSS_SELECTOR, Locator.NamespaceButton)
        self.NamespaceName_bar = (By.CSS_SELECTOR, Locator.NamespaceName_bar)
        self.Create_button_N = (By.XPATH, Locator.Create_button_N)
        self.wait_toCreateNamespace = (By.XPATH, Locator.wait_toCreateNamespace)

        self.check_crateMessage = (By.XPATH, Locator.check_crateMessage)
        self.Namespace_settings = (By.XPATH, Locator.Namespace_settings)
        self.deleteButton_namespace = (By.XPATH, Locator.deleteButton_namespace)
        self.Application_namebox_D = (By.XPATH, Locator.Application_namebox_D)
        self.Delete_permanently_button = (By.XPATH, Locator.Delete_permanently_button)

        self.Organization = (By.XPATH, Locator.Organization)
        self.Organization_searchBar = (By.XPATH, Locator.Organization_searchBar)
        self.Choose_Default = (By.XPATH, Locator.Choose_Default)
        self.Choose_firstOrganization = (By.XPATH, Locator.Choose_firstOrganization)

        self.CPU_bar = (By.XPATH, Locator.CPU_bar)
        self.Memory_box = (By.XPATH, Locator.Memory_box)
        self.Volume_box = (By.XPATH, Locator.Volume_box)
        self.Bandwidth_box = (By.XPATH, Locator.Bandwidth_box)

    def getCreateNew_H(self):
        return self.CreateNew_H

    def getNamespaceButton(self):
        return self.NamespaceButton

    def getNamespaceName_bar(self):
        return self.NamespaceName_bar

    def getCreate_button_N(self):
        return self.Create_button_N

    def getwait_toCreateNamespace(self):
        return self.wait_toCreateNamespace

    def getcheck_crateMessage(self):
        return self.check_crateMessage

    def getNamespace_settings(self):
        return self.Namespace_settings

    def getdeleteButton_namespace(self):
        return self.deleteButton_namespace

    def getApplication_namebox_D(self):
        return self.Application_namebox_D

    def getDelete_permanently_button(self):
        return self.Delete_permanently_button

    def getOrganization(self):
        return self.Organization

    def getOrganization_searchBar(self):
        return self.Organization_searchBar

    def getChoose_Default(self):
        return self.Choose_Default

    def getChoose_firstOrganization(self):
        return self.Choose_firstOrganization

    def getCPU_bar(self):
        return self.CPU_bar

    def getMemory_box(self):
        return self.Memory_box

    def getVolume_box(self):
        return self.Volume_box

    def getBandwidth_box(self):
        return self.Bandwidth_box
