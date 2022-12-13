import logging
import time
import pytest
import simple_colors
from colorama import Fore

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from utilities import XLUtils
from utilities.readProperties import ReadConfig
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache

ss_path = "/DeleteCache/"


class TestCreateCache:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    CF = cacheFunctions()

    path = "C:\\Users\\shabr\\PycharmProjects\\ClusterTest\\testCases\\Cache\\cache_data.xlsx"

    @pytest.mark.regression
    def test_teamNone(self, setup):

        self.logger.info("*************** Try to Test Create Cache *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("----------------Try to Go Cache list ---------------------")
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

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows i a Excel: ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.ServerName = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.Exp = XLUtils.readData(self.path, 'Sheet1', r, 2)
            # self.Exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            # click on an application
            try:
                Cache_name = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='" + self.ServerName + "']")))
                if Cache_name.is_displayed:
                    print(self.ServerName, "Application is present in the list")
                    Cache_name.click()
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
            print("******************************* Test Try to delete cache******************************")

            print("----------------------try to click on Settings button--------------------")
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
            self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 50")
            print("Scroll down")
            time.sleep(3)

            print("----------------------try to click on Delete button from below--------------------")
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

            print("----------------------try to input Cache name--------------------")
            try:
                Cache_namebox_D = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(cache.Cache_namebox_D))
                print("Cache_namebox_D is clickable")
                Cache_namebox_D.send_keys(self.ServerName)
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

            print("----------------------click on  Delete permanently button--------------------")
            try:
                Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(cache.Delete_permanently_button))
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
            print("----------------------check Message--------------------")
            try:
                Cache_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
                    EC.presence_of_element_located(cache.Cache_Deleted_Success_msg))
                if Cache_Deleted_Success_msg.is_displayed():
                    print('Shown a message: ',
                          simple_colors.green(Cache_Deleted_Success_msg.text, ['bold', 'underlined']))
                    print("\n")
                    time.sleep(45)
                    pass
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)
            except AssertionError as e:
                print("AssertionError", e)

            print("----------------------'" + self.ServerName + "' deleted validation from cache list--------------------")
            try:
                self.driver.refresh()
                time.sleep(4)

                cache_name = self.driver.find_element(By.XPATH, "//span[normalize-space()='" + self.ServerName + "']")
                if cache_name.is_Displayed():
                    XLUtils.writeData(self.path, "Sheet1", r, 2, "Test Passed")
                    print(self.ServerName, "is still present in the list")
                    assert False
                else:
                    XLUtils.writeData(self.path, "Sheet1", r, 2, "Test Passed")
                    print("successfully clicked on :", self.ServerName)
                    print(Fore.RED + self.ServerName, "cache is not available is the list, that means deleted successfully")
                    assert True

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
