import time
import logging
import pytest
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.loginPage import LogInPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl
from utilities import XLUtils
from selenium import webdriver
from Src.login_function.login import login
from Src.functions.database.createDatabase import DatabaseFunctions

from Src.screenShot.screenShot import SS
import time
import pytest

import simple_colors
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from urllib.request import urlopen
from urllib.error import *
from utilities.readProperties import ReadConfig

ss_path = "/Database/"


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()
    ServerName = "test_mysql"
    Password = "Qwer1234!!"

    @pytest.mark.regression
    def test_createDatabase(self, setup):

        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)

        ApplicationName = "laravel-0170"

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go create database page *********************")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.DF.go_createPage(self)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to choose MySQL database *********************")

        try:
            MySQL_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.MySQL_button)))
            if MySQL_button.is_displayed():
                MySQL_button.click()
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "MySQL_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose MySQL_button")

        print("****************** Try to choose Team *********************")

        print("---try to click team box---")
        try:
            teamBox_database = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.teamBox_database)))
            if teamBox_database.is_displayed():
                teamBox_database.click()
                time.sleep(2)
            else:
                file_name = ss_path + "teamBox_database" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on team box")

        print("-----------------------try to choose default as a team-------------------------------")

        try:
            defaultTeam_database = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.defaultTeam_database)))
            if defaultTeam_database.is_displayed():
                defaultTeam_database.click()
                time.sleep(2)
            else:
                file_name = ss_path + "defaultTeam_database" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose default Team")

        print("-----Scroll down to show Namespaces-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose a namespace -------------------------------")

        try:
            namespace_first = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.namespace_first)))
            if namespace_first.is_displayed():
                namespace_first.click()
                time.sleep(2)
            else:
                file_name = ss_path + "namespace_first" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put First Namespace")

        print("-----------------------try to put database server name -------------------------------")

        try:
            database_ServerName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.database_ServerName)))
            if database_ServerName.is_displayed():
                database_ServerName.send_keys(self.ServerName)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "database_ServerName" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put Database ServerName")

        print("-----------------------try to put database Password -------------------------------")

        try:
            initial_AdminPassword = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.initial_AdminPassword)))
            if initial_AdminPassword.is_displayed():
                initial_AdminPassword.send_keys(self.Password)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "initial_AdminPassword" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial AdminPassword")

        print("-----------------------try to put database Password -------------------------------")

        try:
            confirm_Password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.confirm_Password)))
            if confirm_Password.is_displayed():
                confirm_Password.send_keys(self.Password)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_Password" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial confirm_Password")

        print("-----Scroll down to show Namespaces-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)

        print("-----------------------try to choose Team as a default-------------------------------")

        try:
            selectVersion_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.selectVersion_box)))
            if selectVersion_box.is_displayed():
                selectVersion_box.click()
                time.sleep(2)
            else:
                file_name = ss_path + "selectVersion_box" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on selectVersion_box")

        try:
            version_8_0_19 = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.version_8_0_19)))
            if version_8_0_19.is_displayed():
                version_8_0_19.click()
                time.sleep(2)
            else:
                file_name = ss_path + "version_8_0_19" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose version 8.0.19")
