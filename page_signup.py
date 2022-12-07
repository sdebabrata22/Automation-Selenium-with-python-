import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text()='Create New Account']").click()
time.sleep(2)
driver.find_element(By.NAME, "firstname").send_keys("debabrata")
driver.find_element(By.NAME, "lastname").send_keys("samal")

driver.find_element(By.NAME, "reg_email__").send_keys("9040525082")
driver.find_element(By.ID, "password_step_input").send_keys("dev@123")

day = Select(driver.find_element(By.ID, "day"))
day.select_by_visible_text("25")

month = Select(driver.find_element(By.ID, "month"))
month.select_by_visible_text("Feb")

year = Select(driver.find_element(By.ID, "year"))
year.select_by_visible_text("1991")

driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.NAME, "websubmit").click()
