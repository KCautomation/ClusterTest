import logging
import time
import pytest
import simple_colors
from colorama import Fore
from selenium.webdriver import ActionChains, Keys

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from Src.all_locators.Locators import Locator

from utilities.readProperties import ReadConfig
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache
from utilities import XLUtils

ss_path = "/DeleteCache/"


class TestCreateCache:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    CF = cacheFunctions()

    # path = "C:\\Users\\shabr\\PycharmProjects\\ClusterTest\\ClusterTest\\walton\\usersData.xlsx"
    path = "C:\\Users\\shabr\\PycharmProjects\\ClusterTest\\testCases\\Cache\\cache_data.xlsx"

    @pytest.mark.regression
    def test_teamNone(self, setup):
        self.logger.info("*************** Try to Test Create Cache *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)
        action = ActionChains(self.driver)

        self.driver.get("http://localhost:4200/manage/users")
        self.driver.implicitly_wait(5)

        # put Email
        try:
            Email_box = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Email_box)))
            print("Email_box is inputable")
            Email_box.send_keys("admin@klovercloud.com")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put email in Email_box')

        # put password
        try:
            Password_box = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Password_box)))
            print("Password_box is inputable")
            Password_box.send_keys("Abcd1234!")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put password in Password_box')

        # click on Toggle_Visibility_Button
        try:
            Toggle_Visibility_Button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Toggle_Visibility_Button)))
            print("Toggle_Visibility_Button is clickable")
            Toggle_Visibility_Button.click()
            time.sleep(1)
            Toggle_Visibility_Button.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')
        # Click on Sign In button

        try:
            Sign_In_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Sign_In_button)))
            print("Password_box is inputable")
            Sign_In_button.click()
            self.driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        self.driver.get("http://localhost:4200/manage/users")
        self.driver.implicitly_wait(5)
        time.sleep(3)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows i a Excel: ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', r, 1)
            # self.Exp = XLUtils.readData(self.path, 'Sheet1', r, 2)
            # username = "user0002"

            self.driver.find_element(By.XPATH,
                                     "//body/kc-root[1]/kc-layout[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/main[1]/kc-user-list[1]/kc-page-layout[1]/kc-page-layout-content[1]/div[1]/div[1]/button[1]/span[1]").click()
            time.sleep(4)

            firstName = self.driver.find_element(By.XPATH,
                                                 "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-user-form[1]/div[1]/form[1]/mat-dialog-content[1]/mat-form-field[1]/div[1]/div[1]/div[3]/input[1]")
            firstName.send_keys(self.username)
            # time.sleep(1)

            email = self.driver.find_element(By.XPATH,
                                             "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-user-form[1]/div[1]/form[1]/mat-dialog-content[1]/mat-form-field[3]/div[1]/div[1]/div[3]/input[1]")
            email.send_keys("" + self.username + "@gmail.com")
            # time.sleep(1)

            autho = self.driver.find_element(By.XPATH,
                                             "//body/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-user-form[1]/div[1]/form[1]/mat-dialog-content[1]/mat-form-field[5]/div[1]/div[1]/div[3]/mat-select[1]/div[1]/div[2]/div[1]")

            autho.click()

            dev = self.driver.find_element(By.XPATH, "//span[contains(text(),'DEV')]")
            dev.click()
            time.sleep(1)
            action.send_keys(Keys.TAB)
            action.perform()
            time.sleep(2)

            click_button = self.driver.find_element(By.XPATH,
                                                    "/html[1]/body[1]/div[3]/div[2]/div[1]/mat-dialog-container[1]/kc-user-form[1]/div[1]/form[1]/mat-dialog-actions[1]/button[2]/span[1]/span[1]")
            click_button.click()
            self.driver.implicitly_wait(5)
            time.sleep(5)
