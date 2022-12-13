import logging
import time
import pytest
import simple_colors

import raf_practice.logs.customolog.custom_logger as cl
from Src.functions.cache.cacheFunction import cacheFunctions
from Src.login_function.login import login
from Src.functions.database.databaseFunctions import DatabaseFunctions
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from pageObjects.Database.pomDatabase import Database
from utilities.readProperties import ReadConfig
from pageObjects.Cache.pomCache import CreateCache

ss_path = "/Database/CreateDatabase/"


class TestCreateDatabase:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()
    CF = cacheFunctions()

    ServerName = "testSql0242"
    Password = "Qwer1235!!"

    @pytest.mark.regression
    def test_MySQLDatabase(self, setup):

        self.logger.info("*************** Test_Create Database *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        data = Database(self.driver)

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
            self.DF.go_createDatabasePage(self)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to choose MySQL database *********************")

        try:
            MySQL_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.MySQL_button))
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
                EC.presence_of_element_located(data.teamBox_database))
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
                EC.presence_of_element_located(data.defaultTeam_database))
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
                EC.presence_of_element_located(data.namespace_first))
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
            print("Successfully chose First Namespace")

        print("-----Scroll up-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -400")
        time.sleep(2)

        print("-----------------------try to put database server name -------------------------------")
        try:
            database_ServerName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.database_ServerName))
            if database_ServerName.is_displayed():
                database_ServerName.clear()
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
                EC.presence_of_element_located(data.initial_AdminPassword))
            if initial_AdminPassword.is_displayed():
                initial_AdminPassword.clear()
                initial_AdminPassword.send_keys(self.Password)
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
                EC.presence_of_element_located(data.confirm_Password))
            if confirm_Password.is_displayed():
                confirm_Password.send_keys(self.Password)
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

        print("-----------------------try to click 0n selectVersion_box-------------------------------")

        try:
            selectVersion_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.selectVersion_box))
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
                EC.presence_of_element_located(data.version_8_0_19))
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

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose Enable Web Client (phpMyAdmin)-------------------------------")

        try:
            enableWebClient = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.enableWebClient)))
            if enableWebClient.is_displayed():
                enableWebClient.click()
                time.sleep(2)
            else:
                file_name = ss_path + "enableWebClient" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose Enable Web Client (phpMyAdmin)")

        print("-----------------------try to click Next button-------------------------------")

        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
            if next_button.is_displayed():
                next_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "next_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on Next button")

        print("-----------------------try to click Next button again-------------------------------")
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
            if next_button.is_displayed():
                next_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "next_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on Next button")

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to click Confirm button-------------------------------")

        try:
            confirm_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.confirm_button))
            if confirm_button.is_displayed():
                confirm_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on Confirm button")

        print("-----------------------Message check-------------------------------")

        try:
            Database_CreatedMsg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(data.Database_CreatedMsg))
            if Database_CreatedMsg.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(Database_CreatedMsg.text, ['bold', 'underlined']))
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locator.Cancel_msg).click()
                time.sleep(7)
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(4)

        print("-----------------------Wait to database initialization------------------------------")
        try:
            WaitTo_Create = WebDriverWait(self.driver, 400).until(
                EC.visibility_of_element_located(data.WaitTo_Create))
            if WaitTo_Create.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(WaitTo_Create.text, ['bold', 'underlined']))
                time.sleep(3)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 600")
        time.sleep(3)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -600")
        time.sleep(3)

        print("-------------------- Try to Delete '" + self.ServerName + "' cache  ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.deleteCache(self, self.ServerName)
            self.driver.refresh()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)