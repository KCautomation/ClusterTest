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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    ElementClickInterceptedException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.applications.application_functions import ApplicationFunctions
from pageObjects.Apllications.pomCreateApplication import CreateApplication
from pageObjects.Apllications.pomDeployApp import DeployApplications

ss_path = "/DeployApplication/"


@allure.severity(allure.severity_level.CRITICAL)
class TestDeploy:
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
    def test_deployApplication(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        ApplicationName = "test-327"
        self.logger.info("*************** Test deploy Application*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        dep = DeployApplications(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e,
                  "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Go to Application list *********************")
        try:
            Applications_list = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(dep.Applications))
            print("Applications button is clickable")
            Applications_list.click()
            self.driver.implicitly_wait(30)
            print("Welcome to applications list")
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

        # click on an application
        try:
            Application_name = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'"+ApplicationName+"')]")))
            if Application_name.is_displayed:
                print(ApplicationName, "Application is present in the list")
                Application_name.click()
                self.driver.implicitly_wait(25)
                print("successfully clicked on :", ApplicationName)
                time.sleep(7)
            else:
                return exit()

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(dep.To_deploy))
            print("deploy element is visible")
            # To_deploy.click()
            To_deploy.click()
            time.sleep(2)
            print("successfully clicked on deploy")
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except ElementClickInterceptedException as e:
            print("ElementClickInterceptedException", e)

        # click on deploy button
        try:
            Deploy_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(dep.Deploy_button))
            print("deploy button is hided")
            Deploy_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click on okay button
        try:
            Okay_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(dep.Okay_button))
            print("deploy button is hided")
            Okay_button.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # check message
        try:
            Deployment_Pending_msg = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(dep.Deployment_Pending_time_msg))
            if Deployment_Pending_msg.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Deployment_Pending_msg.text, ['bold', 'underlined']))
                pass
            else:
                pass
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        try:
            deployment_failed = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(dep.deployment_failed))
            if deployment_failed.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(deployment_failed.text, ['bold', 'underlined']))
                pass
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        try:
            Deployment_Pending_time_msg = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(dep.Deployment_Pending_time_msg))
            if Deployment_Pending_time_msg.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Deployment_Pending_time_msg.text, ['bold', 'underlined']))
                time.sleep(4)
                pass
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        try:
            Application_Deployed = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(dep.Application_Deployed))
            if Application_Deployed.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Application_Deployed.text, ['bold', 'underlined']))
                pass
            else:
                time.sleep(2)
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        try:
            wait_ToDeploy = WebDriverWait(self.driver, 800).until(
                EC.presence_of_element_located(dep.wait_ToDeploy))
            if wait_ToDeploy.is_displayed():
                time.sleep(2)
                self.driver.refresh()
                time.sleep(2)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("---------------Check Deployed Validation--------------------")
        try:
            to_check_deploy = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.to_check_deploy)))
            print("Deploy_button is located")
            to_check_deploy.click()
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(3)
            pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        # validation
        try:
            Deployed_status = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, Locator.Deployed_status)))

            Accepted_status = "Success"
            Actual_status = Deployed_status.text
            if Accepted_status == Actual_status:
                print('Deployed status is: ',
                      simple_colors.green(Actual_status, ['bold', 'underlined']))
                assert True
            else:
                print('Deployed status is: ',
                      simple_colors.green(Actual_status, ['bold', 'underlined']))
                time.sleep(4)
                assert False

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("InvalidSessionIdException error", e)

        file_name = ss_path + "deployed_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

