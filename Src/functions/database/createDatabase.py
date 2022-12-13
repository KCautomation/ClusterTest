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

ss_path = "/Login/"


class CreateDatabases:
    # logger = LogGen.loggen()
    logger = cl.customLogger(logging.DEBUG)

    @staticmethod
    def mySql(self, Team, ServerName, Password, MySql_Version):

        ss = SS(self.driver)
        action = ActionChains(self.driver)
        data = Database(self.driver)

        print("****************** Try to choose MySQL database *********************")

        try:
            MySQL_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.MySQL_button))
            if MySQL_button.is_displayed():
                MySQL_button.click()
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "MySQL_button" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose MySQL_button")

        print("****************** Try to choose Team *********************")

        print("---try to click team box---")
        try:
            teamBox_database = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.teamBox_database))
            if teamBox_database.is_displayed():
                teamBox_database.click()
                time.sleep(2)
            else:
                file_name = ss_path + "teamBox_database" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on team box")

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
            namespace_first = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.namespace_first))
            if namespace_first.is_displayed():
                namespace_first.click()
                time.sleep(2)
            else:
                file_name = ss_path + "namespace_first" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose First Namespace")

        print("-----Scroll up-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -400")
        time.sleep(2)

        print("-----------------------try to put database server name -------------------------------")
        try:
            database_ServerName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.database_ServerName))
            if database_ServerName.is_displayed():
                database_ServerName.clear()
                database_ServerName.send_keys(ServerName)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "database_ServerName" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put Database ServerName")

        print("-----------------------try to put database Password -------------------------------")
        try:
            initial_AdminPassword = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.initial_AdminPassword))
            if initial_AdminPassword.is_displayed():
                initial_AdminPassword.clear()
                initial_AdminPassword.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "initial_AdminPassword" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial AdminPassword")

        print("-----------------------try to put database Password -------------------------------")
        try:
            confirm_Password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.confirm_Password))
            if confirm_Password.is_displayed():
                confirm_Password.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_Password" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial confirm_Password")

        print("-----------------------try to click 0n selectVersion_box-------------------------------")

        try:
            selectVersion_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.selectVersion_box))
            if selectVersion_box.is_displayed():
                selectVersion_box.click()
                time.sleep(2)
            else:
                file_name = ss_path + "selectVersion_box" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on selectVersion_box")

        try:
            MySql_Version = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(MySql_Version))
            if MySql_Version.is_displayed():
                MySql_Version.click()
                time.sleep(2)
            else:
                file_name = ss_path + "version_8_0_19" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose version 8.0.19")

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose Enable Web Client (phpMyAdmin)-------------------------------")

        try:
            enableWebClient = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.enableWebClient)))
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
        else:
            print("Successfully chose Enable Web Client (phpMyAdmin)")

        print("-----------------------try to click Next button-------------------------------")

        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
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
        else:
            print("Successfully clicked on Next button")

        print("-----------------------try to click Next button again-------------------------------")
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
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
        else:
            print("Successfully clicked on Next button")

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to click Confirm button-------------------------------")

        try:
            confirm_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.confirm_button))
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
        else:
            print("Successfully clicked on Confirm button")

        print("-----------------------Message check-------------------------------")

        try:
            Database_CreatedMsg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(data.Database_CreatedMsg))
            if Database_CreatedMsg.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(Database_CreatedMsg.text, ['bold', 'underlined']))
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locator.Cancel_msg).click()
                time.sleep(7)
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(4)

        print("-----------------------Wait to database initialization------------------------------")
        try:
            WaitTo_Create = WebDriverWait(self.driver, 400).until(
                EC.visibility_of_element_located(data.WaitTo_Create))
            if WaitTo_Create.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(WaitTo_Create.text, ['bold', 'underlined']))
                time.sleep(3)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 600")
        time.sleep(3)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -600")
        time.sleep(3)

    @staticmethod
    def Postgresql(self, Team, ServerName, Password, Postgresql_Version, WebClientEmail, WebClientPassword):

        ss = SS(self.driver)
        action = ActionChains(self.driver)
        data = Database(self.driver)

        print("****************** Try to choose Postgresql database *********************")

        try:
            Postgresql = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.Postgresql))
            if Postgresql.is_displayed():
                Postgresql.click()
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "Postgresql" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose MySQL_button")

        print("****************** Try to choose Team *********************")

        print("---try to click team box---")
        try:
            teamBox_database = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.teamBox_database))
            if teamBox_database.is_displayed():
                teamBox_database.click()
                time.sleep(2)
            else:
                file_name = ss_path + "teamBox_database" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on team box")

        print("-----------------------Team-------------------------------")

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
            namespace_first = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.namespace_first))
            if namespace_first.is_displayed():
                namespace_first.click()
                time.sleep(2)
            else:
                file_name = ss_path + "namespace_first" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose First Namespace")

        print("-----Scroll up-----")
        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -400")
        time.sleep(2)

        print("-----------------------try to put database server name -------------------------------")
        try:
            database_ServerName = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.database_ServerName))
            if database_ServerName.is_displayed():
                database_ServerName.clear()
                database_ServerName.send_keys(ServerName)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "database_ServerName" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put Database ServerName")

        print("-----------------------try to put database Password -------------------------------")
        try:
            initial_AdminPassword = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.initial_AdminPassword))
            if initial_AdminPassword.is_displayed():
                initial_AdminPassword.clear()
                initial_AdminPassword.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "initial_AdminPassword" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial AdminPassword")

        print("-----------------------try to put database Password -------------------------------")
        try:
            confirm_Password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.confirm_Password))
            if confirm_Password.is_displayed():
                confirm_Password.send_keys(Password)
                time.sleep(2)
            else:
                file_name = ss_path + "confirm_Password" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put initial confirm_Password")

        print("---------------------Choose Postgresql Version--------------------------")

        try:
            selectVersion_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.selectVersion_box))
            if selectVersion_box.is_displayed():
                selectVersion_box.click()
                time.sleep(2)
            else:
                file_name = ss_path + "selectVersion_box" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully clicked on selectVersion_box")

        try:
            Postgresql_Version = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(Postgresql_Version))
            if Postgresql_Version.is_displayed():
                Postgresql_Version.click()
                time.sleep(2)
            else:
                file_name = ss_path + "version_8_0_19" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully chose version 8.0.19")

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)

        print("-----------------------try to choose Enable Web Client (phpMyAdmin)-------------------------------")

        try:
            enableWebClient = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, Locator.enableWebClient)))
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
        else:
            print("Successfully chose Enable Web Client (phpMyAdmin)")

        print("-----------------------try to put Web_Client_Email -------------------------------")
        try:
            Web_Client_Email = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.Web_Client_Email))
            if Web_Client_Email.is_displayed():
                Web_Client_Email.clear()
                Web_Client_Email.send_keys(WebClientEmail)
                self.driver.implicitly_wait(20)
                time.sleep(2)
            else:
                file_name = ss_path + "database_ServerName" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print("Successfully put Database ServerName")

        print("-----------------------try to put Web Client Password -------------------------------")
        try:
            Web_Client_Password = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.Web_Client_Password))
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
        else:
            print("Successfully put initial AdminPassword")

        print("-----------------------try to click Next button-------------------------------")

        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
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
        else:
            print("Successfully clicked on Next button")

        print("-----------------------try to click Next button again-------------------------------")
        try:
            next_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.next_button))
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
        else:
            print("Successfully clicked on Next button")

        print("-----Scroll down -----")
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 450")
        time.sleep(2)

        print("-----------------------try to click Confirm button-------------------------------")

        try:
            confirm_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(data.confirm_button))
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
        else:
            print("Successfully clicked on Confirm button")

        print("-----------------------Message check-------------------------------")

        try:
            Database_CreatedMsg = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(data.Database_CreatedMsg))
            if Database_CreatedMsg.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(Database_CreatedMsg.text, ['bold', 'underlined']))
                time.sleep(5)
                self.driver.find_element(By.XPATH, Locator.Cancel_msg).click()
                time.sleep(7)
            else:
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)

        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(4)

        print("-----------------------Wait to database initialization------------------------------")
        try:
            WaitTo_Create = WebDriverWait(self.driver, 400).until(
                EC.visibility_of_element_located(data.WaitTo_Create))
            if WaitTo_Create.is_displayed():
                print('Shown a message: ',
                      simple_colors.blue(WaitTo_Create.text, ['bold', 'underlined']))
                time.sleep(3)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # again scroll below
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 400")
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 600")
        time.sleep(3)
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = -600")
        time.sleep(3)
