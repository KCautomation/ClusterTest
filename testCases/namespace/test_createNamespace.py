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

        Namespace_Name = "test223"
        self.logger.info("*************** Test Create Namespace With Access Group: Company*****************")
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
        print("-------Try to click on CreateNew button from Header----------")
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
        print("----Try to click on Namespace button from frame-----")
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
        print("---Try to input Namespace Name---")
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

    def test_defaultOrganization(self, setup):

        Namespace_Name = "test221"
        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
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
        print("---Try to click on CreateNew button from Header---")
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
        print("---Try to input Namespace Name---")
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
        print("Scroll down")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Organization as access group---")
        try:
            Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Organization)))

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
                EC.presence_of_element_located((By.XPATH, Locator.Organization_searchBar)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Choose_Default)))
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
        print("---Try to update CPU by input Memory box---")
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
        print("---Try to update Volume by input box---")
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

        # # click create button for create
        # print("---Try to click on Create Button---")
        # try:
        #     Create_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Create_button_N)))
        #     Create_button.click()
        #     time.sleep(5)
        #     WebDriverWait(self.driver, 180).until(
        #         EC.visibility_of_element_located((By.XPATH, Locator.wait_toCreateNamespace)))
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # click create button for create
        # print("------------------check popup message------------------")
        # try:
        #     check_crateMessage = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.check_crateMessage)))
        #
        #     print('Shown a error message: ',
        #           simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
        #     time.sleep(6)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # print("******************Create Namespace Validation**********************")
        # try:
        #     actual = self.driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     print(actual)
        #     # if self.assertEqual(actual, accepted):
        #     #     print("Created Successfully")
        #     #     assert True
        #     # else:
        #     #     print("Created failed")
        #     #     assert False
        # except AssertionError as e:
        #     print(e)

    def test_useOrganization(self, setup):

        Namespace_Name = "test221"
        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
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
        print("---Try to click on CreateNew button from Header---")
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
        print("---Try to input Namespace Name---")
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
        print("Scroll down")
        time.sleep(2)

        # Choose access organization from Access Group
        print("---Try to Choose Organization as access group---")
        try:
            Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Organization)))

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
                EC.presence_of_element_located((By.XPATH, Locator.Organization_searchBar)))
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
            Choose_A_Organization = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.Choose_firstOrganization)))
            Choose_A_Organization.click()
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
        print("---Try to update CPU by input Memory box---")
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
        print("---Try to update Volume by input box---")
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

        # # click create button for create
        # print("---Try to click on Create Button---")
        # try:
        #     Create_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Create_button_N)))
        #     Create_button.click()
        #     time.sleep(5)
        #     WebDriverWait(self.driver, 180).until(
        #         EC.visibility_of_element_located((By.XPATH, Locator.wait_toCreateNamespace)))
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # click create button for create
        # print("------------------check popup message------------------")
        # try:
        #     check_crateMessage = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.check_crateMessage)))
        #
        #     print('Shown a error message: ',
        #           simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
        #     time.sleep(6)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # print("******************Create Namespace Validation**********************")
        # try:
        #     actual = self.driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     print(actual)
        #     # if self.assertEqual(actual, accepted):
        #     #     print("Created Successfully")
        #     #     assert True
        #     # else:
        #     #     print("Created failed")
        #     #     assert False
        # except AssertionError as e:
        #     print(e)
    def test_defaultTeam(self, setup):

        Namespace_Name = "test221"
        self.logger.info("*************** Test Create Namespace with Access Group: Team *****************")
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
            Team = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.Team)))

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
                EC.presence_of_element_located((By.XPATH, Locator.teamSearch_box)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Choose_TeamDefault)))
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

        # # click create button for create
        # print("---Try to click on Create Button---")
        # try:
        #     Create_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Create_button_N)))
        #     Create_button.click()
        #     time.sleep(5)
        #     WebDriverWait(self.driver, 180).until(
        #         EC.visibility_of_element_located((By.XPATH, Locator.wait_toCreateNamespace)))
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # click create button for create
        # print("------------------check popup message------------------")
        # try:
        #     check_crateMessage = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.check_crateMessage)))
        #
        #     print('Shown a error message: ',
        #           simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
        #     time.sleep(6)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # print("******************Create Namespace Validation**********************")
        # try:
        #     actual = self.driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     print(actual)
        #     # if self.assertEqual(actual, accepted):
        #     #     print("Created Successfully")
        #     #     assert True
        #     # else:
        #     #     print("Created failed")
        #     #     assert False
        # except AssertionError as e:
        #     print(e)

    def test_useTeam(self, setup):

        Namespace_Name = "test221"
        self.logger.info("*************** Test Create Namespace with Access Group: Team *****************")
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
            Team = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, Locator.Team)))

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
                EC.presence_of_element_located((By.XPATH, Locator.teamSearch_box)))
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
                EC.presence_of_element_located((By.XPATH, Locator.Choose_firstTeam)))
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

        # # click create button for create
        # print("---Try to click on Create Button---")
        # try:
        #     Create_button = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.Create_button_N)))
        #     Create_button.click()
        #     time.sleep(5)
        #     WebDriverWait(self.driver, 180).until(
        #         EC.visibility_of_element_located((By.XPATH, Locator.wait_toCreateNamespace)))
        #
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # # click create button for create
        # print("------------------check popup message------------------")
        # try:
        #     check_crateMessage = WebDriverWait(self.driver, 20).until(
        #         EC.presence_of_element_located((By.XPATH, Locator.check_crateMessage)))
        #
        #     print('Shown a error message: ',
        #           simple_colors.red(check_crateMessage.text, ['bold', 'underlined']))
        #     time.sleep(6)
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
        #
        # print("******************Create Namespace Validation**********************")
        # try:
        #     actual = self.driver.current_url
        #     accepted = "https://eks.alpha.klovercloud.io/namespace"
        #     print(actual)
        #     # if self.assertEqual(actual, accepted):
        #     #     print("Created Successfully")
        #     #     assert True
        #     # else:
        #     #     print("Created failed")
        #     #     assert False
        # except AssertionError as e:
        #     print(e)