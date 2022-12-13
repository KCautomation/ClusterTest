import logging
import time
import pytest
import simple_colors

import raf_practice.logs.customolog.custom_logger as cl
from Src.functions.cache.cacheFunction import cacheFunctions
from Src.login_function.login import login
from Src.functions.database.databaseFunctions import DatabaseFunctions
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from pageObjects.Database.pomDatabase import Database
from utilities.readProperties import ReadConfig
from pageObjects.Cache.pomCache import CreateCache
from Src.functions.database.createDatabase import Mysql

ss_path = "/Database/CreateDatabase/"


class TestCreateDatabase:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    DF = DatabaseFunctions()
    CF = cacheFunctions()
    My = Mysql()

    @pytest.mark.regression
    def test_MySQLDatabase(self, setup):

        self.logger.info("*************** Test_Create Database *****************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        data = Database(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go create database page *********************")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.DF.go_createDatabasePage(self)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go create MySql database *********************")
        Team = data.defaultTeam_database
        ServerName = "testMyql0133"
        Password = "Qwer1234!!"
        MySql_Version = data.version_8_0_19

        try:
            self.driver.refresh()
            time.sleep(3)
            self.My.mySql(self, Team, ServerName, Password, MySql_Version)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("-------------------- Try to Delete '" + ServerName + "' cache  ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.deleteCache(self, ServerName)
            self.driver.refresh()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)