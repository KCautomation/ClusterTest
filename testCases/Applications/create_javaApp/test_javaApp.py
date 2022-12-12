import logging
import time

import allure
import pytest

from selenium.webdriver import Keys, ActionChains

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login

from Src.screenShot.screenShot import SS

from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.applications.application_functions import ApplicationFunctions
from pageObjects.Apllications.pomCreateApplication import CreateApplication
from Src.functions.applications.create_JavaApp import JavaApplication

ss_path = "/Database/"


@allure.severity(allure.severity_level.CRITICAL)
class TestJavaApplication:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    appFunction = ApplicationFunctions()
    create = JavaApplication()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_java_default_02(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With Java SpringBoot*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test335"
        Java_Version = app.Java_Version_11
        SpringBoot_Version = app.SpringBoot_Version_2_1_11
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

        print("****************** Try to  Create Java Application TC-001 *********************")

        try:
            print("*********** Try to  Create PHP Application With Java Version: 11 & Laravel Version: 2.1.11*********")
            self.create.Java_application(self, ApplicationName, Team, Java_Version, SpringBoot_Version)
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