import time
import logging
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)

    # @pytest.mark.regression
    # def test_homePageTitle(self, setup):
    #     self.logger.info("*************** Test_001_Login *****************")
    #     self.logger.info("****Started Home page title test ****")
    #     self.driver = setup
    #     self.logger.info("****Opening URL****")
    #     self.driver.get(self.baseURL)
    #     act_title = self.driver.title
    #     print(act_title)
    #
    #     if act_title == "KloverCloud | Sign In":
    #         self.logger.info("**** Home page title test passed ****")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.logger.error("**** Home page title test failed****")
    #         self.driver.save_screenshot(
    #             "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
    #         self.driver.close()
    #         assert False

    @data(("imon", "aman"))
    @unpack
    def test_login(self, user, pasw):
        self.logger.info("****Started Login Test****")
        driver = self.driver
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(user)
        time.sleep(1)
        self.lp.setPassword(pasw)
        time.sleep(1)
        self.lp.clickLogin()
        time.sleep(4)
        self.driver.refresh()
        time.sleep(2)

        # act_title = self.driver.title
        # if act_title == "KloverCloud | Dashboard":
        #     self.logger.info("****Login test passed ****")
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.error("****Login test failed ****")
        #     self.driver.save_screenshot(
        #         "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
        #     self.driver.close()
        #     assert False
