import time
import logging
import pytest
from pageObjects.Login.loginPage2 import LoginPage2
from utilities.readProperties import ReadConfig
import raf_practice.logs.customolog.custom_logger as cl


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(20)
        self.lp = LoginPage2(self.driver)

        self.lp.Email_box.send_keys(self.useremail)
        self.lp.Password_box.send_keys(self.password)
        self.lp.Sign_In_button.click()
        self.driver.implicitly_wait(20)

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
