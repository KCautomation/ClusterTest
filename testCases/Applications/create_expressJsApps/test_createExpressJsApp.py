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
from Src.functions.applications.create_expressJsApp import javascriptApplication

ss_path = "/Database/"


@allure.severity(allure.severity_level.CRITICAL)
class TestJavascriptApplications:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()

    appFunction = ApplicationFunctions()
    create = javascriptApplication()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_expressjs_default_02(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With Javascript express js *****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

        ApplicationName = "test341"
        ExpressJs_Version = app.ExpressJs_Version_4_17_1
        Team = app.Team_Default

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
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

        print("****************** Try to  Create C# Application TC-002 *********************")

        try:
            print("*****Create C# Application With DotNet version: 2.2.14*****")
            self.create.expressJsApplication(self, ApplicationName, Team, ExpressJs_Version)
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
