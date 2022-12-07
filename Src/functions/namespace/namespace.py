import time

import allure
import pytest

import simple_colors
from allure_commons.types import AttachmentType
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


class NamespaceFunctions:
    @staticmethod
    def namespaceDelete(self, Namespace_Name):
        print("-------Try to click on namespace Delete--------")
        try:
            deleteButton_namespace = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.deleteButton_namespace)))
            deleteButton_namespace.click()
            time.sleep(4)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # input application name
        print("-------Try to put Application Name in application name box--------")
        try:
            input_namespaceName = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
            print("application_Delete is clickable")
            input_namespaceName.send_keys(Namespace_Name)
            print("successfully inputted Application_name ")
            time.sleep(5)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # scroll down
        self.driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
        print("Scroll down")
        time.sleep(3)

        # input application name
        try:
            Delete_permanently_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Delete_permanently_button)))
            Delete_permanently_button.click()
            print("successfully clicked on Delete_permanently_button ")
            time.sleep(15)
            self.driver.refresh()
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException", e)

        # delete validation
        try:
            self.driver.refresh()
            Namespace = WebDriverWait(self.driver, 120).until(
                EC.presence_of_element_located((By.XPATH, "//span[normalize-space()= '" + Namespace_Name + "']")))
            if Namespace.is_displayed():
                allure.attach(self.driver.get_screenshot_as_png(), name="delete_Screenshot",
                              attachment_type=AttachmentType.PNG)
                print("Namespace '" + Namespace_Name + "' is found")
                assert False

            else:
                print("Namespace '" + Namespace_Name + "' is not found")
                assert True

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        except AssertionError as e:
            print("AssertionError error", e)

    # @staticmethod
    # def namespaceDelete(self, Namespace_Name):
