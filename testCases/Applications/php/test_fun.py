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
    ServerName = "testSql0233"
    Password = "Qwer1235!!"

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Laravel_default_01(self, setup):
        # pytest.skip("Skipping test...later I will implement...")

        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

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

        print("****************** Try to  Create PHP Application With PHP: *********************")

        ApplicationName = "test330"
        Laravel_Version = app.Laravel_version_5_7
        Team = app.Team_Default
        try:
            self.create.Laravel_application(self, ApplicationName, Team, Laravel_Version)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
