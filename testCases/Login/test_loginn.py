import time

import pytest
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException
from pageObjects.login3 import Login3


class Test001:

    @pytest.mark.sanity
    @pytest.mark.regression
    def test(self, setup):
        self.driver = setup
        driver = self.driver
        self.driver.get("https://eks.alpha.klovercloud.io/")
        self.driver.set_page_load_timeout(30)

        home = Login3(driver)
        home.useremail.send_keys("LambdaTest")
        time.sleep(1)
        home.password.send_keys("LambdaTest")
        time.sleep(1)

        home.signin_button.submit()
        time.sleep(5)
