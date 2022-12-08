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
    def test_defaultOrganization(self, setup):

        self.logger.info("*************** Test Create Namespace with Access Group: organization *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        Namespace_Name = 'test221'

        self.driver.get(self.baseURL)
        Accept_title = "KloverCloud | Dashboard"
        Actual_title = self.driver.title

        if Accept_title == Actual_title:
            print("Already Logged In, Page Title is:", self.driver.title)
            pass
        else:
            print("****************** Try to Test Cluster Login *********************")
            try:
                self.login.test_cluster_login(self)
            except NoSuchElementException as e:
                print("NoSuchElementException error :\n", e, "\n")
            except TimeoutException as e:
                print("TimeoutException error", e)
            except InvalidSessionIdException as e:
                print("InvalidSessionIdException", e)

