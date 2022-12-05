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
from urllib.request import urlopen
from urllib.error import *
from utilities.readProperties import ReadConfig
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
from urllib.request import urlopen
from urllib.error import *
from utilities.readProperties import ReadConfig

ss_path = "/LogIn/"


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
            print("NewApplication_H button is clickable")
            cacheButton.click()
            time.sleep(5)
            driver.implicitly_wait(20)

            WebDriverWait(driver, 80).until(EC.element_to_be_clickable((By.XPATH, Locator.wait_forfilter)))
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            page = self.driver.title
            print("Welcome Create Database Page & Create Database Title is:", page)
