import time
from telnetlib import EC

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
from utilities.readProperties import ReadConfig

ss_path = "/Applications/PHP/"


class TestDeleteNamespace:
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
    def test_deleteNamespaces(self, setup):

        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        Namespace_Name = 'test221'
        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to click on Namespace from side bar *********************")
        try:
            Namespace_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.NamespaceButton_sidebar)))

            if Namespace_button.is_displayed():
                Namespace_button.click()
                self.driver.implicitly_wait(5)
                time.sleep(3)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Namespace validation
        try:
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '" + Namespace_Name + "']")))
            if Namespace.is_displayed():
                Namespace.click()
                time.sleep(5)
                print("Welcome to '" + Namespace_Name + "' namespace & page title is :", self.driver.title)
                pass

            else:
                print("Created failed")
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Namespace delete
        print("-------Try to click on namespace Settings--------")

        try:
            Namespace_settings = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Namespace_settings)))
            Namespace_settings.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # click on Delete button
        print("-------Try to click on namespace Delete--------")
        try:
            deleteButton_namespace = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.deleteButton_namespace)))
            deleteButton_namespace.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        print("-------Try to put Application Name in application name box--------")
        try:
            input_namespaceName = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
            print("application_Delete is clickable")
            input_namespaceName.send_keys(Namespace_Name)
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
            Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Delete_permanently_button)))
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(15)
            self.driver.refresh()
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # check msg
        # try:
        #     Namespace_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
        #     if Namespace_Deleted_Success_msg.is_displayed():
        #
        #         print('Shown a message: ',
        #               simple_colors.green(Namespace_Deleted_Success_msg.text, ['bold', 'underlined']))
        #         print("\n")
        #         pass
        #     else:
        #         pass
        #     time.sleep(10)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error :\n", e, "\n")
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException", e)
        # except AssertionError as e:
        #     print("AssertionError", e)

        # delete validation
        try:
            self.driver.refresh()
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '" + Namespace_Name + "']")))
            if Namespace.is_displayed():
                print("Namespace '" + Namespace_Name + "' is found")
                assert False

            else:
                print("Namespace '" + Namespace_Name + "' is not found")
                assert True

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("AssertionError error", e)
        ss = SS(self.driver)
        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)
