import logging
import time

import allure
import pytest
import simple_colors
from colorama import Fore
from selenium.webdriver import Keys, ActionChains

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
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
from pageObjects.Apllications.pomDeleteAppication import DeleteApplication
from Src.functions.applications.deleteApp import DeleteApp

ss_path = "/DeleteApplication/"


@allure.severity(allure.severity_level.CRITICAL)
class TestDeleteApplication:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()

    appFunction = ApplicationFunctions()
    ServerName = "testSql0233"
    Password = "Qwer1235!!"

    delete = DeleteApp()

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_applications(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        ApplicationName = "test-352"
        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        del_pom = DeleteApplication(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Applications list *********************")
        try:
            Applications_list = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(del_pom.Applications))
            print("Applications button is clickable")
            Applications_list.click()
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
            Application_name = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'" + ApplicationName + "')]")))
            if Application_name.is_displayed:
                print(ApplicationName, "Application is present in the list")
                Application_name.click()
                print("successfully clicked on :", ApplicationName)
                time.sleep(10)
            else:
                print("" + ApplicationName + " is not avalavle in the list")
                file_name = ss_path + "app_is_" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
                # self.driver.close()
                self.driver.quit()

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.delete.delete_app(self, ApplicationName)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

