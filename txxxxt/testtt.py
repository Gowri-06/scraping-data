import json
# import requests
# import urllib.request as requests
import pandas as pd


with open("D:/git/office/txxxxt/crunch_saas_backup.json", mode='r', encoding='UTF-8') as f:
    print(f)
    json_data = json.load(f)
    # print(json_data)
    x = range(213)
    # print(x)
    data  =[["xxx","uyyy"]]
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    list10 = []
    list11 = []
    list12 = []
    list13 = []
    list14 = []
    list15 = []
    list16 = []
    list17 = []
    list18 = []
    list19 = []

    for i in x:
        #  print(i)
         organization_1 = json_data["ent"][i]["Organization"]
        #  print(organization_1)
         list1.append(organization_1)
        #  a = {"one":organization_1}
        #  print(list1)
         about_2 = json_data["ent"][i]["About"]
        #  b = {"two":about_2}
        #  sp_list = [a["one"],b["two"]]
        #  print("sp_list00",sp_list,type(sp_list))
        #  data.append(sp_list)
        #  print("dta..........",data)
        #  print(about_2)
         list2.append(about_2)
        #  print(a,b)
         location_3 = json_data["ent"][i]["Location"]
        #  print(location_3)
         list3.append(location_3)
         employees_4 = json_data["ent"][i]["Employees"]
        #  print(employees_4)
         list4.append(employees_4)
         funding_5 = json_data["ent"][i]["Funding"] 
        #  print(funding_5)
         list5.append(funding_5)
         ownership_6 = json_data["ent"][i]["Ownership"]
        #  print(ownership_6)
         list6.append(ownership_6)
         website_7  = json_data["ent"][i]["Website"]
        #  print(website_7)
         list7.append(website_7)
         rank_8 = json_data["ent"][i]["Rank"]
        #  print(rank_8)
         list8.append(rank_8)
         industries_9 = json_data["ent"][i]["Details"]["Industries"]
        #  print(industries_9)
         list9.append(industries_9)
         headquaters_10 = json_data["ent"][i]["Details"]["Headquarters Regions"]
        #  print(headquaters_10)
         list10.append(headquaters_10)
         founded_date_11 = json_data["ent"][i]["Details"]["Founded Date"]
        #  print(founded_date_11)
         list11.append(founded_date_11)
         founders_12 = json_data["ent"][i]["Details"]["Founders"]
        #  print(founders_12)
         list12.append(founders_12)
         operating_status_13 = json_data["ent"][i]["Details"]["Operating Status"]
        #  print(operating_status_13)
         list13.append(operating_status_13)
         also_known_as_14 = json_data["ent"][i]["Details"]["Also Known As"]
        #  print(also_known_as_14)
         list14.append(also_known_as_14)
         legal_name_15 = json_data["ent"][i]["Details"]["Legal Name"]
        #  print(legal_name_15)
         list15.append(legal_name_15)
         last_funding_type_16 = json_data["ent"][i]["Details"]["Last Funding Type"]
        #  print(last_funding_type_16)
         list16.append(last_funding_type_16)
         company_type_17 = json_data["ent"][i]["Details"]["Company Type"]
        #  print(company_type_17)
         list17.append(company_type_17)
         contact_email_18 = json_data["ent"][i]["Details"]["Contact Email"]
        #  print(contact_email_18)
         list18.append(contact_email_18)
         phone_number_19 = json_data["ent"][i]["Details"]["Phone Number"]
        #  print(phone_number_19)
         list19.append(phone_number_19)
        #  keys_values = json_data["ent"][0]
        #  keys_values1 = json_data["ent"][0]["Details"]
        #  get_keys = list(keys_values.keys())
        #  get_keys1 = list(keys_values1.keys())
        #  print("*****aaaaaaaaaaaaa",get_keys)
        #  print("*****bbbbbbbbbbbbb",get_keys1)
        #  a = {
              
        #      'Organization':organization_1, 
        #       'About':about_2,
        #       'Location':location_3,
        #       'Employees':employees_4,
        #       'Funding':funding_5,
        #       'Ownership':ownership_6,
        #       'Website':website_7,
        #       'Rank':rank_8,
        #       'Industries':industries_9,
        #       'Headquarters Regions':headquaters_10,
        #       'Founded Date':founded_date_11,
        #       'Founders':founders_12,
        #       'Operating Status':operating_status_13,
        #       'Also Known As':also_known_as_14,
        #       'Legal Name':legal_name_15,
        #       'Last Funding Type':last_funding_type_16,
        #       'Company Type':company_type_17,
        #       'Contact Email':contact_email_18,
        #       'Phone Number':phone_number_19

        #        }
               
    #      var1 = [a["Organization"],a["About"]]
    #      print("var100",var1)
    #      data.append(var1)
    # print("dataaaa****",data)


    # company_name = json_data["entities"][0]["properties"]["identifier"]["permalink"]
    # company_name2 = json_data["entities"][1]["properties"]["identifier"]["permalink"]
    # print(company_name)
    # json_str = json.dumps(company_name2, indent=2)
    # print(json_str)
    # x = range(235)
    # row1 = []
    # row2 = []
    # for i in x:
    # print("ii>>",i)
    # all_company_name = json_data["entities"][i]["properties"]["identifier"]["permalink"]
    # print(">>>",all_company_name)
    # all_company_urls = 'https://www.crunchbase.com/organization/' + all_company_name
    # print("<<<",all_company_urls)
    # row1.append(all_company_name)
    # row2.append(all_company_urls)
    df = pd.DataFrame({
        "Organization":list1,
        "About":list2,
        "Location":list3,
        "Employees":list4,
        "Funding":list5,
        "Ownership":list6,
        "Website":list7,
        "Rank":list8,
        "Industries":list9,
        "Headquarters Regions":list10,
        "Founded Date":list11,
        "Founders":list12,
        "Operating Status":list13,
        "Also Known As":list14,
        "Legal name":list15,
        "Last Funding Type":list16,
        "Company Type ":list17,
        "Contact Email":list18,
        "Phone Number":list19

                                       })
    print(df)
    df.to_excel("CrunchbaseLeadsexcel.xlsx", index=False)
    print("file written now")
# print(row1)
# print(row2)
# r = requests.get('https://api.github.com/users/naveenkrnl')
# response = requests.urlopen('https://www.crunchbase.com/organization/gloc-al')
# response1 = response.read()
# print(response1)
# print(r.content)
