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


class login:
    @staticmethod
    def test_cluster_login(self):
        driver = self.driver
        baseURL = ReadConfig.getApplicationURL()
        username = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()
        # try block to read URL
        try:
            html = urlopen(baseURL)

        # except block to catch
        # exception
        # and identify error
        except HTTPError as e:
            print(Fore.LIGHTRED_EX + "HTTP error", e)

        except URLError as e:
            print(Fore.LIGHTRED_EX + "Opps ! Page not found!", e)

        except WebDriverException as e:
            print(Fore.LIGHTRED_EX + "WebDriverException", e)

        else:
            print(Fore.YELLOW + 'Yeah ! URL found ')

        driver.get(baseURL)
        driver.implicitly_wait(20)
        time.sleep(2)

        # put Email
        try:
            Email_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Email_box)))
            print("Email_box is inputable")
            Email_box.send_keys(username)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put email in Email_box')

        # put password
        try:
            Password_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.Password_box)))
            print("Password_box is inputable")
            Password_box.send_keys(password)
            time.sleep(2)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        else:
            print('Successfully put password in Password_box')

        # click on Toggle_Visibility_Button
        try:
            Toggle_Visibility_Button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Toggle_Visibility_Button)))
            print("Toggle_Visibility_Button is clickable")
            Toggle_Visibility_Button.click()
            time.sleep(1)
            Toggle_Visibility_Button.click()
            time.sleep(1)
        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        else:
            print('Successfully showed & hided Password')
        # Click on Sign In button

        try:
            Sign_In_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, Locator.Sign_In_button)))
            print("Password_box is inputable")
            Sign_In_button.click()
            self.driver.implicitly_wait(10)
            time.sleep(7)
        except NoSuchElementException as e:
            print("NoSuchElementException error :\n", e, "\n")
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)
        else:
            print('Successfully click on Sign In button')

        # check error message have or not
        try:
            LogIn_Authentication_Error = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Locator.LogIn_Authentication_Error)))
            if LogIn_Authentication_Error.is_displayed():
                print("\n")
                print('Shown a error message: ',
                      simple_colors.red(LogIn_Authentication_Error.text, ['bold', 'underlined']))
                print("\n")
                self.driver.close()
                self.driver.stop()
                # return FileExistsError
            else:
                pass

        except NoSuchElementException as e:
            print("NoSuchElementException error", e)
        except TimeoutException as e:
            print("TimeoutException error", e)
        except InvalidSessionIdException as e:
            print("InvalidSessionIdException error", e)

        # Login validation
        # try:
        #     if WebDriverWait(driver, 50).until(
        #             EC.visibility_of_element_located((By.XPATH, Locator.Dashboard_button))):
        #         Dashboard_title = driver.title
        #         Accepted_title = "KloverCloud | Dashboard"
        #         self.assertEqual(Dashboard_title, Accepted_title)
        #         print("Successfully logged in && Welcome to", Dashboard_title)
        #     else:
        #         print("Login Failed")
        #         assert False
        # except NoSuchElementException as e:
        #     print("NoSuchElementException error", e)
        # except TimeoutException as e:
        #     print("TimeoutException error", e)
        # except InvalidSessionIdException as e:
        #     print("InvalidSessionIdException error", e)
