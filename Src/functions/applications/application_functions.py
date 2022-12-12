import time

import allure
import pytest

import simple_colors
from allure_commons.types import AttachmentType
from colorama import Fore
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException, ElementClickInterceptedException
from urllib.request import urlopen
from urllib.error import *

from pageObjects.Apllications.pomCreateApplication import CreateApplication
from utilities.readProperties import ReadConfig
from Src.screenShot.screenShot import SS

ss_path = "/Login/"


class ApplicationFunctions:

    @staticmethod
    def deployApplication(self):

        print("******************************* Test Try to deploy application******************************")
        # click on deploy
        try:
            To_deploy = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located((By.XPATH, Locator.To_deploy)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Deploy_button)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Okay_button)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_msg)))
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
                EC.presence_of_element_located((By.XPATH, Locator.deployment_failed)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Deployment_Pending_time_msg)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Application_Deployed)))
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
            deployed_validation = WebDriverWait(self.driver, 800).until(
                EC.presence_of_element_located((By.XPATH, Locator.deployed_validation)))
            if deployed_validation.is_displayed():
                time.sleep(2)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        time.sleep(3)

    @staticmethod
    def test_deploy_validation(self):
        # pytest.skip("Skipping test...later I will implement...")
        action = ActionChains(self.driver)

        print("---------------Deployed Validation--------------------")
        try:
            time.sleep(2)
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

    @staticmethod
    def test_delete_app(self, ApplicationName):
        # pytest.skip("Skipping test...later I will implement...")

        print("-------Try to click on application Settings--------")

        try:
            application_Settings = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Settings)))
            print("application_Settings is clickable")
            application_Settings.click()
            print("Welcome application_Settings ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # click on Delete button
        print("-------Try to click on application Delete--------")
        try:
            application_Delete = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.application_Delete)))
            print("application_Delete is clickable")
            application_Delete.click()
            print("successfully clicked application_Delete ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        print("-------Try to put Application Name in application name box--------")
        try:
            Application_namebox_D = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
            print("application_Delete is clickable")
            Application_namebox_D.send_keys(ApplicationName)
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
            Application_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
            if Application_Deleted_Success_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(Application_Deleted_Success_msg.text, ['bold', 'underlined']))
                print("\n")
                pass
            else:
                pass
            time.sleep(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)
        ss = SS(self.driver)
        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)

    @staticmethod
    def go_CreateAppPage(self):
        print(Fore.CYAN + "-----------------------From Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.CreateNew_H)))
            print("CreateNew_H button is clickable")
            CreateNew_H.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            NewApplication_H = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.NewApplication_H)))
            print("NewApplication_H button is clickable")
            NewApplication_H.click()
            time.sleep(5)
            self.driver.implicitly_wait(20)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on NewApplication_H')
        print(
            Fore.CYAN + "-----------------------Welcome Create Application Page----------------------------------------")


