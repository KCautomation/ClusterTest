import logging
import time
import pytest
import simple_colors

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.functions.database.createDatabase import DatabaseFunctions
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from Src.application_delete.delete_app import test_delete_app

from utilities.readProperties import ReadConfig
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache
from pageObjects.Apllications.pomDeleteAppication import DeleteApplication

ss_path = "/DeleteCache/"


class TestCreateCache:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    CF = cacheFunctions()

    @pytest.mark.regression
    def test_teamNone(self, setup):

        self.logger.info("*************** Test_Create Cache *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        del_pom = DeleteApplication(self.driver)

        ServerName = "test-25"
        Password = "Qwer1235!!"

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go cache list by click on Caches *********************")

        print("****************** Go to Cache list *********************")
        try:
            Cache_list = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_S))
            print("Applications button is clickable")
            Cache_list.click()
            print("Welcome to applications list")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        # self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        # print("Scroll down")
        # time.sleep(3)

        # click on an application
        try:
            Cache_name = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='"+ServerName+"']")))
            if Cache_name.is_displayed:
                print(ServerName, "Application is present in the list")
                Cache_name.click()
                print("successfully clicked on :", ServerName)
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
            Cache_Settings = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_Settings))
            print("application_Settings is clickable")
            Cache_Settings.click()
            print("Welcome application_Settings ")
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

        # click on Delete button
        try:
            Cache_Delete = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_Delete))
            print("Cache_Delete is clickable")
            Cache_Delete.click()
            print("successfully clicked Cache_Delete ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        try:
            Cache_namebox_D = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_namebox_D))
            print("Cache_namebox_D is clickable")
            Cache_namebox_D.send_keys(ServerName)
            print("successfully inputted Cache_namebox_D ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        # self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        # print("Scroll down")
        # time.sleep(3)

        # delete
        try:
            Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(del_pom.Delete_permanently_button))
            print("application_Delete is clickable")
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # check msg
        try:
            Cache_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(cache.Cache_Deleted_Success_msg))
            if Cache_Deleted_Success_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(Cache_Deleted_Success_msg.text, ['bold', 'underlined']))
                print("\n")
                assert True
                time.sleep(10)

            else:
                assert False
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

