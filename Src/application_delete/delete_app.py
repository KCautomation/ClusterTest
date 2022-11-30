import time
from telnetlib import EC
import pytest

import simple_colors
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from Src.all_locators.Locators import Locator

# from src.screen_shots.screen_shots import SS
# from src.base.environment_setup import EnvironmentSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from src.function.logIn.login_fun import test_cluster_login

ss_path = "/Applications/PHP/"


# class DeleteApplication(EnvironmentSetup):

def test_delete_app(self, ApplicationName):
    # pytest.skip("Skipping test...later I will implement...")
    driver = self.driver
    # ApplicationName = input("Enter Application Name: ")
    # click on settings
    print("******************************* Test Try to delete application******************************")

    print("-------Try to click on application Settings--------")

    try:
        application_Settings = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locator.application_Settings)))
        print("application_Settings is clickable")
        application_Settings.click()
        print("Welcome application_Settings ")
        time.sleep(5)
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)

    # click on Delete button
    print("-------Try to click on application Delete--------")
    try:
        application_Delete = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locator.application_Delete)))
        print("application_Delete is clickable")
        application_Delete.click()
        print("successfully clicked application_Delete ")
        time.sleep(5)
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)

    # input application name
    print("-------Try to put Application Name in application name box--------")
    try:
        Application_namebox_D = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locator.Application_namebox_D)))
        print("application_Delete is clickable")
        Application_namebox_D.send_keys(ApplicationName)
        print("successfully inputted Application_name ")
        time.sleep(5)
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)

    # scroll down
    driver.execute_script("document.querySelector('.sidenav-content').scrollTop = 20")
    print("Scroll down")
    time.sleep(3)

    # input application name
    try:
        Delete_permanently_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locator.Delete_permanently_button)))
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

    # check msg
    try:
        Application_Deleted_Success_msg = WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.XPATH, Locator.Application_Deleted_Success_msg)))
        if Application_Deleted_Success_msg.is_displayed():

            print('Shown a message: ',
                  simple_colors.green(Application_Deleted_Success_msg.text, ['bold', 'underlined']))
            print("\n")
            pass
        else:
            pass
        time.sleep(10)
    except NoSuchElementException as e:
        print("NoSuchElementException error :\n", e, "\n")
    except TimeoutException as e:
        print("TimeoutException error", e)
    except InvalidSessionIdException as e:
        print("InvalidSessionIdException", e)
    except AssertionError as e:
        print("AssertionError", e)
    # ss = SS(driver)
    # file_name = ss_path + "delete_success_screenshot_" + time.asctime().replace(":", "_") + ".png"
    # ss.driver.save_screenshot(file_name)
    # ss.ScreenShot(file_name)
