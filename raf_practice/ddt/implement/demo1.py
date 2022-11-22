import time
import logging
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl


class Test_001_Login:
    baseURL = "https://eks.alpha.klovercloud.io/"

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def object_setup(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        print(act_title)

        if act_title == "KloverCloud | Sign In":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(
                "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
            self.driver.close()
            assert False

    # @pytest.mark.sanity
    @pytest.mark.run(order=1)
    def test_login(self):

        self.logger.info("****Started Login Test****")
        driver = self.driver
        self.lp = LoginPage(self.driver)
        self.lp.setUserName("useremail")
        time.sleep(1)
        self.lp.setPassword("password")
        time.sleep(1)
        self.lp.clickLogin()
        time.sleep(10)
        act_title = self.driver.title
        if act_title == "KloverCloud | Dashboard":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(
                "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
            self.driver.close()
            assert False