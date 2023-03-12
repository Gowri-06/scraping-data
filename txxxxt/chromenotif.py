import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# our domian name

# navigate to the Chrome settings page
driver.get("chrome://settings/")


# driver.get('chrome://settings/')
# driver.maximize_window()
# time.sleep(10)
# # privacy_security = driver.find_element(By.XPATH,"//*[@id='searchInput']").send_keys("Site settings")
# link = driver.find_element(By.LINK_TEXT,"Privacy and security").click()
# #  = driver.find_element(By.XPATH, "").click()
# time.sleep(5)
# alert = Alert(driver)
# alert.accept()
# alert.dismiss()
# notifications_close = driver.find_element(By.XPATH, "").click()
# maker_tab_click = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div/div[3]/a").click()
# actions = ActionChains(driver)
# actions.click(on_element=login_click)
# actions.perform()
# login = driver.find_element(By.CLASS_NAME, "login")
# login.click()
# print(login)
# Enter login details
# driver.find_element(By.ID, "id_login").send_keys("gowridev007@gmail.com")
# driver.find_element(By.ID, "id_password").send_keys("tester@123")
# login_page = driver.find_element(By.CSS_SELECTOR, "button").click()
time.sleep(5)
# print("text",login_page)
# driver.back()



    

   
