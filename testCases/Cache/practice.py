import time
import logging
import pytest
from selenium.webdriver.common.by import By
from Src.all_locators.Locators import Locator
from Src.highlight_Element.highlight_ele import highlight
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import raf_practice.logs.customolog.custom_logger as cl
from utilities import XLUtils
from selenium import webdriver


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

        box = self.driver.find_element(By.XPATH, Locator.Email_box)
        time.sleep(4)

        highlight(box, 3, "yellow", 3)
        box.send_keys("kupa")
        time.sleep(4)
