import logging
import time

import allure
import pytest
import simple_colors
from colorama import Fore
from selenium.webdriver import Keys, ActionChains

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.functions.database.createDatabase import DatabaseFunctions
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.applications.application_functions import ApplicationFunctions
from pageObjects.Apllications.pomCreateApplication import CreateApplication
from Src.functions.applications.create_php import PHPApplication

ss_path = "/Database/"


@allure.severity(allure.severity_level.CRITICAL)
class TestPHPApplication:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()

    appFunction = ApplicationFunctions()
    create = PHPApplication()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Laravel_default_02(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test334"
        Laravel_Version = app.Laravel_version_6_0
        Team = app.Team_Default

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e,
                  "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go Create Application page *********************")
        try:
            self.appFunction.go_CreateAppPage(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to  Create PHP Application TC-001 *********************")

        try:
            print("*********** Try to  Create PHP Application With PHP Version: 7.3 & Laravel Version: 6.0*********")
            self.create.Laravel_application(self, ApplicationName, Team, Laravel_Version)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.deployApplication(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        # check deployed status
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Laravel_default_03(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test335"
        Laravel_Version = app.Laravel_version_5_8
        Team = app.Team_Default

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e,
                  "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go Create Application page *********************")
        try:
            self.appFunction.go_CreateAppPage(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to  Create PHP Application TC-001 *********************")

        try:
            print("*********** Try to  Create PHP Application With PHP Version: 7.3 & Laravel Version: 5.8*********")
            self.create.Laravel_application(self, ApplicationName, Team, Laravel_Version)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.deployApplication(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        # check deployed status
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Laravel_default_04(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test335"
        Laravel_Version = app.Laravel_version_5_7
        Team = app.Team_Default

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e,
                  "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go Create Application page *********************")
        try:
            self.appFunction.go_CreateAppPage(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to  Create PHP Application TC-001 *********************")

        try:
            print("*********** Try to  Create PHP Application With PHP Version: 7.3 & Laravel Version: 5.7*********")
            self.create.Laravel_application(self, ApplicationName, Team, Laravel_Version)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.deployApplication(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        # check deployed status
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)


    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Laravel_default_05(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test335"
        Laravel_Version = app.Laravel_version_5_6
        Team = app.Team_Default

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e,
                  "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go Create Application page *********************")
        try:
            self.appFunction.go_CreateAppPage(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to  Create PHP Application TC-001 *********************")

        try:
            print("*********** Try to  Create PHP Application With PHP Version: 7.3 & Laravel Version: 5.7*********")
            self.create.Laravel_application(self, ApplicationName, Team, Laravel_Version)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.deployApplication(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        # check deployed status
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)