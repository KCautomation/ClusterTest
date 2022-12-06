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

ss_path = "/Database/"


class TestCreateNamespace:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()
    ServerName = "testSql0233"
    Password = "Qwer1235!!"

    @pytest.mark.regression
    def test_CreateNamespace(self, setup):

        Namespace_Name = "test221"
        self.logger.info("*************** Test Create Namespace *****************")
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

        print("****************** Try to go create namespace page *********************")

        # click on create button from header
        print("Try to click on CreateNew button from Header")
        try:
            CreateNew_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.CreateNew_H)))
            CreateNew_button.click()
            self.driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click namespace
        print("Try to click on Namespace button from frame")
        try:
            NamespaceButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Locator.NamespaceButton)))
            NamespaceButton.click()
            self.driver.implicitly_wait(10)
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # input Namespace name
        print("Try to input Namespace Name")
        try:
            NamespaceName_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Locator.NamespaceName_bar)))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click create button for create
        print("Try to click on Create Button")
        try:
            Create_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Create_button_N)))
            Create_button.click()
            time.sleep(5)
            WebDriverWait(self.driver, 180).until(
                EC.visibility_of_element_located((By.XPATH, Locator.wait_toCreateNamespace)))

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click create button for create
        print("------------------check popup message------------------")
        try:
            check_crateMessage = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.check_crateMessage)))

            print('Shown a error message: ',
                  simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
            time.sleep(6)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("******************Create Namespace Validation**********************")
        try:
            actual = self.driver.current_url
            accepted = "https://eks.alpha.klovercloud.io/namespace"
            print(actual)
            # if self.assertEqual(actual, accepted):
            #     print("Created Successfully")
            #     assert True
            # else:
            #     print("Created failed")
            #     assert False
        except AssertionError as e:
            print(e)
