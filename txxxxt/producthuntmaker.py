import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options


option1 = Options()
option1.headless = True
option1.add_argument("--disable-notifications")
service = Service("E:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service,options=option1,chrome_options=option1)
df = pd.read_excel("./txxxxt/ProducthuntProduct.xlsx",sheet_name="Sheet1")
# service=service
# print(df)
url = df["Url"]
url_list =  [ product for product in url ]
print("url_listtt",len(url_list),type(url_list))
maker_designation_info = []
for i in range(0,100):
    print(i)
    # print(url_list[i])
    # download chrome driver file

    # our domian name
    driver.get(f'{url_list[i]}')
    driver.maximize_window()
    driver.implicitly_wait(1000)
    page_popup_close = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/a").click()
    time.sleep(5)
    maker_tab_click = driver.find_element(By.XPATH, "//*[@id='__next']/div[2]/div[2]/div/div[3]/a").click()
    driver.implicitly_wait(10)
    maker_info = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[3]/main/div[2]")
    text = maker_info.text
    print("text_variable",text)
    maker_designation_info.append(text)
    
print("output",maker_designation_info)
df = pd.read_excel('./txxxxt/ProducthuntProduct.xlsx')

# print(df)
df["Makers Information"] = maker_designation_info
# df.to_excel("ProducthuntProduct.xlsx", index=False)
df.to_excel('./txxxxt/ProducthuntProduct.xlsx', index=False)

print("file written now")
# a = maker_info.find_elements(By.XPATH,"//a[@href]")
# b = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[3]/main/div[2]")
# c = b.find_element(By.TAG_NAME,"a")
# d = c.get_attribute("href")
# print("url of makers",d)
# profile_url = maker_info.get_attribute("href")
# print("href>>>>",profile_url)
# text = maker_info.text
# list = []
# for href in a:
#     # print(href)
#     profile_url = href.get_attribute("href")
#     print(">>>>>>",profile_url)


    

   
