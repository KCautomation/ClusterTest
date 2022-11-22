import time

from selenium.webdriver.common.by import By

import XLUtils
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://eks.alpha.klovercloud.io/")
driver.maximize_window()
driver.implicitly_wait(10)

path = "C:/Users/shabr/PycharmProjects/ClusterTest/raf_practice/ddt/for_xl/Login1.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")

for r in range(2, rows + 1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys(password)

    driver.find_element(By.XPATH,
                        "//body/kc-root[1]/kc-login[1]/div[1]/div[2]/div[1]/form[1]/button[1]/span[1]/div[1]").click()

    act_title = driver.title
    if act_title == "KloverCloud | Dashboard":
        assert True
        XLUtils.writeData(path, "Sheet1", r, 3, "test passed")

    else:
        XLUtils.writeData(path, "Sheet1", r, 3, "test failed")
        print("test failed")

    time.sleep(3)
    driver.refresh()
