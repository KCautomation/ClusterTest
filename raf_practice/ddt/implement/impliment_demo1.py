import time
import logging
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl
import raf_practice.ddt.implement.demo1 as ob


@pytest.mark.usefixtures("setup")
class Test_002_Login:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def test_homePageTitle(self):
        ob.Test_001_Login()

    # m = test_homePageTitle()
    # m.test_homePageTitle()




# # @pytest.mark.sanity
# @pytest.mark.regression
# def test_login(self, setup):
#
#     self.logger.info("****Started Login Test****")
#     self.driver = setup
#     self.driver.get(self.baseURL)
#     self.driver.implicitly_wait(20)
#     self.lp = LoginPage(self.driver)
#     self.lp.setUserName(self.useremail)
#     time.sleep(1)
#     self.lp.setPassword(self.password)
#     time.sleep(1)
#     self.lp.clickLogin()
#     time.sleep(10)
#     act_title = self.driver.title
#     if act_title == "KloverCloud | Dashboard":
#         self.logger.info("****Login test passed ****")
#         self.driver.close()
#         assert True
#     else:
#         self.logger.error("****Login test failed ****")
#         self.driver.save_screenshot(
#             "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
#         self.driver.close()
#         assert False
