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
# options=option1
df = pd.read_excel("./txxxxt/ProducthuntProductCopy.xlsx",sheet_name="Sheet1")
# service=service
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
# # df.to_excel("ProducthuntProduct.xlsx", index=False)
# df.to_excel('./txxxxt/ProducthuntProductCopy.xlsx', index=False)
# print("single_list",single_list)
    # remove_dup = list(dict.fromkeys(prof_url)) 
    # result_list2.append(prof_url)
# print("(result_list",result_list2)
# final_list = list(dict.fromkeys(result_list2)) 
# print("final_list",final_list)
# one_product_all_makers =[final_list] 
# print(one_product_all_makers,"one_product_all_makers")
    # mylist = ["a", "b", "a", "c", "c"]
# mylist = list(dict.fromkeys(mylist))
# print(mylist)
# for href in a:
#     # print(href)
#     profile_url = href.get_attribute("href")
#     print(">>>>>>",profile_url)
#     list1.append(profile_url)
    # list1 =list(dict.fromkeys(list1))
    # print("list>>>>",list1)
#     for prof_url in list1:
#         if prof_url.startswith("https://www.producthunt.com/@"):
#             print(result_list.append(prof_url))
# print("result_list",result_list)
    
# text = maker_info.text
# print("text_variable",text)
# maker_designation_info.append(text)

    
# print("output",maker_designation_info)
# df = pd.read_excel('./txxxxt/ProducthuntProduct.xlsx')

# # print(df)
# df["All_Makers_Url"] = result_list
# # df.to_excel("ProducthuntProduct.xlsx", index=False)
# df.to_excel('./txxxxt/ProducthuntProduct.xlsx', index=False)

# print("file written now")
# a = maker_info.find_elements(By.XPATH,"//a[@href]")
# b = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div[3]/main/div[2]")
# c = b.find_element(By.TAG_NAME,"a")
# d = c.get_attribute("href")
# print("url of makers",d)

# text = maker_info.text
# list = []
# for href in a:
#     # print(href)
#     profile_url = href.get_attribute("href")
#     print(">>>>>>",profile_url)


    

   
