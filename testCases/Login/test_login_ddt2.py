import time
import logging
import pytest
from selenium import webdriver
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl
from utilities import XLUtils
from utilities.readProperties import ReadConfig
import time


class Test_002_Login:
    baseURL = ReadConfig.getApplicationURL()
    logger = cl.customLogger(logging.DEBUG)
    path = "/TestData/Login_data_two.xlsx"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********Test_003_Login*********")
        self.logger.info("****Verifying Login DDT Test2****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Sheet1")
        print("Number of Rows i a Excel: ", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "KloverCloud | Dashboard"

            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.lp.ClickProfile()
                    time.sleep(2)
                    self.lp.clickLogout()
                    time.sleep(3)
                    # self.lp.clickLogout();
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    self.lp.ClickProfile()
                    time.sleep(2)
                    self.lp.clickLogout()
                    time.sleep(3)
                    # self.lp.clickLogout();
                    lst_status.append("Fail")

            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
            print(lst_status)
        self.driver.refresh()
        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");

        # lst_status = []
        # for r in range(2, self.rows + 1):
        #     self.username = XLUtils.readData(self.path, "Sheet1", r, 1)
        #     self.password = XLUtils.readData(self.path, "Sheet1", r, 2)
        #     self.exp = XLUtils.readData(self.path, "Sheet1", r, 3)
        #
        #     self.lp.setUserName(self.username)
        #     time.sleep(1)
        #     self.lp.setPassword(self.password)
        #     time.sleep(1)
        #     self.lp.clickLogin()
        #     time.sleep(6)
        #     act_title = self.driver.title
        #     exp_title = "KloverCloud | Dashboard"
        #
        #     if act_title == exp_title:
        #         if self.exp == 'Pass':
        #             self.logger.info("**** passed ****")
        #             self.lp.ClickProfile()
        #             time.sleep(2)
        #             self.lp.clickLogout()
        #             time.sleep(3)
        #             lst_status.append("Pass")
        #         elif self.exp == 'Fail':
        #             self.logger.info("**** failed ****")
        #             self.lp.ClickProfile()
        #             time.sleep(2)
        #             self.lp.clickLogout()
        #             lst_status.append("Fail")
        #             time.sleep(5)
        #
        #     elif act_title != exp_title:
        #         if self.exp == 'Pass':
        #             self.logger.info("**** failed ****")
        #             lst_status.append("Fail")
        #         elif self.exp == 'Fail':
        #             self.logger.info("**** passed ****")
        #             lst_status.append("Pass")
        #             print(lst_status)
        #
        # if "Fail" not in lst_status:
        #     self.logger.info("******* DDT Login test passed **********")
        #     self.driver.close()
        #     assert True
        # else:
        #     self.logger.error("******* DDT Login test failed **********")
        #     self.driver.close()
        #     assert False
        #
        # self.logger.info("******* End of Login DDT Test **********")
        # self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ")
