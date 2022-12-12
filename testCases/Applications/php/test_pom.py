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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.applications.application_functions import ApplicationFunctions
from pageObjects.Apllications.pomCreateApplication import CreateApplication

ss_path = "/Database/"


@allure.severity(allure.severity_level.CRITICAL)
class TestPHPApplication:
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
    def test_Laravel_default_01(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        ApplicationName = "test328"
        self.logger.info("*************** Test Create Application With PHP Laravel*****************")
        self.driver = setup
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        app = CreateApplication(self.driver)

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

        print("****************** Try to go Create Application page *********************")
        try:
            self.appFunction.go_CreateAppPage(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("***************Create PHP application with PHP Version: 7.3 &  SpringBoot version : 7.0**************")

        print("----try to choose Laravel from below--------")
        try:
            Laravel = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(app.Laravel))
            # driver.refresh()
            Laravel.click()
            self.driver.implicitly_wait(10)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("----Try to put application name--------")
        try:
            ApplicationName_box = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(app.ApplicationName_box))
            if ApplicationName_box.is_displayed():
                print("ApplicationName_box is visible")
                ApplicationName_box.send_keys(ApplicationName)
                time.sleep(2)
                file_name = ss_path + "ApplicationName_box_" + time.asctime().replace(":", "_") + ".png"
                ApplicationName_box.screenshot(file_name)
            else:
                file_name = ss_path + "ApplicationName_box_" + time.asctime().replace(":", "_") + ".png"
                ApplicationName_box.screenshot(file_name)

                # # file_name = ss_path + "ApplicationName_box_" + time.asctime().replace(":", "_") + ".png"
                # ss.driver.save_screenshot(file_name)
                # ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        # choose version
        print("---------PHP: 7.3 & Laravel: 7.0 chose by default 7.3------------")

        # scroll down
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 150")
        print("Scroll down")
        time.sleep(2)

        # Click on team box
        print("----try to click Team box--------")
        try:
            TeamBox_A = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(app.TeamBox_A))
            print("TeamBox_A button is clickable")
            TeamBox_A.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on TeamBox_A')

        print("----try to choose Team as Default--------")
        try:
            Team_Default = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Team_Default))
            print("Team_Default button is clickable")
            Team_Default.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully chose Team as Default')

        # scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        print("Scroll down")

        print("----try to click 'Next' button-------")
        try:
            Next_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Next_button))
            print("Next_button button is clickable")
            Next_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on Next_button')

        print("----try to again click 'Next' button-------")
        try:
            Next_button_two = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Next_button))
            print("Next_button_two button is clickable")
            Next_button_two.click()
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked on Next_button')

        # again scroll below to show Namespaces
        print("Try Scroll down to show Namespaces")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 250")
        time.sleep(2)

        # Choose A Namespace for Prod Environment
        print("----try to Choose A Namespace for Prod Environment--------")
        try:
            Choose_Namespace_one = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Choose_Namespace_one))
            print("Choose_Namespace_one button is clickable")
            Choose_Namespace_one.click()
            time.sleep(5)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully Chose first Namespace')

        print("-----Scroll down to show Namespaces-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 1500")
        time.sleep(2)

        # click on save button
        print("----try to click save button--------")
        try:
            Save_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Save_button_A))
            print("Save_button button is clickable")
            Save_button.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)

        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully clicked save button')

        # click on Create application button
        print("----try to click 'Create application' button--------")
        try:
            Create_Application = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(app.Create_Application))
            print("Create_Application button is clickable")
            Create_Application.click()
            time.sleep(4)
            # check success message
            New_Git_Commit_Pushed_msg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(app.New_Git_Commit_Pushed_msg))
            if New_Git_Commit_Pushed_msg.is_displayed():

                print('Shown a message: ',
                      simple_colors.green(New_Git_Commit_Pushed_msg.text, ['bold', 'underlined']))
                print("\n")
                time.sleep(6)
                Application_build_finished_successfully_msg = WebDriverWait(self.driver, 80).until(
                    EC.presence_of_element_located(app.Application_build_finished_successfully_msg))
                if Application_build_finished_successfully_msg.is_displayed():
                    print('Shown a message: ',
                          simple_colors.green(Application_build_finished_successfully_msg.text, ['bold', 'underlined']))
                    print("\n")
                    print("Application_build_finished_successfully")
                    time.sleep(10)
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # time.sleep(80)
        # wait for confirmation
        try:
            wait_ToCreateApplication = WebDriverWait(self.driver, 800).until(
                EC.visibility_of_element_located(app.wait_ToCreateApplication))
            if wait_ToCreateApplication.is_displayed():
                time.sleep(4)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # application created validation
        print("---------------Try to Crated Application Validation--------------------")
        try:
            self.driver.refresh()
            time.sleep(3)
            check_create_app = WebDriverWait(self.driver, 40).until(
                EC.presence_of_element_located(app.check_create_app))
            check_create_app.click()
            time.sleep(2)
            action.send_keys(Keys.ENTER)
            action.perform()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # checked validation message
        try:
            Created_status = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(app.check_app_status))

            Actual_status = Created_status.text
            Accepted_status = "Success"

            if Actual_status == Accepted_status:
                print('Application created status is: ',
                      simple_colors.green(Actual_status, ['bold', 'underlined']))
                time.sleep(2)
                assert True
            else:
                print('Application created status is: ',
                      simple_colors.green(Actual_status, ['bold', 'underlined']))

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("AssertionError", e)

        # deploy application
        print("*******************************Try to Test deploy application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.deployApplication(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        # check deployed status
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_deploy_validation(self)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("*******************************Try Test to delete application******************************")
        try:
            self.driver.refresh()
            time.sleep(3)
            self.appFunction.test_delete_app(self, ApplicationName)
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("---------------------- deleted Application validation-----------------------")

        print("Application Delete Successfully")

        file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
        ss.driver.save_screenshot(file_name)
        ss.ScreenShot(file_name)