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
driver = webdriver.Chrome(service=service,chrome_options=option1,options=option1)
# options=option1 service=service
df = pd.read_excel("./txxxxt/ProducthuntProductCopy.xlsx",sheet_name="Sheet1")
# print(df)
url = df["Url"]
url_list =  [ product for product in url ]
# print("url_listtt",len(url_list),type(url_list))
result_list = []
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
    a = maker_info.find_elements(By.TAG_NAME,"a")
    list_comphrension = [href.get_attribute("href") for href in a]
    # print("list_comphrension",list_comphrension)
    list1 =list(dict.fromkeys(list_comphrension))
    # result_list.append(list1)
    # print("list>>>>",list1)
    var = [ prof_url for prof_url in list1 if prof_url.startswith("https://www.producthunt.com/@")]
    print("var",var)
    combinee_url_one = ", ".join(var)
    result_list.append(combinee_url_one)
# single_list = [ j for j in result_list[0]]
print("result_list",len(result_list),result_list)

# df = pd.read_excel('./txxxxt/ProducthuntProductCopy.xlsx')
# # print(df)
# df["Profile_Url"] = result_list
# df.to_excel('./txxxxt/ProducthuntProductCopy.xlsx', index=False)










    

   
