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

        print("****************** Try to Test Cluster Login *********************")
        try:
            self.login.test_cluster_login(self)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("****************** Try to go create namespace page *********************")

        Namespace_Name = 'test-orga'

        self.driver.find_element(By.XPATH, "//span[normalize-space()='Namespace']").click()
        self.driver.implicitly_wait(5)
        time.sleep(3)


        try:
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '" + Namespace_Name + "']")))
            if Namespace.is_displayed():
                Namespace.click()
                time.sleep(5)
                print("Welcome to '" + Namespace_Name + "' namespace & page title is :", self.driver.title)
                pass

            else:
                print("Created failed")
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # act_title = self.driver.title
        # print(act_title)
        # if act_title == Namespace_Name:
        #     self.logger.info("****Login test passed ****")
        #     self.driver.close()
        #     # assert True
        # else:
        #     self.logger.error("****Login test failed ****")
        #     # self.driver.save_screenshot(
        #     #     "C:/Users/shabr/PycharmProjects/ClusterTest/Screenshots/" + "test_loginPageTitle.png")
        #     self.driver.close()
        #     # assert False
