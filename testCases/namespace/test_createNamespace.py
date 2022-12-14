import logging
import time

import allure
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
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.namespace.namespace import NamespaceFunctions
from pageObjects.Namespace.pomCreateNamespace import CreateNamespace

ss_path = "/Database/"


@allure.severity(allure.severity_level.CRITICAL)
class TestCreateNamespace:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    namespace = NamespaceFunctions()
    DF = DatabaseFunctions()
    ServerName = "testSql0233"
    Password = "Qwer1235!!"

    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_defaultly(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test334"
        self.logger.info("*************** Test Create Namespace With Access Group: Company*****************")
        self.driver = setup
        ss = SS(self.driver)
        nam = CreateNamespace(self.driver)

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
        print("-------Try to click on CreateNew button from Header----------")
        try:
            CreateNew_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.CreateNew_H))
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
        print("----Try to click on Namespace button from frame-----")
        try:
            NamespaceButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceButton))
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
        print("---Try to input Namespace Name---")
        try:
            NamespaceName_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceName_bar))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click create button for create
        print("---Try to click on Create Button---")
        try:
            Create_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Create_button_N))
            Create_button.click()
            time.sleep(5)
            WebDriverWait(self.driver, 180).until(
                EC.visibility_of_element_located(nam.wait_toCreateNamespace))

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # check check_crateMessage
        print("------------------check popup message------------------")
        try:
            check_crateMessage = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(nam.check_crateMessage))

            print('Shown a error message: ',
                  simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
            time.sleep(6)
            pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        print("******************Create Namespace Validation**********************")
        try:
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '"+Namespace_Name+"']")))
            if Namespace.is_displayed():
                Namespace.click()
                print("Welcome to '" + Namespace_Name + "' namespace & page title is :", self.driver.title)
                time.sleep(7)
                pass
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
                print("Namespace Created failed")
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
            self.driver.refresh()
            time.sleep(3)
            Namespace_settings = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(nam.Namespace_settings))
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
                EC.element_to_be_clickable(nam.deleteButton_namespace))
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
                EC.element_to_be_clickable(nam.Application_namebox_D))
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
        # self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        # print("Scroll down")
        # time.sleep(3)

        # input application name
        try:
            Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(nam.Delete_permanently_button))
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
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '"+Namespace_Name+"']")))
            if Namespace.is_displayed():
                print("Namespace '" + Namespace_Name + "' is found")
                allure.attach(self.driver.get_screenshot_as_png(), name="Delete_Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
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

    def test_defaultOrganization(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test334"
        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        nam = CreateNamespace(self.driver)
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
        print("---Try to click on CreateNew button from Header---")
        try:
            CreateNew_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.CreateNew_H))
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
        print("---Try to click on Namespace button from frame---")
        try:
            NamespaceButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceButton))
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
        print("---Try to input Namespace Name---")
        try:
            NamespaceName_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceName_bar))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Organization as access group---")
        try:
            Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Organization))

            Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("---Try to click search box---")
        try:
            Organization_searchBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Organization_searchBar))
            Organization_searchBar.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Organization selection
        print("---Try to choose Organization---")
        try:
            Choose_Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Choose_Default))
            Choose_Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("---Try to update CPU by input CPU box---")
        try:
            CPU_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.CPU_bar))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("---Try to update CPU by input Memory box---")
        try:
            Memory_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Memory_box))

            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("---Try to update Volume by input box---")
        try:
            Volume_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Volume_box))

            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("---Try to update Bandwidth by input box--")
        try:
            Bandwidth_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Bandwidth_box))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("---Try to click on Create Button---")
        try:
            Create_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Create_button_N))
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
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '" + Namespace_Name + "']")))
            if Namespace.is_displayed():
                Namespace.click()
                time.sleep(5)
                print("Welcome to '" + Namespace_Name + "' namespace & page title is :", self.driver.title)
                time.sleep(7)
                pass

            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Create_Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
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
            self.driver.refresh()
            time.sleep(3)
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
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '"+Namespace_Name+"']")))
            if Namespace.is_displayed():
                print("Namespace '" + Namespace_Name + "' is found")
                allure.attach(self.driver.get_screenshot_as_png(), name="Delete_Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
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

    def test_useOrganization(self, setup):
        # pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test335"
        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        nam = CreateNamespace(self.driver)
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
        print("---Try to click on CreateNew button from Header---")
        try:
            CreateNew_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.CreateNew_H))
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
        print("---Try to click on Namespace button from frame---")
        try:
            NamespaceButton = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceButton))
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
        print("---Try to input Namespace Name---")
        try:
            NamespaceName_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.NamespaceName_bar))
            NamespaceName_box.send_keys(Namespace_Name)
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("Scroll down")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Organization as access group---")
        try:
            Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Organization))

            Organization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("---Try to click search box---")
        try:
            Organization_searchBar = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Organization_searchBar))
            Organization_searchBar.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Organization selection
        print("---Try to choose Organization---")
        try:
            Choose_firstOrganization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Choose_firstOrganization))
            Choose_firstOrganization.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("---Try to update CPU by input CPU box---")
        try:
            CPU_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.CPU_bar))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("---Try to update CPU by input Memory box---")
        try:
            Memory_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Memory_box))

            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("---Try to update Volume by input box---")
        try:
            Volume_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Volume_box))

            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("---Try to update Bandwidth by input box--")
        try:
            Bandwidth_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Bandwidth_box))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("---Try to click on Create Button---")
        try:
            Create_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.Create_button_N))
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
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '"+Namespace_Name+"']")))
            if Namespace.is_displayed():
                Namespace.click()
                time.sleep(5)
                print("Welcome to '" + Namespace_Name + "' namespace & page title is :", self.driver.title)
                time.sleep(7)
                pass

            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Create_Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
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
            self.driver.refresh()
            time.sleep(3)
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
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '"+Namespace_Name+"']")))
            if Namespace.is_displayed():
                print("Namespace '" + Namespace_Name + "' is found")
                allure.attach(self.driver.get_screenshot_as_png(), name="Delete_Namespace_Validation",
                              attachment_type=AttachmentType.PNG)
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

    def test_useDefaultTeam(self, setup):
        pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test302"
        self.logger.info("*************** Test Create Namespace with Access Group: Team *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        nam = CreateNamespace(self.driver)

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
        print("---Try to click on Namespace button from frame---")
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
        print("--Try to input Namespace Name--")
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

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("---Scroll down---")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Team as a access group---")
        try:
            Team = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(nam.Team))

            Team.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("---Try to click search box---")
        try:
            teamSearch_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.teamSearch_box))
            teamSearch_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Team selection
        print("---Try to choose Team---")
        try:
            teamDefault = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.teamDefault))
            teamDefault.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("---Try to update CPU by input CPU box---")
        try:
            CPU_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.CPU_bar)))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("Try to update CPU by input Memory box")
        try:
            Memory_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Memory_box)))

            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("Try to update Volume by input box")
        try:
            Volume_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Volume_box)))

            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("---Try to update Bandwidth by input box--")
        try:
            Bandwidth_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Bandwidth_box)))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("---Try to click on Create Button---")
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

    def test_useTeam(self, setup):
        pytest.skip("Skipping test...later I will implement...")
        Namespace_Name = "test303"
        self.logger.info("*************** Test Create Namespace with Access Group: Team *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        nam = CreateNamespace(self.driver)

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
        print("---Try to click on Namespace button from frame---")
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
        print("--Try to input Namespace Name--")
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

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 550")
        print("---Scroll down---")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Team as a access group---")
        try:
            Team = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(nam.Team))

            Team.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # click search box and choose organization
        print("---Try to click search box---")
        try:
            teamSearch_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.teamSearch_box))
            teamSearch_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Team selection
        print("---Try to choose Team---")
        try:
            first_Team = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(nam.first_Team))
            first_Team.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 730")
        print("Scroll down")
        time.sleep(2)

        # CPU selection
        print("---Try to update CPU by input CPU box---")
        try:
            CPU_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.CPU_bar)))
            CPU_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Memory Selection
        print("Try to update CPU by input Memory box")
        try:
            Memory_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Memory_box)))

            Memory_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Persistent Volume selection
        print("Try to update Volume by input box")
        try:
            Volume_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Volume_box)))

            Volume_box.send_keys(0)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Bandwidth selection
        print("---Try to update Bandwidth by input box--")
        try:
            Bandwidth_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Bandwidth_box)))
            Bandwidth_box.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Scroll
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -730")
        print("Scroll up")
        time.sleep(2)

        # click create button for create
        print("---Try to click on Create Button---")
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
