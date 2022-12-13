import logging
import time
import allure
import pytest
import simple_colors
from colorama import Fore
from selenium.webdriver import Keys, ActionChains

import raf_practice.logs.customolog.custom_logger as cl
from Src.login_function.login import login
from Src.screenShot.screenShot import SS
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException
from allure_commons.types import AttachmentType
from utilities.readProperties import ReadConfig
from Src.functions.applications.application_functions import ApplicationFunctions
from pageObjects.Apllications.pomCreateApplication import CreateApplication
from pageObjects.Database.pomDatabase import Database
from Src.functions.cache.cacheFunction import cacheFunctions
from pageObjects.Cache.pomCache import CreateCache

ss_path = "/Login/"


class CreateCaches:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)
    CF = cacheFunctions()

    @staticmethod
    def cache(self, Team, ServerName, Password, Cache_Version, WebClientEmail, WebClientPassword):
        ss = SS(self.driver)
        action = ActionChains(self.driver)
        cache = CreateCache(self.driver)

        print("--------------- Try to choose redis -----------------")
        try:
            redis_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.redis_button))
            if redis_button.is_displayed():
                redis_button.click()
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "redis_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("----------------- Try to choose Team ----------------------")

        print("---try to click team box---")
        try:
            teamBox_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.teamBox_c))
            if teamBox_c.is_displayed():
                teamBox_c.click()
                time.sleep(2)
            else:
                file_name = ss_path + "teamBox_c" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to choose default as a team-------------------------------")

        try:
            Team = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(Team))
            if Team.is_displayed():
                Team.click()
                time.sleep(2)
            else:
                file_name = ss_path + "defaultTeam_database" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose default Team")

        print("-----Scroll down to show Namespaces-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose a namespace -------------------------------")
        try:
            Namespace_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.Namespace_c))
            if Namespace_c.is_displayed():
                Namespace_c.click()
                time.sleep(2)
            else:
                file_name = ss_path + "namespace_first" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----Scroll up-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -400")
        time.sleep(2)

        print("-----------------------try to put cache server name -------------------------------")
        try:
            serverNameBox_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.serverNameBox_c))
            if serverNameBox_c.is_displayed():
                serverNameBox_c.clear()
                serverNameBox_c.send_keys(ServerName)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "serverNameBox_c" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to put cache Password -------------------------------")
        try:
            adminPassword_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.adminPassword_c))
            if adminPassword_c.is_displayed():
                adminPassword_c.clear()
                adminPassword_c.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "initial_AdminPassword" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to put database Password -------------------------------")
        try:
            confirmPassword_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.confirmPassword_c))
            if confirmPassword_c.is_displayed():
                confirmPassword_c.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_Password" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to click 0n selectVersion_box-------------------------------")

        try:
            selectVersion_c = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.selectVersion_c))
            if selectVersion_c.is_displayed():
                selectVersion_c.click()
                time.sleep(2)
            else:
                file_name = ss_path + "selectVersion_box" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        try:
            Cache_Version = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(Cache_Version))
            if Cache_Version.is_displayed():
                Cache_Version.click()
                time.sleep(2)
            else:
                file_name = ss_path + "Cache_Version" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose Enable Web Client (P3 X Redis UI)-------------------------------")

        try:
            enableWebClient = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.Enable_Web_Client_P3_X_Redis))
            if enableWebClient.is_displayed():
                enableWebClient.click()
                time.sleep(2)
            else:
                file_name = ss_path + "enableWebClient" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 800")
        time.sleep(2)

        print("-----------------------try to put Web_Client_Email -------------------------------")
        try:
            Web_Client_Email = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.Web_Client_Email))
            if Web_Client_Email.is_displayed():
                Web_Client_Email.clear()
                Web_Client_Email.send_keys(WebClientEmail)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "cache_server_name" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to put Web Client Password -------------------------------")
        try:
            Web_Client_Password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.Web_Client_Password))
            if Web_Client_Password.is_displayed():
                Web_Client_Password.clear()
                Web_Client_Password.send_keys(WebClientPassword)
                time.sleep(2)
            else:
                file_name = ss_path + "initial_AdminPassword" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to click Next button-------------------------------")

        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.next_button))
            if next_button.is_displayed():
                next_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "next_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------try to click Next button again-------------------------------")
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.next_button))
            if next_button.is_displayed():
                next_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "next_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to click Confirm button-------------------------------")

        try:
            confirm_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(cache.confirm_button))
            if confirm_button.is_displayed():
                confirm_button.click()
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        print("-----------------------Message check-------------------------------")

        try:
            Cache_createdMsg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(cache.Cache_createdMsg))
            if Cache_createdMsg.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(Cache_createdMsg.text, ['bold', 'underlined']))
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locator.Cancel_msg).click()
                time.sleep(1)

                # Wait to finish create
                WebDriverWait(self.driver, 500).until(
                    EC.visibility_of_element_located((By.XPATH, Locator.Access_Terminal)))
                time.sleep(5)
                pass
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

