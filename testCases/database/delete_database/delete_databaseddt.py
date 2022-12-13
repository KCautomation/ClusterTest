import logging
import time
import pytest
import simple_colors

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.functions.database.databaseFunctions import DatabaseFunctions
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from Src.application_delete.delete_app import test_delete_app

from utilities.readProperties import ReadConfig
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache

ss_path = "/Database/"


class TestDeleteDatabase:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()
    ServerName = "test-sql-221"
    Password = "Qwer1235!!"

    path = "C:\\Users\\shabr\\PycharmProjects\\ClusterTest\\testCases\\database\\delete_database\\deleteDatabase.xlsx"

    @pytest.mark.regression
    def test_DeleteDatabase(self, setup):

        self.logger.info("*************** Test_Create Database *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)

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
            database_list = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.database_list)))
            print("Applications button is clickable")
            database_list.click()
            print("Welcome to database list")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows i a Excel: ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.ServerName = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Exp = XLUtils.readData(self.path, 'Sheet1', r, 2)

            # scroll down
            self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
            print("Scroll down")
            time.sleep(3)

            # click on an application
            try:
                database_name = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='" + self.ServerName + "']")))
                if database_name.is_displayed:
                    print(self.ServerName, "Application is present in the list")
                    database_name.click()
                    print("successfully clicked on :", self.ServerName)
                    time.sleep(10)
                else:
                    return exit()

            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)
            # click on settings
            print("******************************* Test Try to delete application******************************")
            try:
                database_Settings = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, Locator.database_Settings)))
                print("application_Settings is clickable")
                database_Settings.click()
                print("Welcome database Settings ")
                time.sleep(5)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)

            # click on Delete button
            try:
                database_Delete = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, Locator.database_Delete)))
                print("application_Delete is clickable")
                database_Delete.click()
                print("successfully clicked application_Delete ")
                time.sleep(5)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)

            # input application name
            try:
                database_nameBox = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, Locator.database_nameBox)))
                print("application_Delete is clickable")
                database_nameBox.send_keys(self.ServerName)
                print("successfully inputted Application_name ")
                time.sleep(5)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)

            # scroll down
            self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
            print("Scroll down")
            time.sleep(3)

            # input application name
            try:
                deletePermanently = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, Locator.deletePermanently)))
                print("application_Delete is clickable")
                deletePermanently.click()
                print("successfully clicked on Delete_permanently_button ")
                time.sleep(2)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)
            # time.sleep(30)

            # check msg
            try:
                Cache_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
                if Cache_Deleted_Success_msg.is_displayed():
                    XLUtils.writeData(self.path, "Sheet1", r, 2, "Test Passed")

                    print('Shown a message: ',
                          simple_colors.green(Cache_Deleted_Success_msg.text, ['bold', 'underlined']))
                    print("\n")
                    pass
                time.sleep(35)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)
            time.sleep(30)
            ss = SS(self.driver)
            file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
            ss.driver.save_screenshot(file_name)
            ss.ScreenShot(file_name)
