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

ss_path = "/Applications/"


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
    ServerName = "testSql0233"
    Password = "Qwer1235!!"

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_PHPApplication(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        ApplicationName = "test317"
        self.logger.info("*************** Test Create Namespace With Access Group: Company*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # overview
        try:

            Overview = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Overview_button)))
            if Overview.is_Displayed:
                Overview.click()

                # scroll down
                action.send_keys(Keys.PAGE_DOWN)
                action.perform()

                time.sleep(1)

                action.send_keys(Keys.PAGE_DOWN)
                action.perform()

                time.sleep(1)

                action.send_keys(Keys.PAGE_DOWN)
                action.perform()
                time.sleep(1)

                print("Scroll down")
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # PipelineConfig
        try:

            PipelineConfig = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.PipelineConfig_button)))
            if PipelineConfig.is_Displayed:
                PipelineConfig.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # Config_button
        try:

            ResourcesConfig = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Resources_Config_button)))
            if ResourcesConfig.is_Displayed:
                ResourcesConfig.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # ExternalEndpoints
        try:

            ExternalEndpoints = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.External_Endpoints_button)))
            if ExternalEndpoints.is_Displayed:
                ExternalEndpoints.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # EnvironmentVariables
        try:

            EnvironmentVariables = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Environment_Variables_button)))
            if EnvironmentVariables.is_Displayed:
                EnvironmentVariables.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # Secrets
        try:

            Secrets = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Secrets_button)))
            if Secrets.is_Displayed:
                Secrets.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # Monitoring
        try:

            Monitoring = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Monitoring_button)))
            if Monitoring.is_Displayed:
                Monitoring.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # Logs_button
        try:

            Logs = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.Logs_button)))
            if Logs.is_Displayed:
                Logs.click()
                self.driver.implicitly_wait(10)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
