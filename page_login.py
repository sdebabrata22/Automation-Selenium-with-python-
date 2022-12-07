from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.facebook.com/')
driver.maximize_window()


driver.find_element(By.ID,"email").send_keys("samaldebabrat608@gmail.com")
driver.find_element(By.ID,"pass").send_keys("dev@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()



