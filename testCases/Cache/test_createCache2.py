import logging
import time
import pytest
import simple_colors

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException
from Src.application_delete.delete_app import test_delete_app

from utilities.readProperties import ReadConfig
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache
from Src.functions.cache.create_Cache import CreateCaches

ss_path = "/Caches/create/"


class TestCreateCache:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    login = login()
    CF = cacheFunctions()
    CC = CreateCaches()

    @pytest.mark.regression
    def test_TC001(self, setup):

        print("****************** Try to go create Cache based on Team: None & Version: 5.0.7   *********************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("-------------------- Try to go create cache page ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.go_createCachePage(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("---------- Start create Cache based on Team: None & Version: 5.0.7  -------------")
        Team = cache.Team_None
        ServerName = "testCache0141"
        Password = "Qwer1234!!"
        Cache_Version = cache.Version_5_0_7
        WebClientEmail = "test@gmail.com"
        WebClientPassword = "Qwer1234!!"

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CC.cache(self, Team, ServerName, Password, Cache_Version, WebClientEmail, WebClientPassword)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

    @pytest.mark.regression
    def test_TC002(self, setup):

        print("****************** Try to go create Cache based on Team: None & Version: 6.0.5  *********************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("-------------------- Try to go create cache page ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.go_createCachePage(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("---------- Start create Cache based on Team: None & Version: 6.0.5  -------------")
        Team = cache.Team_None
        ServerName = "testCache0141"
        Password = "Qwer1234!!"
        Cache_Version = cache.version_6_0_5
        WebClientEmail = "test@gmail.com"
        WebClientPassword = "Qwer1234!!"

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CC.cache(self, Team, ServerName, Password, Cache_Version, WebClientEmail, WebClientPassword)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

    @pytest.mark.regression
    def test_TC003(self, setup):

        print("****************** Try to go create Cache based on Team: Default & Version: 5.0.7  *********************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("-------------------- Try to go create cache page ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.go_createCachePage(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("---------- Start create Cache based on Team: Default & Version: 5.0.7  -------------")
        Team = cache.DefaultTeam_cache
        ServerName = "testCache0141"
        Password = "Qwer1234!!"
        Cache_Version = cache.Version_5_0_7
        WebClientEmail = "test@gmail.com"
        WebClientPassword = "Qwer1234!!"

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CC.cache(self, Team, ServerName, Password, Cache_Version, WebClientEmail, WebClientPassword)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

    @pytest.mark.regression
    def test_TC004(self, setup):

        print("****************** Try to go create Cache based on Team: Default & Version: 6.0.5  *********************")
        # self.logger.info("****Started Home page title test ****")
        self.driver = setup
        ss = SS(self.driver)
        cache = CreateCache(self.driver)

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("-------------------- Try to go create cache page ---------------")

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CF.go_createCachePage(self)
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("---------- Start create Cache based on Team: Default & Version: 6.0.5  -------------")
        Team = cache.DefaultTeam_cache
        ServerName = "testCache0141"
        Password = "Qwer1234!!"
        Cache_Version = cache.version_6_0_5
        WebClientEmail = "test@gmail.com"
        WebClientPassword = "Qwer1234!!"

        try:
            self.driver.refresh()
            time.sleep(3)
            self.CC.cache(self, Team, ServerName, Password, Cache_Version, WebClientEmail, WebClientPassword)

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
