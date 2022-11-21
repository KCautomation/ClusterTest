import time

import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.warning("*************** Test_001_Login *****************")
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

    demo = logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        time.sleep(1)
        self.lp.setPassword(self.password)
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


# demo = Test_001_Login()
# demo.loggen()
