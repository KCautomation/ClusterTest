from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator


class CreateApplication(object):
    def __init__(self, driver):
        self.driver = driver

        self.Laravel = (By.XPATH, Locator.Laravel)
        self.ApplicationName_box = (By.XPATH, Locator.ApplicationName_box)
        self.TeamBox_A = (By.XPATH, Locator.TeamBox_A)

        self.Team_Default = (By.XPATH, Locator.Team_Default)
        self.Team_None = (By.XPATH, Locator.Team_None)

        self.Next_button = (By.XPATH, Locator.Next_button)
        self.Choose_Namespace_one = (By.XPATH, Locator.Choose_Namespace_one)

        self.Save_button_A = (By.XPATH, Locator.Save_button_A)
        self.Create_Application = (By.XPATH, Locator.Create_Application)
        self.New_Git_Commit_Pushed_msg = (By.XPATH, Locator.New_Git_Commit_Pushed_msg)
        self.Application_build_finished_successfully_msg = (
            By.XPATH, Locator.Application_build_finished_successfully_msg)

        self.wait_ToCreateApplication = (By.XPATH, Locator.wait_ToCreateApplication)
        self.check_create_app = (By.XPATH, Locator.check_create_app)
        self.check_app_status = (By.XPATH, Locator.check_app_status)

        # Laravel

        self.Laravel_version_6_0 = (By.XPATH, Locator.Laravel_version_6_0)
        self.Laravel_version_5_8 = (By.XPATH, Locator.Laravel_version_5_8)
        self.Laravel_version_5_7 = (By.XPATH, Locator.Laravel_version_5_7)
        self.Laravel_version_5_6 = (By.XPATH, Locator.Laravel_version_5_6)

        # Dot Net
        self.DotNet = (By.XPATH, Locator.DotNet)
        self.DoNet_v_box = (By.XPATH, Locator.DoNet_v_box)
        self.DontNet_V_3_0 = (By.XPATH, Locator.DontNet_V_3_0)
        self.DotNet_V_2_2 = (By.XPATH, Locator.DotNet_V_2_2)
        self.DotNet_V_2_1 = (By.XPATH, Locator.DotNet_V_2_1)

        # java
        self.SpringBoot = (By.XPATH, Locator.SpringBoot)
        self.SpringBoot_Version_box = (By.XPATH, Locator.SpringBoot_Version_box)
        self.SpringBoot_Version_2_1_11 = (By.XPATH, Locator.SpringBoot_Version_2_1_11)
        self.Java_Version_box = (By.XPATH, Locator.Java_Version_box)
        self.Java_Version_11 = (By.XPATH, Locator.Java_Version_11)
        self.Java_Version_8 = (By.XPATH, Locator.Java_Version_8)

        # Python
        self.Django = (By.XPATH, Locator.Django)
        self.Python_version_box = (By.XPATH, Locator.Python_version_box)
        self.Python_version_3_7_8 = (By.XPATH, Locator.Python_version_3_7_8)
        self.Python_version_3_6_11 = (By.XPATH, Locator.Python_version_3_6_11)

        self.Django_version_box = (By.XPATH, Locator.Django_version_box)
        self.Django_Version_2_2_14 = (By.XPATH, Locator.Django_Version_2_2_14)

        # Golang
        self.Golang = (By.XPATH, Locator.Golang)
        self.Goecho_Version_box = (By.XPATH, Locator.Goecho_Version_box)
        self.Goecho_V_4_1_14 = (By.XPATH, Locator.Goecho_V_4_1_14)

    def getGoLang(self):
        return self.Golang

    def getGoecho_Version_box(self):
        return self.Goecho_Version_box

    def getGoecho_V_4_1_14(self):
        return self.Goecho_V_4_1_14

    def getDjango(self):
        return self.Django

    def getPython_version_box(self):
        return self.Python_version_box

    def getPython_version_3_7_8(self):
        return self.Python_version_3_7_8

    def getPython_version_3_6_11(self):
        return self.Python_version_3_6_11

    def getDjango_version_box(self):
        return self.Django_version_box

    def getDjango_Version_2_2_14(self):
        return self.Django_Version_2_2_14

    def getSpringBoot(self):
        return self.SpringBoot

    def getSpringBoot_Version_box(self):
        return self.SpringBoot_Version_box

    def getSpringBoot_Version_2_1_11(self):
        return self.SpringBoot_Version_2_1_11

    def getJava_Version_box(self):
        return self.Java_Version_box

    def getJava_Version_11(self):
        return self.Java_Version_11

    def getJava_Version_8(self):
        return self.Java_Version_8

    def getDotNet(self):
        return self.DotNet

    def getDoNet_v_box(self):
        return self.DoNet_v_box

    def getDontNet_V_3_0(self):
        return self.DontNet_V_3_0

    def getDotNet_V_2_2(self):
        return self.DotNet_V_2_2

    def getDotNet_V_2_1(self):
        return self.DotNet_V_2_1

    def getLaravel_version_6_0(self):
        return self.Laravel_version_6_0

    def getLaravel_version_5_8(self):
        return self.Laravel_version_5_8

    def getLaravel_version_5_7(self):
        return self.Laravel_version_5_7

    def getLaravel_version_5_6(self):
        return self.Laravel_version_5_6

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

    def getTeam_None(self):
        return self.Team_None

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
