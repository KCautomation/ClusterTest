import time
import pytest

import simple_colors
from colorama import Fore
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Src.all_locators.Locators import Locator
from selenium.common.exceptions import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    WebDriverException

from Src.screenShot.screenShot import SS
from pageObjects.Cache.pomCache import CreateCache

ss_path = "/Screenshots/Cache/deleteCache/"


class cacheFunctions:

    @staticmethod
    def go_createCachePage(self):
        driver = self.driver
        print(Fore.CYAN + "-----------------------From Header frame----------------------------------------")
        # click on create button from header
        try:
            CreateNew_H = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.CreateNew_H)))
            print("CreateNew_H button is clickable")
            CreateNew_H.click()
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        else:
            print('Successfully clicked on CreateNew')

        # click on "New Application" button from dropdown
        try:
            cacheButton = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.cacheButton)))
            print("cache button is clickable")
            cacheButton.click()
            time.sleep(5)
            driver.implicitly_wait(20)

            WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.XPATH, Locator.redis_button)))
            time.sleep(3)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            page = self.driver.title
            print("Welcome Create Cache Page & Create Database Title is:", page)

    @staticmethod
    def deleteCache(self, ServerName):
        driver = self.driver
        cache = CreateCache(self.driver)
        ss = SS(self.driver)

        print("******************************* Test Try to delete cache******************************")

        print("----------------------try to click on Settings button--------------------")
        try:
            Cache_Settings = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_Settings))
            print("application_Settings is clickable")
            Cache_Settings.click()
            print("Welcome application_Settings ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 50")
        print("Scroll down")
        time.sleep(3)

        print("----------------------try to click on Delete button from below--------------------")
        try:
            Cache_Delete = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_Delete))
            print("Cache_Delete is clickable")
            Cache_Delete.click()
            print("successfully clicked Cache_Delete ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        print("----------------------try to input Cache name--------------------")
        try:
            Cache_namebox_D = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Cache_namebox_D))
            print("Cache_namebox_D is clickable")
            Cache_namebox_D.send_keys(ServerName)
            print("successfully inputted Cache_namebox_D ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        # self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        # print("Scroll down")
        # time.sleep(3)

        print("----------------------click on  Delete permanently button--------------------")
        try:
            Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(cache.Delete_permanently_button))
            print("application_Delete is clickable")
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        print("----------------------check Message--------------------")
        try:
            Cache_Deleted_Success_msg = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located(cache.Cache_Deleted_Success_msg))
            if Cache_Deleted_Success_msg.is_displayed():
                print('Shown a message: ',
                      simple_colors.green(Cache_Deleted_Success_msg.text, ['bold', 'underlined']))
                print("\n")
                time.sleep(45)
                pass
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)

        print("----------------------'" + ServerName + "' deleted validation from cache list--------------------")
        try:
            self.driver.refresh()
            time.sleep(4)

            cache_name = self.driver.find_element(By.XPATH, "//span[normalize-space()='" + ServerName + "']")
            if cache_name.is_Displayed():
                print(ServerName, "is still present or disable in the list")
                file_name = ss_path + "delete_or_disable_cache" + time.asctime().replace(":", "_") + ".png"
                ss.driver.save_screenshot(file_name)
                ss.ScreenShot(file_name)

                assert False
            else:
                print("successfully clicked on :", ServerName)
                print(Fore.RED + ServerName, "cache is not available is the list, that means deleted successfully")
                assert True

        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)
        except AssertionError as e:
            print("AssertionError", e)
