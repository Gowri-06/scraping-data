import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
import pandas as pd
import json
from dotenv import load_dotenv
import os

def product_hunt(): 

    # Load environment variables from the .env file
    load_dotenv()

    # Access environment variables as regular variables
    token = os.getenv("ACCESS_TOKEN")
    print(token)
    start_of_year = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
    print("start_of_year",start_of_year)
    iso_format=start_of_year.isoformat()
    print("iso to use",type(iso_format),iso_format)
    # Define the GraphQL query
  
    # after: "MjA"
    # user
    # userId
    # slug
    # productLinks
    query = """
      query {
        posts(postedAfter: "2023-01-01", postedBefore: "2023-01-31", order: RANKING,after: "ODA") {
          edges {
            node {
              id
              name
              tagline
              url
              votesCount
            }
           }
         pageInfo {
            hasNextPage
            endCursor
          }
        }
      }
    """
    # query = """
    #   query {
    #     posts(postedAfter: "2023-01-01", postedBefore: "2023-01-31", order: RANKING,after: "ODA") {
    #       edges {
    #         node {
    #           id
    #           createdAt
    #           slug
    #           makers {
    #           coverImage
    #           id 
    #           name
    #           websiteUrl
    #           username
    #           isMaker
    #           isViewer
    #           profileImage
    #           twitterUsername
    #           url
    #           }
    #           productLinks{
    #           type
    #           url
    #           }
    #           userId
    #           name
    #           tagline
    #           url
    #           votesCount
    #           website
    #           commentsCount
    #           description
    #           user {
    #           id
    #           name 
    #           username
    #           websiteUrl
    #           coverImage
    #           createdAt 
    #           headline
    #           isMaker
    #           isViewer
    #           profileImage 
    #           twitterUsername
    #           url
    #           }
    #           featuredAt 
    #           isCollected
    #           isVoted
    #           media {
    #           videoUrl
    #           url
    #           }
    #           reviewsCount
    #           reviewsRating
    #           thumbnail {
    #           videoUrl
    #           url
    #           }
    #         }
    #        }
    #      pageInfo {
    #         hasNextPage
    #         endCursor
    #       }
    #     }
    #   }
    # """


    # Set up the API request headers and parameters
    url = 'https://api.producthunt.com/v2/api/graphql'

    headers = {
        "Authorization": f'Bearer {token}',
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Host": "api.producthunt.com"

    }
    json = {'query': query}

    # Make the API request
    response = requests.post(url, headers=headers, json=json)
    print("200staatus",response)
    print("dataa and cursor key",response.json())
    data = response.json()['data']['posts']['edges']
    size = len(data) 
    print("?????count",size)
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    id_1 = data ['node']["id"]
    name_2=data ['node']["name"] 
    tagline_3=data ['node']["tagline"]
    url_4=data ['node']["url"]
    votesCount_5=data ['node']["votesCount"]
    list1.append(id_1)
    list2.append(name_2)
    list3.append(tagline_3)
    list4.append(url_4)
    list5.append(votesCount_5)

    df = pd.DataFrame({
            "Id":list1,
             "Name":list2,
           "Tagline":list3,
             "Url":list4,
            "Votescount":list5,


                                           })
    df.to_excel("Producthuntsecond.xlsx", index=False)
    # print(df)
    # print("file written now")
    # df_old = pd.read_excel('Producthuntsecond.xlsx')
    # df_new = pd.concat([df_old,df], ignore_index=True)
    # df_new.to_excel('Producthuntsecond.xlsx', index=False)

    option1 = Options()
    option1.headless = True
    option1.add_argument("--disable-notifications")
    service = Service("E:/selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=service,chrome_options=option1,options=option1)
    # options=option1 service=service
    df = pd.read_excel("./txxxxt/ProducthuntSecond.xlsx",sheet_name="Sheet1") 
    # print(df)
    url = df["Url"]
    id_list= df["Id"]
    only_id_list = []
    url_list =  [ product for product in url ]
    # print("url_listtt",len(url_list),type(url_list))
    result_list = []
    combined_url_list = []
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
        combinee_url_one = ", ".join(var)
        combined_url_list.append(combinee_url_one)
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
    df = pd.DataFrame({
            "All_Urls":lists_into_one,
          


                                           })
    df.to_excel('./txxxxt/ProducthuntSecondData.xlsx', index=False)
    # print(df)
    df = pd.read_excel('./txxxxt/ProducthuntSecondData.xlsx')
    df["Id Reference"] = lists_into_two 
    # this is in a first excel sheet
    df = pd.read_excel('./txxxxt/ProducthuntSecond.xlsx')
    df["Profile_Url"] = combined_url_list
    print("file written")
    # pass
    # profile_info_url_info_text
    #take json file 1


    fd = pd.read_excel("./txxxxt/ProducthuntSecondData.xlsx",sheet_name="Sheet1")
    fd_url = fd["All_Urls"] 
    fd_url_list =[ pro_info_url_all for pro_info_url_all in fd_url ] 
    print(">>>>>>>>>",fd_url_list)
    fd_list = []
    for i in range(0,210):
        print(i)
        # print(url_list[i])
        # download chrome driver file
        # our domian name
        driver.get(f'{fd_url_list[i]}')    
        driver.maximize_window()
        driver.implicitly_wait(1000)
        fd_maker_info_header = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div")
        fd_maker_info_about_info = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]")
        fd_text1 = fd_maker_info_header.text
        print("fd_text1",fd_text1)
        fd_text2 = fd_maker_info_about_info.text
        print("fd_text2",fd_text2)
        both_header_about_info = f'{fd_url_list[i]}' + " " + fd_text1 + " " + fd_text2 
        remove_slashes_str = both_header_about_info.replace("\n"," ")
        print(both_header_about_info)
        fd_list.append(remove_slashes_str)
    print("$$$$$????fd_list",fd_list)  
    df = pd.read_excel('./txxxxt/ProducthuntSecondData.xlsx')
    # print(df)
    df["Profile Information"] = fd_list
    # df.to_excel('./txxxxt/Producthunt_all_url.xlsx', index=False)
    print("file_written_now")
    # listen
    # convert to json file 1
    # convert to json file 2
# product_hunt()

def combine_json():
    # take the json file for profile information and id reference !important
    # Open and read the JSON file
    with open('content3.json') as f:
        dict_list = json.load(f)
    list = []
    list2 = []
    #list Print the Python object
    print("data",dict_list)
    lists_of_dicts = []
    ids_added = {}

    for d in dict_list:
        id_val = d['Id Reference']
        print("id_val",id_val)
        if id_val not in ids_added:
            ids_added[id_val] = len(lists_of_dicts)
            lists_of_dicts.append([d])
        else:
            lists_of_dicts[ids_added[id_val]].append(d)

    print("lists_of_dicts",lists_of_dicts)
    # convert this value in to json file 2


   # json file 1
    with open("content2.json", "r") as f1:
        data1 = json.load(f1)
        print("data><><>",len(data1))
        for i in data1:
            print("data111",len(data1))
            i["Information"] = ""
        # print("add_information",data1)
    with open('writedata.json', 'w') as json_file:
        json.dump(data1,json_file)
    
    ##################
    # json file 1 and json file 2
    import json

    # Load the first JSON file
    with open('file1.json', 'r') as f1:
        data1 = json.load(f1)

    # Load the second JSON file
    with open('file2.json', 'r') as f2:
        data2 = json.load(f2)

    # Combine the two objects as desired (in this example, we concatenate two lists)
    combined_data_file = data1 + data2

    # Write the combined data to a new file
    with open('combined.json', 'w') as fout:
        json.dump(combined_data_file, fout)

    # after combined json use it in a json studio 
    ##################
    final_json = [{},{}]

    with open('final.json', 'w') as fout:
        json.dump(final_json, fout)

# combine_json()

    

   
