import pandas as pd

df = pd.read_excel("ProducthuntProduct.xlsx",sheet_name="Sheet1")
# print(df)
url = df["Url"]
url_list =  [ product for product in url ]
print("url_listtt",len(url_list),type(url_list))
for i in range(0,100):
    print(i)
    print(url_list[i])
# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.action_chains import ActionChains

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys

# download chrome driver file
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
# our domian name
driver.get("https://www.selfinstaller.com/")
driver.maximize_window()
driver.implicitly_wait(1000)
# Home login click to enter in to login page
login_click = driver.find_element(By.XPATH, "/html/body/header/div/div[3]/a")
actions = ActionChains(driver)
actions.click(on_element=login_click)
actions.perform()
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



    

   
