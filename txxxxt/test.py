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


def processing_data_web():
    option1 = Options()
    option1.headless = True
    option1.add_argument("--disable-notifications")
    service = Service("E:/selenium/chromedriver.exe")
    driver = webdriver.Chrome(service=service,chrome_options=option1,options=option1)
    fd = pd.read_excel("./txxxxt/Producthunt_all_url.xlsx",sheet_name="Sheet1")
    fd_url = fd["All_Urls"] 
    fd_url_list =[ pro_info_url_all for pro_info_url_all in fd_url ] 
    # print(">>>>>>>>>",fd_url_list)
    fd_list = []
    list1  = []
    for i in range(0,210):
      print(i)
        # print(url_list[i])
        # download chrome driver file
        # our domian name
      driver.get(f'{fd_url_list[i]}')    
      driver.maximize_window()
      driver.implicitly_wait(1000)
    #   name = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div/header/div/div[2]/h1")
    #   name_of_person = name.text
    #   print("name_of_person",name_of_person)
    #   desgination = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div/header/div/div[2]/div[1]")
    #   desgination_value = desgination.text
    #   print("desgination_value=",desgination_value)
    #   hashtag = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div/header/div/div[2]/div[2]/div[1]")
    #   hashtag_value = hashtag.text
    #   print("hashtag_value",hashtag_value)
    #   followers = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div/header/div/div[2]/div[2]/div[2]/a[1]")
    #   followers_value = followers.text
    #   print("followers_value",followers_value)
    #   following = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div/header/div/div[2]/div[2]/div[2]/a[2]")
    #   following_value = following.text
    #   print("following_value",following_value)
      twitter_name =driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/main/div[1]/div[1]") 
      twitter_name_value = twitter_name.text
      twitter_name_value.replace("Twitter","")
      link = twitter_name_value
      print("$$$",link)
      print("twitter_name",twitter_name_value)
      dict  ={

      }
    #   dict["Name"] = name_of_person 
    #   dict["Desgination"] =  desgination_value 
    #   dict["Hashtag_value"] = hashtag_value
    #   dict["Followers_value"] =  followers_value
    #   dict["Following_value"] =    following_value
    #   dict["Twitter Url"] =  ""
    #   dict["Linkedin Url"] = ""
      

      if "LINKS" in link:
          print("pass")
          div_tag = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/main/div[1]/div[1]")
          anchor_tag = div_tag.find_elements(By.TAG_NAME,"a")
          coll_links = [href.get_attribute("href") for href in anchor_tag ]
          filter_value = coll_links
          print("filter_value",filter_value)
          list_compre1 = [ i for i in filter_value if (i.startswith("https://twitter.com/") or i.startswith("https://www.linkedin.com/")  )]
          list_compre1.sort()
          print("list_compre1",list_compre1)
          list2 = [ i for i in list_compre1 if i.startswith("https://twitter.com/")]
          print("list2",list2)
          list3 = [ j for j in list_compre1 if (j.startswith("https://www.linkedin.com/"))]
          print("list3",list3)
          # list4 = [ k for k in list_compre1 if (k.startswith("https://www.") or k.startswith("https://") or k.startswith("http://") or k.startswith("http://www."))]
          # print("list4",list4)
          # list_compre1.sort(reverse=True)
          # sorted_value = [list_compre1,list_compre1,list_compre1]
          # list1.append(list_compre1)
          for j in list_compre1:
              print("for loop")
              if (len(list_compre1)) >= 2:
                   dict["Twitter Url"] = list_compre1[0]
                   dict["Linkedin Url"] = list_compre1[1]
              elif j.startswith("https://twitter.com/"):
                dict["Twitter Url"] = list_compre1[0]
           
              elif j.startswith("https://www.linkedin.com/"):
                dict["Linkedin Url"] = list_compre1[0]
              list1.append(dict)
              print("lennnnnncheck",len(list1))







          #          if j.startswith("https://www.linkedin.com/"):
          #             dict["Linkedin Url"] = list_compre1[1]
          #          else:
          #             dict["Linkedin Url"] = ""
          #          if j.startswith("https://www.") or j.startswith("https://") or j.startswith("http://") or j.startswith("http://www."):
          #             dict["Website Url"] = list_compre1[2]
          #          else:
          #             dict["Website Url"] = ""
              

              # elif  j.startswith("https://twitter.com/") or  j.startswith("https://www.linkedin.com/"):
              #      dict["Twitter Url"] = list_compre1[0]
              #      dict["Website Url"] = ""
              #      dict["Linkedin Url"] = list_compre1[1]
              # elif  j.startswith("https://www.linkedin.com/") and j.startswith("https://www.") or j.startswith("https://") or j.startswith("http://"):
              #      dict["Twitter Url"] = ""
              #      dict["Website Url"] = list_compre1[1]
              #      dict["Linkedin Url"] = list_compre1[0]
              # elif j.startswith("https://twitter.com/") and j.startswith("https://www.") or j.startswith("https://") or j.startswith("http://"):
              #      dict["Twitter Url"] = list_compre1[0]
              #      dict["Website Url"] = list_compre1[1]
              #      dict["Linkedin Url"] = ""

      


          # list_compre2 = [i for i in filter_value if i.startswith("https://www.")]
          # print(list_compre2)
          # print("filter_value",filter_value)
          # print("coll_links",coll_links)
          # dict["Twitter Url"] =  list_compre1[0] 
          # dict["Website Url"] = list_compre1[1] 
          # print("dicti",dict)
          # dict["Website Url"] = filter_value[1]
          # dict["Website Url"] =    following_value


      else:
          list1.append(dict)
          print("lennnnnnnn****",len(list1))

          # dict["Twitter Url"] = ""
          # div_tag = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/main/div[1]/div[1]")
          # anchor_tag = div_tag.find_elements(By.TAG_NAME,"a")
          # coll_links = [href.get_attribute("href") for href in anchor_tag ]
          # filter_value = coll_links
          # list_compre2 = [j for j in filter_value if j.startswith("https://www.")]
          # print(list_compre2)
          # dict["Website Url"] = list_compre2[0] 
          # dict["Twitter Url"] =  ""
          print("fail")
    print("dict",dict)
    print("listtttttttttt",list1)
    print(len(list1))
        # fd_maker_info_header = driver.find_element(By.XPATH,"//*[@id='__next']/div[2]/div/header/div[1]/div/div")
        # fd_maker_info_about_info = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]")
        # fd_text1 = fd_maker_info_header.text
        # print("fd_text1",fd_text1)
        # fd_text2 = fd_maker_info_about_info.text
        # print("fd_text2",fd_text2)
        # both_header_about_info = fd_text1 + " " + fd_text2 
        # remove_slashes_str = both_header_about_info.replace("\n"," ")
        # print(both_header_about_info)
        # fd_list.append(remove_slashes_str)
    # print("$$$$$????fd_list",fd_list)  
    df = pd.read_excel('./txxxxt/Producthunt_all_url_backup.xlsx')
    print(df)
    df["Profile Information dict"] = list1
    df.to_excel('./txxxxt/Producthunt_all_url_backup.xlsx', index=False)
    print("file_written_now")
    # listen
    # convert to json file 1
    # convert to json file 2
# processing_data_web()
# product_hunt()