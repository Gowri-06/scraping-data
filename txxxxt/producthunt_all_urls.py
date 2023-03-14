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
id_list= df["Id"]
only_id_list = []
url_list =  [ product for product in url ]
# print("url_listtt",len(url_list),type(url_list))
result_list = []
# id_value = []
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
    var = [ prof_url for prof_url in list1 if prof_url.startswith("https://www.producthunt.com/@") ]
    # print("var",var)
    id_var = "id=" + str(id_list[i])
    var2 = [ f'{prof_url}{id_var}' for prof_url in list1 if prof_url.startswith("https://www.producthunt.com/@")]
    # print("var2",var2)
    my_list = [k[-9:] for k in var2]
    # print("my_list",my_list)
    only_id_list.append(my_list)
    # combinee_url_one = ", ".join(var)
    result_list.append(var)
    # id_value.append(var2)
print("only_id_list",only_id_list)
# print("id_value",id_value)
# single_list = [ j for j in result_list[0]]
# print("result_list",len(result_list),result_list) 
lists_into_one = [ item for sublist in result_list for item in sublist] 
# print("lists_into_one",lists_into_one)
lists_into_two = [ item2 for sublist2 in only_id_list for item2 in sublist2] 
# print("lists_into_two",lists_into_two)

df = pd.read_excel('./txxxxt/Producthunt_all_url.xlsx')

# print(df)
df["Id Reference"] = lists_into_two 
# df.to_excel("ProducthuntProduct.xlsx", index=False)

df.to_excel('./txxxxt/Producthunt_all_url.xlsx', index=False)
# pass
# profile_info_url_info_text



# fd = pd.read_excel("./txxxxt/Producthunt_all_url.xlsx",sheet_name="Sheet1")
# fd_url = fd["All_Urls"] 
# fd_url_list =[ pro_info_url_all for pro_info_url_all in fd_url ] 
# print(">>>>>>>>>",fd_url_list)
# fd_list = []
# for i in range(0,210):
#     print(i)
#     # print(url_list[i])
#     # download chrome driver file
#     # our domian name
#     driver.get(f'{fd_url_list[i]}')    
#     driver.maximize_window()
#     driver.implicitly_wait(1000)
#     fd_maker_info_header = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div")
#     fd_maker_info_about_info = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]")
#     fd_text1 = fd_maker_info_header.text
#     print("fd_text1",fd_text1)
#     fd_text2 = fd_maker_info_about_info.text
#     print("fd_text2",fd_text2)
#     both_header_about_info = f'{fd_url_list[i]}' + " "+ fd_text1 + " " + fd_text2 
#     remove_slashes_str = both_header_about_info.replace("\n"," ")
#     print(both_header_about_info)
#     fd_list.append(remove_slashes_str)
# print("$$$$$????fd_list",fd_list)  
# # df = pd.read_excel('./txxxxt/Producthunt_all_url.xlsx')
# # # print(df)
# # df["Profile Information"] = fd_list
# # df.to_excel('./txxxxt/Producthunt_all_url.xlsx', index=False)
# # print("file_written_now")

# # Load the Excel file into a pandas DataFrame
# excel_file = pd.read_excel('./txxxxt/ProducthuntProductCopy.xlsx')

# # Convert the DataFrame to a JSON string
# json_string = excel_file.to_json(orient='records')

# # Save the JSON string to a file
# with open('content2.json', 'w') as json_file:
#     json_file.write(json_string)




    

   
