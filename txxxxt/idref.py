# take the json file for profile information and id reference !important
import json 
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
# convert this value in to json
##################
# Now combine both json to get final  json output 
##################


# import pandas as pd
# # Load the Excel file into a pandas DataFrame
# excel_file = pd.read_excel('./txxxxt/Producthunt_all_url.xlsx')

# # Convert the DataFrame to a JSON string
# json_string = excel_file.to_json(orient='records')

# # Save the JSON string to a file
# with open('content3.json', 'w') as json_file:
#     json_file.write(json_string)

# Open the first input file and load its contents
# import json reference code
# dict_list = [
#     {'id': 1, 'name': 'John'},
#     {'id': 2, 'name': 'Alice'},
#     {'id': 3, 'name': 'Bob'},
#     {'id': 2, 'name': 'Charlie'},
#     {'id': 1, 'name': 'Kate'},
#     {'id': 4, 'name': 'David'},
#     {'id': 3, 'name': 'Mary'}
# ]

# lists_of_dicts = []
# ids_added = {}

# for d in dict_list:
#     id_val = d['id']
#     if id_val not in ids_added:
#         ids_added[id_val] = len(lists_of_dicts)
#         lists_of_dicts.append([d])
#     else:
#         lists_of_dicts[ids_added[id_val]].append(d)
        
# print(lists_of_dicts)

# # list = []
# with open("content2.json", "r") as f1:
#     data1 = json.load(f1)
#     print("data><><>",len(data1))
#     for i in data1:
#         print("data111",len(data1))
#         i["Information"] = ""
#     # print("add_information",data1)
# with open('writedata.json', 'w') as json_file:
#     json.dump(data1,json_file)
        # list.append(i)
        # pass
# print("json_file1",list)
# Open the second input file and load its contents
# with open("writedata.json", "r") as f1:
#     data1 = json.load(f1)
#     print("data2",len(data1))
# with open("output_file.json", "r") as f2:
#     data2 = json.load(f2)
#     print("data2",len(data2))
# # Combine the two objects as desired (in this example, we concatenate two lists)
# combined_data = data1 + data2
import json
final_json = [
    {
        "Id": 375989,
        "Name": "Live Video Calling SDK by Dyte",
        "Tagline": "Integrate into your product within minutes",
        "Url": "https://www.producthunt.com/posts/live-video-calling-sdk-by-dyte?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 1022,
        "Profile_Url": "https://www.producthunt.com/@abhishek_kankani, https://www.producthunt.com/@palash_golecha, https://www.producthunt.com/@kushagra_vaish",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@abhishek_kankani",
            "Profile Information": "https://www.producthunt.com/@abhishek_kankani Abhishek Kankani CEO & Co-founder @Dyte #3253855 45 followers 18 following 200 points Follow BADGES Top Product MAKER HISTORY Dyte Video SDK Integrate live video calling into your product within minutes Jan 2023 🎉 Joined Product Hunt March 2nd, 2021 Report",
            "Id Reference": "id=375989"
        },
        {
            "All_Urls": "https://www.producthunt.com/@palash_golecha",
            "Profile Information": "https://www.producthunt.com/@palash_golecha Palash Golecha Co-founder dyte.io #3640660 23 followers 7 following 104 points Follow BADGES Top Product MAKER HISTORY Dyte Video SDK Integrate live video calling into your product within minutes Jan 2023 🎉 Joined Product Hunt August 17th, 2021 Report",
            "Id Reference": "id=375989"
        },
        {
            "All_Urls": "https://www.producthunt.com/@kushagra_vaish",
            "Profile Information": "https://www.producthunt.com/@kushagra_vaish Kushagra Vaish Maker and reluctant leader #3102152 27 followers 0 following 103 points Follow BADGES Top Product MAKER HISTORY Dyte Video SDK Integrate live video calling into your product within minutes Jan 2023 🎉 Joined Product Hunt January 5th, 2021 Report",
            "Id Reference": "id=375989"
        }
    ]
    },
    {
        "Id": 377157,
        "Name": "LINER AI",
        "Tagline": "A trustworthy ChatGPT search assistant",
        "Url": "https://www.producthunt.com/posts/liner-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 466,
        "Profile_Url": "https://www.producthunt.com/@brianwoo, https://www.producthunt.com/@jinukim21, https://www.producthunt.com/@jinukim, https://www.producthunt.com/@sungmoon, https://www.producthunt.com/@mynhpark",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@brianwoo",
            "Profile Information": "https://www.producthunt.com/@brianwoo Brian Woo #3630467 285 followers 97 following 1,426 points Follow LINKS Twitter BADGES 7 Top Product Veteran View all badges MAKER HISTORY LINER Highlight while you read LINER AI Jan 2023 Improved Google Search by LINER Dec 2020 LINER Home Aug 2020 LINER Browser Extension Aug 2019 LINER 5 Aug 2018 Highlighting API made by LINER Nov 2017 LINER for Safari May 2017 LINER for Pocket Mar 2017 LINER for iOS Jan 2017 Liner Jul 2015 Google Search Scanner by LINER Filter out irrelevant search results and save your time Dec 2021 LINER for Slack Inspire your team by sharing key quotes to Slack with LINER Aug 2021 Centro 365 V2 Make the admin of Microsoft 365 just that little bit easier Feb 2020 LINER for Samsung First official Android app exclusive on Samsung Galaxy Apps Nov 2018 View more Report",
            "Id Reference": "id=377157"
        },
        {
            "All_Urls": "https://www.producthunt.com/@jinukim21",
            "Profile Information": "https://www.producthunt.com/@jinukim21 Jinu Kim LINER CEO #247375 87 followers 10 following 1,457 points Follow LINKS Website Twitter INTERESTS Productivity API BADGES 6 Top Product Veteran MAKER HISTORY LINER Highlight while you read LINER AI Jan 2023 Improved Google Search by LINER Dec 2020 LINER Home Aug 2020 LINER Browser Extension Aug 2019 LINER 5 Aug 2018 Highlighting API made by LINER Nov 2017 LINER for Safari May 2017 LINER for Pocket Mar 2017 LINER for iOS Jan 2017 Liner Jul 2015 Centro 365 V2 Make the admin of Microsoft 365 just that little bit easier Feb 2020 LINER for Samsung First official Android app exclusive on Samsung Galaxy Apps Nov 2018 FirefoxPWA Tool to install, manage and use Web Apps in Mozilla Firefox Jun 2017 LINER for Chrome Highlight everything! From Wikipedia to PDF files Jul 2016 🎉 Joined Product Hunt June 15th, 2015 Report",
            "Id Reference": "id=377157"
        },
        {
            "All_Urls": "https://www.producthunt.com/@jinukim",
            "Profile Information": "https://www.producthunt.com/@jinukim Jinu Kim #1545376 8 followers 0 following 54 points Follow BADGES Top Product MAKER HISTORY Google Search Scanner by LINER Filter out irrelevant search results and save your time Dec 2021 LINER for Slack Inspire your team by sharing key quotes to Slack with LINER Aug 2021 LINER Highlight while you read Aug 2021 🎉 Joined Product Hunt November 28th, 2018 Report",
            "Id Reference": "id=377157"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sungmoon",
            "Profile Information": "https://www.producthunt.com/@sungmoon Sung Cho #23565 843 followers 33 following 185 points Follow LINKS Twitter Website BADGES Top Product Veteran MAKER HISTORY LINER Highlight while you read Highlighting API made by LINER Nov 2017 LINER for Safari May 2017 Liner Jul 2015 FirefoxPWA Tool to install, manage and use Web Apps in Mozilla Firefox Jun 2017 🎉 Joined Product Hunt July 1st, 2014 Report",
            "Id Reference": "id=377157"
        },
        {
            "All_Urls": "https://www.producthunt.com/@mynhpark",
            "Profile Information": "https://www.producthunt.com/@mynhpark Min Park https://nexybit.com #473726 119 followers 14 following 1,119 points Follow LINKS Website Twitter INTERESTS Productivity Home Writing Marketing BADGES 3 Top Product Veteran MAKER HISTORY Nexybit Trade Mining and Futures Exchange. May 2019 LINER Highlight while you read LINER for Pocket Mar 2017 LINER for iOS Jan 2017 LINER for Chrome Highlight everything! From Wikipedia to PDF files Jul 2016 🎉 Joined Product Hunt February 28th, 2016 Report",
            "Id Reference": "id=377157"
        }
    ]
    },
    {
        "Id": 376810,
        "Name": "Getgud.io",
        "Tagline": "Making online games toxic free",
        "Url": "https://www.producthunt.com/posts/getgud-io?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 370,
        "Profile_Url": "https://www.producthunt.com/@artkulakov, https://www.producthunt.com/@guykroupp",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@artkulakov",
            "Profile Information": "https://www.producthunt.com/@artkulakov Art Kulakov ML Lead, B2B gaming startup founder #4950832 51 followers 1 following 203 points Follow LINKS Medium Twitter Linkedin INTERESTS Health & Fitness Productivity Indie Games Artificial Intelligence Tech Games Data & Analytics Finance Data Science Data Visualization BADGES Gemologist 2 Top Product MAKER HISTORY Getgud.io Making online games toxic free! Jan 2023 Zenen Imagine ChatGPT and Siri had a baby. That's Zenen. Jan 2023 VoiceType Write Your Entire Email From Short Voice Prompt Jan 2023 100+ AI Prompts A collection of ChatGPT, MidJourney, Dalle2 prompts Jan 2023 🎉 Joined Product Hunt December 24th, 2022 Report",
            "Id Reference": "id=376810"
        },
        {
            "All_Urls": "https://www.producthunt.com/@guykroupp",
            "Profile Information": "https://www.producthunt.com/@guykroupp guy kroupp Tech entrepreneur #366814 18 followers 2 following 86 points 🦄 9 day streak Follow ABOUT Love to create products that make things better LINKS Twitter BADGES 2 Top Product Veteran MAKER HISTORY Getgud.io Making online games toxic free! Jan 2023 Coralogix Solve your production problems faster. Coralogix 2.0 Jan 2017 Coralogix Dec 2015 🎉 Joined Product Hunt December 9th, 2015 Report",
            "Id Reference": "id=376810"
        }
    ]
    },
    {
        "Id": 376335,
        "Name": "littlecook",
        "Tagline": "Turn unused ingredients into delicious new dishes",
        "Url": "https://www.producthunt.com/posts/littlecook?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 251,
        "Profile_Url": "https://www.producthunt.com/@supnim, https://www.producthunt.com/@amir_bio",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@supnim",
            "Profile Information": "https://www.producthunt.com/@supnim Nimesh Founder littlecook.io ✦ ex-amazon #4228846 87 followers 90 following 112 points Follow ABOUT Product designer building products, join me on the journey. LINKS littlecook Twitter Linkedin Portfolio INTERESTS Music Fashion Cooking Software Engineering Tech UX Design BADGES Top Product MAKER HISTORY littlecook Your digital sous chef Jan 2023 🎉 Joined Product Hunt April 17th, 2022 Report",
            "Id Reference": "id=376335"
        },
        {
            "All_Urls": "https://www.producthunt.com/@amir_bio",
            "Profile Information": "https://www.producthunt.com/@amir_bio Amir Andohkosh Founder #5064271 23 followers 16 following 68 points ✨ 3 day streak Follow ABOUT Software engineer by trade, entrepreneur by destiny.  Building littlecook.io to learn and help make a difference LINKS littlecook Twitter INTERESTS Health & Fitness Productivity Growth Hacking Artificial Intelligence Tech Food & Drink BADGES Top Product MAKER HISTORY littlecook Your digital sous chef Jan 2023 🎉 Joined Product Hunt January 23rd, 2023 Report",
            "Id Reference": "id=376335"
        }
    ]
    },
    {
        "Id": 376853,
        "Name": "Terrastruct",
        "Tagline": "The diagramming tool for developers",
        "Url": "https://www.producthunt.com/posts/terrastruct-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 261,
        "Profile_Url": "https://www.producthunt.com/@alixanderwang",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@alixanderwang",
            "Profile Information": "https://www.producthunt.com/@alixanderwang Alexander Wang #1981849 98 followers 193 following 37 points ☀️ 2 day streak Follow LINKS Twitter MAKER HISTORY Terrastruct The diagramming tool for developers Terrastruct Jan 2023 Terrastruct Feb 2021 Terrastruct Jan 2020 D2 Modern diagram scripting language to turn text to diagrams Dec 2022 🎉 Joined Product Hunt July 19th, 2019 Report",
            "Id Reference": "id=376853"
        }
    ]
    },
    {
        "Id": 377091,
        "Name": "PriceWell Bubble Plugin for Stripe",
        "Tagline": "No fuss, no-code Stripe subscriptions for Bubble apps",
        "Url": "https://www.producthunt.com/posts/pricewell-bubble-plugin-for-stripe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 271,
        "Profile_Url": "https://www.producthunt.com/@matthew_reid1, https://www.producthunt.com/@new_user__0292023a0db70d1b8ed6caa",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@matthew_reid1",
            "Profile Information": "https://www.producthunt.com/@matthew_reid1 Matthew Reid Co-Founder PriceWell.io #2985088 38 followers 71 following 46 points 🌟 5 day streak Follow ABOUT 🔨 Bootstrapping PriceWell.io Helping anyone build Stripe subscriptions into their website. 10 year Full Stack Developer, Cyclist, Foodie, Dad LINKS Website INTERESTS Fintech SaaS Developer Tools Tech No-Code BADGES Gemologist View all badges MAKER HISTORY PriceWell No fuss, no-code Stripe subscriptions for Bubble apps Jan 2023 SaaS Pricing Guide 350+ SaaS companies pricing compared Apr 2021 🎉 Joined Product Hunt November 13th, 2020 Report",
            "Id Reference": "id=377091"
        },
        {
            "All_Urls": "https://www.producthunt.com/@new_user__0292023a0db70d1b8ed6caa",
            "Profile Information": "https://www.producthunt.com/@new_user__0292023a0db70d1b8ed6caa Σπυρος Κοντοπριας A storyteller #5090787 8 followers 2 following 34 points ☀️ 2 day streak Follow BADGES Gemologist MAKER HISTORY PriceWell No fuss, no-code Stripe subscriptions for Bubble apps Jan 2023 SaaS Pricing Guide 350+ SaaS companies pricing compared Apr 2021 🎉 Joined Product Hunt April 7th, 2021 Report",
            "Id Reference": "id=377091"
        }
    ]
    },
    {
        "Id": 377162,
        "Name": "ChatGPT Famous Resumes",
        "Tagline": "1000+ AI generated resumes of famous people",
        "Url": "https://www.producthunt.com/posts/chatgpt-famous-resumes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 232,
        "Profile_Url": "https://www.producthunt.com/@viktorkirilov",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@viktorkirilov",
            "Profile Information": "https://www.producthunt.com/@viktorkirilov Viktor Kirilov Software Engineer, Car Enthusiast #1723797 9 followers 1 following 93 points ☀️ 2 day streak Follow BADGES Top Product MAKER HISTORY This Resume Does Not Exist Resumes generated by a neural network ChatGPT Famous Resumes Jan 2023 This Resume Does Not Exist Mar 2019 Enhancv Our resumes get people hired at top companies Nov 2019 🎉 Joined Product Hunt March 12th, 2019 Report",
            "Id Reference": "id=377162"
        }
    ]
    },
    {
        "Id": 376934,
        "Name": "Delibr AI",
        "Tagline": "AI-assisted end-to-end product management platform",
        "Url": "https://www.producthunt.com/posts/delibr-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 272,
        "Profile_Url": "https://www.producthunt.com/@nilsjanse, https://www.producthunt.com/@andre_dantorp1, https://www.producthunt.com/@fredrika_andersson, https://www.producthunt.com/@erik_wenneborg, https://www.producthunt.com/@fbonawiede, https://www.producthunt.com/@nicole_landgraff",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@nilsjanse",
            "Profile Information": "https://www.producthunt.com/@nilsjanse Nils Janse Founder of Delibr #1913411 33 followers 22 following 88 points Follow LINKS Twitter Website INTERESTS Design Tools Productivity Task Management User Experience Growth Hacking Developer Tools BADGES Top Product MAKER HISTORY Delibr Get out of the feature factory and ship more product value Delibr AI Jan 2023 Delibr 2.0 Jan 2022 Epic Alignment Sep 2020 Delibr Jun 2019 🎉 Joined Product Hunt June 10th, 2019 Report",
            "Id Reference": "id=376934"
        },
        {
            "All_Urls": "https://www.producthunt.com/@andre_dantorp1",
            "Profile Information": "https://www.producthunt.com/@andre_dantorp1 André Dantorp Startup and tech lover #2157216 3 followers 1 following 27 points ✨ 3 day streak Follow BADGES Gemologist MAKER HISTORY Delibr Get out of the feature factory and ship more product value Jan 2023 🎉 Joined Product Hunt October 21st, 2019 Report",
            "Id Reference": "id=376934"
        },
        {
            "All_Urls": "https://www.producthunt.com/@fredrika_andersson",
            "Profile Information": "https://www.producthunt.com/@fredrika_andersson Fredrika Andersson Product designer @Delibr #4044997 14 followers 9 following 31 points Follow ABOUT We @Delibr have launched Delibr AI! Check it out: https://www.producthunt.com/posts/delibr-ai LINKS Delibr AI Launch MAKER HISTORY Delibr Get out of the feature factory and ship more product value Jan 2023 🎉 Joined Product Hunt January 31st, 2022 Report",
            "Id Reference": "id=376934"
        },
        {
            "All_Urls": "https://www.producthunt.com/@erik_wenneborg",
            "Profile Information": "https://www.producthunt.com/@erik_wenneborg Erik Wenneborg Co founder at Delibr #1919776 2 followers 0 following 43 points ☀️ 2 day streak Follow BADGES Top Product MAKER HISTORY Delibr Get out of the feature factory and ship more product value Delibr AI Jan 2023 Delibr 2.0 Jan 2022 Delibr Jun 2019 🎉 Joined Product Hunt June 13th, 2019 Report",
            "Id Reference": "id=376934"
        },
        {
            "All_Urls": "https://www.producthunt.com/@fbonawiede",
            "Profile Information": "https://www.producthunt.com/@fbonawiede Farid Bonawiede Co founder at Delibr #806283 34 followers 23 following 47 points Follow LINKS Twitter INTERESTS Web App Productivity Home Text Editors Developer Tools Tech BADGES Top Product Veteran MAKER HISTORY Delibr Get out of the feature factory and ship more product value Delibr AI Jan 2023 Delibr 2.0 Jan 2022 Delibr Jun 2019 🎉 Joined Product Hunt February 11th, 2017 Report",
            "Id Reference": "id=376934"
        },
        {
            "All_Urls": "https://www.producthunt.com/@nicole_landgraff",
            "Profile Information": "https://www.producthunt.com/@nicole_landgraff Nicole Landgraff Launching Delibr AI for Product Managers #4045032 29 followers 101 following 36 points Follow MAKER HISTORY Delibr Get out of the feature factory and ship more product value Jan 2023 🎉 Joined Product Hunt January 31st, 2022 Report",
            "Id Reference": "id=376934"
        }
    ]
    },
    {
        "Id": 377110,
        "Name": "Kayyo",
        "Tagline": "AI-powered personal MMA trainer",
        "Url": "https://www.producthunt.com/posts/kayyo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 206,
        "Profile_Url": "https://www.producthunt.com/@labibyasir, https://www.producthunt.com/@aymansaleh, https://www.producthunt.com/@tedjouc1, https://www.producthunt.com/@mohamed_jaber2, https://www.producthunt.com/@messipsa21, https://www.producthunt.com/@michaelpaik",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@labibyasir",
            "Profile Information": "https://www.producthunt.com/@labibyasir Labib Yasir Co-Founder & CEO of Kayyo #5069345 7 followers 5 following 43 points Follow ABOUT Building Kayyo. My life mission is to create a billion martial artists. INTERESTS Artificial Intelligence Tech MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 24th, 2023 Report",
            "Id Reference": "id=377110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@aymansaleh",
            "Profile Information": "https://www.producthunt.com/@aymansaleh Ayman Saleh ML Engineer, Building perception systems #5091242 0 followers 0 following 17 points Follow INTERESTS Developer Tools Artificial Intelligence MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 30th, 2023 Report",
            "Id Reference": "id=377110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@tedjouc1",
            "Profile Information": "https://www.producthunt.com/@tedjouc1 tedjouc1 Product Designer at Kayyo #5065014 0 followers 0 following 20 points ☀️ 2 day streak Follow INTERESTS Design Tools User Experience Tech MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 23rd, 2023 Report",
            "Id Reference": "id=377110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@mohamed_jaber2",
            "Profile Information": "https://www.producthunt.com/@mohamed_jaber2 Mohamed Jaber iOS Software Engineer @ Kayyo #5086282 0 followers 0 following 20 points Follow INTERESTS Developer Tools Artificial Intelligence Tech MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 28th, 2023 Report",
            "Id Reference": "id=377110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@messipsa21",
            "Profile Information": "https://www.producthunt.com/@messipsa21 Messipsa Tamazouzt software engineer #5086489 0 followers 0 following 17 points Follow MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 28th, 2023 Report",
            "Id Reference": "id=377110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@michaelpaik",
            "Profile Information": "https://www.producthunt.com/@michaelpaik Michael Paik Building Kayyo #5072246 3 followers 2 following 32 points Follow MAKER HISTORY Kayyo AI Powered Personal MMA Trainer Jan 2023 🎉 Joined Product Hunt January 24th, 2023 Report",
            "Id Reference": "id=377110"
        }
    ]
    },
    {
        "Id": 377104,
        "Name": "Femme Stock",
        "Tagline": "Beautiful, feminine Ai stock images",
        "Url": "https://www.producthunt.com/posts/femme-stock?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 160,
        "Profile_Url": "https://www.producthunt.com/@zeng",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@zeng",
            "Profile Information": "https://www.producthunt.com/@zeng Zeng Founder of FemmeStock & WhoWhatWhyAi #4432284 778 followers 69 following 1,085 points 🔥 204 day streak Follow ABOUT I am a no-code explorer and AI art enthusiast.  Love to explore new skills and new products. Making AI art is my new hobby.  Feel free DM me on Twitter for a quick chat. @zeng_wt 😉  Sign up to WhoWhatWhyAi newsletter! LINKS Virtual coffee chat with me☕ Femme Stock See My AI Christmas Tree 🎄 Twitter Ai newsletter My blog My AI art Gallery My page Ai art banners 2023 Free 100 AI art banners / cover images INTERESTS Virtual Reality Health & Fitness Productivity Task Management Writing User Experience Social Media Marketing Education Growth Hacking Internet of Things Developer Tools Artificial Intelligence Augmented Reality Product Hunt E-Commerce Bots Games BADGES Buddy System Gemologist Thought Leader View all badges MAKER HISTORY Angel In Heaven Healing hearts after miscarriage. Mar 2023 WhoWhatWhyAi The Goldilocks of Ai Newsletters Feb 2023 Femme Stock Beautiful, feminine AI stock images Jan 2023 AI generated banners 2023 Amazing AI art banners for 2023 Jan 2023 30 AI Christmas & Winter Coloring Pages 30 AI generated Christmas & winter themed coloring pages Dec 2022 View more Report",
            "Id Reference": "id=377104"
        }
    ]
    },
    {
        "Id": 376474,
        "Name": "Zoom Timer BlueSky Apps",
        "Tagline": "Timer shared directly in your Zoom meetings",
        "Url": "https://www.producthunt.com/posts/zoom-timer-bluesky-apps?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 138,
        "Profile_Url": "https://www.producthunt.com/@ben_ross, https://www.producthunt.com/@mait",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@ben_ross",
            "Profile Information": "https://www.producthunt.com/@ben_ross Ben Ross #791361 45 followers 0 following 118 points Follow BADGES 3 Top Product Veteran MAKER HISTORY BlueSky Timer for Zoom Make your Zoom meetings more efficient. Zoom Timer BlueSky Apps Jan 2023 BlueSky Timer for Zoom Jan 2022 Zoom Video communication made simple and easy Sep 2020 POWR Create beautiful website apps, no coding required Oct 2019 🎉 Joined Product Hunt January 25th, 2017 Report",
            "Id Reference": "id=376474"
        },
        {
            "All_Urls": "https://www.producthunt.com/@mait",
            "Profile Information": "https://www.producthunt.com/@mait Mahin Ali SaaS Marketing #4382539 3 followers 44 following 58 points Follow LINKS Website INTERESTS SaaS Artificial Intelligence MAKER HISTORY BlueSky Timer for Zoom Make your Zoom meetings more efficient. Jan 2023 🎉 Joined Product Hunt June 22nd, 2022 Report",
            "Id Reference": "id=376474"
        }
    ]
    },
    {
        "Id": 377113,
        "Name": "WhatsApp Beta",
        "Tagline": "A more seamless experience for WhatsApp users on macOS",
        "Url": "https://www.producthunt.com/posts/whatsapp-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 120,
        "Profile_Url": "https://www.producthunt.com/@iamsandysk, https://www.producthunt.com/@aluxian",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@iamsandysk",
            "Profile Information": "https://www.producthunt.com/@iamsandysk Santhosh Kumar Elango Co-Founder and CEO at Leadfriday #3406702 94 followers 335 following 62 points Follow LINKS Twitter Linkedin INTERESTS Productivity User Experience SaaS Tech MAKER HISTORY Leadfriday Generate 3x more leads using your current website traffic. Dec 2021 Jikoo.io Modern live chat and no-code chatbot for startups Aug 2021 WhatsApp The simple, reliable, secure messaging app. Jun 2021 🎉 Joined Product Hunt May 13th, 2021 Report",
            "Id Reference": "id=377113"
        },
        {
            "All_Urls": "https://www.producthunt.com/@aluxian",
            "Profile Information": "https://www.producthunt.com/@aluxian Alexandru Rosianu Co-founder & CTO @ Proptee #94699 242 followers 0 following 336 points Follow ABOUT On a mission to bring real estate investing to everyone. LINKS Twitter Website Facebook LinkedIn INTERESTS Android Mac Chrome Extensions Design Tools Productivity API Open Source Writing User Experience Internet of Things SaaS Software Engineering Developer Tools Artificial Intelligence GitHub BADGES 3 Top Product Veteran MAKER HISTORY Proptee: Fractional Real Estate Trading Earn weekly passive income from US, UK and EU real estate Sep 2022 Nothing Fancy Newsletter Learn how to earn passive income 😎🤏 😳🕶🤏 Aug 2022 Tomo Cheap Flights Save up to 70% on flights around the world ✈️ Jun 2017 Whatsie Desktop client for WhatsApp web May 2016 WhatsApp The simple, reliable, secure messaging app. Jun 2015 View more Report",
            "Id Reference": "id=377113"
        }
    ]
    },
    {
        "Id": 376809,
        "Name": "balancez",
        "Tagline": "Achieving balance, one day at a time",
        "Url": "https://www.producthunt.com/posts/balancez?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 117,
        "Profile_Url": "https://www.producthunt.com/@elifduran",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@elifduran",
            "Profile Information": "https://www.producthunt.com/@elifduran Elif Duran Co-founder @BeforeSunset, learner&maker #4366845 693 followers 1,097 following 805 points ☀️ 2 day streak Follow ABOUT Hi,   I am Elif from BeforeSunset and currently building in public.  Our aim is to create the simplest work management tool that will end you up working in a healthy environment, and finish your work before sunset 🌅   Your suggestions and comments are always welcome. We'll be launching a sub-product every month, stay tuned!  LINKS Twitter LinkedIn BeforeSunset INTERESTS Design Tools Productivity Task Management Freelance User Experience Marketing Startup Books Time Tracking SEO SaaS Developer Tools Tech Books BADGES Buddy System Gemologist Thought Leader View all badges MAKER HISTORY balancez Achieving balance, one day at a time Jan 2023 The Jingle Bell Timer Jingle into focus with our 25-minute AI timer BeforeSunset Catch beautiful sights, finish your work before sunset. Nov 2022 Free Productivity Guide Your productivity booster with all the statistics and facts Sep 2022 🎉 Joined Product Hunt June 15th, 2022 Report",
            "Id Reference": "id=376809"
        }
    ]
    },
    {
        "Id": 377095,
        "Name": "Tibio",
        "Tagline": "Track your mood, habits, make notes, and more",
        "Url": "https://www.producthunt.com/posts/tibio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 133,
        "Profile_Url": "https://www.producthunt.com/@patriksvob, https://www.producthunt.com/@duc_phi_viet",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@patriksvob",
            "Profile Information": "https://www.producthunt.com/@patriksvob Patrik Svoboda Product designer, Tibio co-creator. #370268 116 followers 103 following 188 points Follow LINKS Dribbble Twitter Linkedin BADGES 2 Top Product Veteran MAKER HISTORY Tibio Track your mood, habits, make notes, and more Jan 2023 React-UseAnimations Collection of free animated icons for React.js. Oct 2019 useAnimations An animated icon library for your projects May 2019 Cryptosaur Visually appealing cryptocurrency tracking iOS app Aug 2018 Pandacolors One click color generator with real time preview Sep 2017 🎉 Joined Product Hunt December 13th, 2015 Report",
            "Id Reference": "id=377095"
        },
        {
            "All_Urls": "https://www.producthunt.com/@duc_phi_viet",
            "Profile Information": "https://www.producthunt.com/@duc_phi_viet Duc Phi Viet Hi, I am a creator of Tibio app. #5081562 4 followers 0 following 16 points Follow MAKER HISTORY Tibio Track your mood, habits, make notes, and more Jan 2023 🎉 Joined Product Hunt January 26th, 2023 Report",
            "Id Reference": "id=377095"
        }
    ]
    },
    {
        "Id": 375586,
        "Name": "Monse",
        "Tagline": "Privacy-friendly personal finance application",
        "Url": "https://www.producthunt.com/posts/monse-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 123,
        "Profile_Url": "https://www.producthunt.com/@victor_falcon",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@victor_falcon",
            "Profile Information": "https://www.producthunt.com/@victor_falcon Víctor Falcón #1861319 15 followers 3 following 32 points Follow MAKER HISTORY NotifyWave Real-time notifications for everything that matters to you Mar 2023 Monse Privacy-friendly personal finance application Jan 2023 Monse Privacy-friendly and automated personal finances May 2022 💰 Manage your money and investment with a few minutes per month a no efford Aug 2021 🎉 Joined Product Hunt May 12th, 2019 Report",
            "Id Reference": "id=375586"
        }
    ]
    },
    {
        "Id": 377115,
        "Name": "Nike Training Club on Netflix",
        "Tagline": "Just stream it",
        "Url": "https://www.producthunt.com/posts/nike-training-club-on-netflix?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 89,
        "Profile_Url": "https://www.producthunt.com/@schlafman, https://www.producthunt.com/@navin_",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@schlafman",
            "Profile Information": "https://www.producthunt.com/@schlafman Dave Schlafman #385046 487 followers 178 following 68 points Follow LINKS Twitter BADGES Top Product Veteran MAKER HISTORY Netflix Watch TV shows and movies online. Jun 2017 🎉 Joined Product Hunt December 27th, 2015 Report",
            "Id Reference": "id=377115"
        },
        {
            "All_Urls": "https://www.producthunt.com/@navin_",
            "Profile Information": "https://www.producthunt.com/@navin_ Navin Iyengar Product Designer, Netflix #139257 664 followers 672 following 358 points Follow LINKS Twitter BADGES Top Product Veteran MAKER HISTORY Netflix Watch TV shows and movies online. Nov 2016 🎉 Joined Product Hunt January 18th, 2015 Report",
            "Id Reference": "id=377115"
        }
    ]
    },
    {
        "Id": 375401,
        "Name": "bestcodingpractices.dev",
        "Tagline": "A place to learn, inspire and share best coding practices",
        "Url": "https://www.producthunt.com/posts/bestcodingpractices-dev?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 87,
        "Profile_Url": "https://www.producthunt.com/@cedric_teyton, https://www.producthunt.com/@arthur_magne, https://www.producthunt.com/@xavier_blanc, https://www.producthunt.com/@heloise_birot, https://www.producthunt.com/@corentin_latappy, https://www.producthunt.com/@malo_couaran",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@cedric_teyton",
            "Profile Information": "https://www.producthunt.com/@cedric_teyton Cédric Teyton CEO & co-founder @Promyze #3283109 5 followers 1 following 27 points Follow ABOUT I'm a software developer with a strong interest in the following topics (among others): * Software Quality  * DevOps culture  * Cloud computing  * Software Craftsmanship   I've co-founded Promyze, a knowledge-sharing platform for developers focusing on expertise and best coding practices.  Our work is to help companies to improve their software engineering practices by levering on their internal knowledge sharing. LINKS Website INTERESTS Software Engineering Developer Tools MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 Promyze Share your best coding practices Oct 2021 🎉 Joined Product Hunt March 16th, 2021 Report",
            "Id Reference": "id=375401"
        },
        {
            "All_Urls": "https://www.producthunt.com/@arthur_magne",
            "Profile Information": "https://www.producthunt.com/@arthur_magne Arthur Magne Co-founder & CTO @ Promyze #3537745 2 followers 0 following 16 points Follow LINKS Website INTERESTS Productivity Developer Tools Tech MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 Promyze Share your best coding practices Oct 2021 🎉 Joined Product Hunt July 8th, 2021 Report",
            "Id Reference": "id=375401"
        },
        {
            "All_Urls": "https://www.producthunt.com/@xavier_blanc",
            "Profile Information": "https://www.producthunt.com/@xavier_blanc Xavier Blanc I am interested in software development #3756491 0 followers 0 following 16 points Follow LINKS Website MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 Promyze Share your best coding practices Oct 2021 🎉 Joined Product Hunt September 30th, 2021 Report",
            "Id Reference": "id=375401"
        },
        {
            "All_Urls": "https://www.producthunt.com/@heloise_birot",
            "Profile Information": "https://www.producthunt.com/@heloise_birot Heloïse Birot https://promyze.com/ #3694934 0 followers 0 following 16 points ☀️ 2 day streak Follow INTERESTS Design Tools Marketing Growth Hacking Developer Tools Tech MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 Promyze Share your best coding practices Oct 2021 🎉 Joined Product Hunt September 8th, 2021 Report",
            "Id Reference": "id=375401"
        },
        {
            "All_Urls": "https://www.producthunt.com/@corentin_latappy",
            "Profile Information": "https://www.producthunt.com/@corentin_latappy Corentin Latappy Dev @Promyze #3769713 0 followers 0 following 8 points Follow MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 🎉 Joined Product Hunt October 6th, 2021 Report",
            "Id Reference": "id=375401"
        },
        {
            "All_Urls": "https://www.producthunt.com/@malo_couaran",
            "Profile Information": "https://www.producthunt.com/@malo_couaran Malo Couaran Budding software craftman #5022568 0 followers 0 following 8 points Follow INTERESTS Developer Tools Artificial Intelligence Tech MAKER HISTORY bestcodingpractices.dev A place to learn, inspire and share best coding practices Jan 2023 🎉 Joined Product Hunt January 17th, 2023 Report",
            "Id Reference": "id=375401"
        }
    ]
    },
    {
        "Id": 377208,
        "Name": "Moonwalkers",
        "Tagline": "Seriously fast walking shoes",
        "Url": "https://www.producthunt.com/posts/moonwalkers?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 68,
        "Profile_Url": "No",
        "Information": [{"All_Urls":""},{ "Profile Information":""},{ "Id Reference":""}]
    },
    {
        "Id": 376579,
        "Name": "Squaredance for Shopify",
        "Tagline": "Partner marketplace for DTC brands, get customers,grow sales",
        "Url": "https://www.producthunt.com/posts/squaredance-for-shopify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 76,
        "Profile_Url": "https://www.producthunt.com/@shilpamandhan, https://www.producthunt.com/@nmastracci, https://www.producthunt.com/@michael_fulton, https://www.producthunt.com/@camay_lee",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@shilpamandhan",
            "Profile Information": "https://www.producthunt.com/@shilpamandhan Shilpa Mandhan Head of Growth @ Squaredance #4539037 9 followers 2 following 17 points Follow ABOUT Hi! I work as the Head of Growth at Squaredance. I manage our acquisition and retention+engagement efforts, and love it. I've spent much of my career in customer success and consulting, and have been finding the role and the new industry at Squaredance very refreshing to work in, especially after a long mat leave caring for first kid.  I love coffee, crossfit, travel, and jamming to Bollywood tunes.  LINKS LinkedIn INTERESTS Customer Success Marketing Growth Hacking Artificial Intelligence Social media marketing MAKER HISTORY Squaredance for Shopify Partner marketplace for DTC brands—get customers, grow sales Jan 2023 🎉 Joined Product Hunt August 22nd, 2022 Report",
            "Id Reference": "id=376579"
        },
        {
            "All_Urls": "https://www.producthunt.com/@nmastracci",
            "Profile Information": "https://www.producthunt.com/@nmastracci Natalie Mastracci Product @ Squaredance #4861991 17 followers 19 following 43 points Follow ABOUT Former 2x Olympic rower bringing high-performance team management and customer obsession to product leadership in marketplace SaaS. LINKS LinkedIn INTERESTS User Experience Marketing E-Commerce Tech Affiliate marketing MAKER HISTORY Squaredance for Shopify Partner marketplace for DTC brands—get customers, grow sales Jan 2023 🎉 Joined Product Hunt November 30th, 2022 Report",
            "Id Reference": "id=376579"
        },
        {
            "All_Urls": "https://www.producthunt.com/@michael_fulton",
            "Profile Information": "https://www.producthunt.com/@michael_fulton Michael Fulton Growth Marketing Director #4973029 8 followers 3 following 8 points Follow ABOUT As a marketing professional, I've worked across the entire spectrum to develop a fairly well-rounded approach. I've been a media buyer/planner, designer, copywriter, and strategist, managed email, events, social, video, web, influencers, and partnerships, and have worked for B2B, not-for-profit, DTC, MLM, and now a SaaS marketplace.  Build a strong foundation so everything else can work properly. LINKS Squaredance INTERESTS Productivity User Experience Marketing SaaS Marketing attribution Influencer marketing Affiliate marketing MAKER HISTORY Squaredance for Shopify Partner marketplace for DTC brands—get customers, grow sales Jan 2023 🎉 Joined Product Hunt January 4th, 2023 Report",
            "Id Reference": "id=376579"
        },
        {
            "All_Urls": "https://www.producthunt.com/@camay_lee",
            "Profile Information": "https://www.producthunt.com/@camay_lee Camay Lee Product marketer #4975124 1 follower 0 following 6 points Follow INTERESTS Design Tools User Experience Marketing Tech Design Graphic Design Web Design UX Design Design resources MAKER HISTORY Squaredance for Shopify Partner marketplace for DTC brands—get customers, grow sales Jan 2023 🎉 Joined Product Hunt January 4th, 2023 Report",
            "Id Reference": "id=376579"
        }
    ]
    },
    {
        "Id": 377154,
        "Name": "7-Day UX Job Hunting Challenge",
        "Tagline": "Go from 0 to 10 job applications, in 7 days",
        "Url": "https://www.producthunt.com/posts/7-day-ux-job-hunting-challenge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Profile_Url": "https://www.producthunt.com/@semigrownkid, https://www.producthunt.com/@bribribri",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@semigrownkid",
            "Profile Information": "https://www.producthunt.com/@semigrownkid Christopher Nguyen Making UX Playbook #3390344 103 followers 6 following 166 points ☀️ 2 day streak Follow ABOUT The Diversified Designpreneur  Building @uxplaybook @divvynotion @playstack @supbiohq  Obsess with UX, growth hacking and tech  Open to connections on Twitter @uxchrisnguyen 🤓 LINKS Website Twitter LinkedIn TikTok YouTube INTERESTS Email Design Tools Productivity Writing User Experience Social Media Growth Hacking Global Nomad Artificial Intelligence Remote Work BADGES Buddy System View all badges MAKER HISTORY UX Playbook ⚡️ Build A Better UX Career, Faster 7-Day UX Job Hunting Challenge Jan 2023 UX Portfolio Critique Jan 2023 UX Interview Masterclass Oct 2022 UX Portfolio Playbook Aug 2022 UX Management Playbook 2.0 Jul 2022 UX Management Playbook Jul 2022 UX Playbook 2.0 May 2022 UX Playbook May 2021 🎉 Joined Product Hunt May 6th, 2021 Report",
            "Id Reference": "id=377154"
        },
        {
            "All_Urls": "https://www.producthunt.com/@bribribri",
            "Profile Information": "https://www.producthunt.com/@bribribri Bryant Castro Design leader growing teams & products #4654449 3 followers 1 following 29 points Follow ABOUT A designer doing nerdy design stuff before it was coveted as a profitable professional skill. My last role as Director of UX for Bitso (web3). Building products that help designers mostly. INTERESTS Design Tools Productivity Crypto Tech Web3 UX Design MAKER HISTORY UX Playbook ⚡️ Build A Better UX Career, Faster 7-Day UX Job Hunting Challenge Jan 2023 UX Portfolio Critique Jan 2023 UX Interview Masterclass Oct 2022 🎉 Joined Product Hunt September 23rd, 2022 Report",
            "Id Reference": "id=377154"
        }
    ]
    },
    {
        "Id": 377195,
        "Name": "Whispr",
        "Tagline": "Alternative to ChatGPT",
        "Url": "https://www.producthunt.com/posts/whispr-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 60,
        "Profile_Url": "https://www.producthunt.com/@alvaro_pintado",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@alvaro_pintado",
            "Profile Information": "https://www.producthunt.com/@alvaro_pintado Álvaro Pintado Co-Founder at Gox. #5016060 2 followers 0 following 7 points 🌟 5 day streak Follow INTERESTS Artificial Intelligence MAKER HISTORY Whispr ChatGPT's alternative for when it's disabled. Jan 2023 🎉 Joined Product Hunt January 16th, 2023 Report",
            "Id Reference": "id=377195"
        }
    ]
    },
    {
        "Id": 377087,
        "Name": "This Product Does Not Exist",
        "Tagline": "Reinventing the wheel with AI, one product at a time",
        "Url": "https://www.producthunt.com/posts/this-product-does-not-exist-1?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 56,
        "Profile_Url": "https://www.producthunt.com/@verfasor",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@verfasor",
            "Profile Information": "https://www.producthunt.com/@verfasor Mighil globe-earther and schnauzer enthusiast #3955223 127 followers 1 following 175 points ☀️ 2 day streak Follow ABOUT Seasoned professional with diverse work experience in marketing and technology. In my free time, I enjoy reading, writing, tinkering, and experimenting new sound design techniques. Key member of EarlyBird, HeyForm, and TinySnap. I'm down for a coffee and chinwag if you're in Chengdu. Weixin @mighil. LINKS side dishes mighil.com portfolio old blog INTERESTS Productivity Writing User Experience Marketing Developer Tools BADGES Gemologist Top Product View all badges MAKER HISTORY GPT 3.5 Turbo Playground A micro app to try the new ChatGPT API Mar 2023 SEO Stan An AI-powered micro SEO tool for bloggers and makers Feb 2023 Linked XP Elevate your LinkedIn game Feb 2023 This Product Does Not Exist Reinventing the wheel. One AI-generated product at a time. Jan 2023 Welma Understand and retain complex text with the help of AI Jan 2023 View more Report",
            "Id Reference": "id=377087"
        }
    ]
    },
    {
        "Id": 377100,
        "Name": "Fablegym",
        "Tagline": "Read a classic book in 30 days as an email newsletter",
        "Url": "https://www.producthunt.com/posts/fablegym?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 59,
        "Profile_Url": "https://www.producthunt.com/@solomon_teach",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@solomon_teach",
            "Profile Information": "https://www.producthunt.com/@solomon_teach Solomon Kingsnorth Teacher #1253561 147 followers 17 following 341 points ☀️ 2 day streak Follow LINKS Website Twitter INTERESTS Mac Design Tools Productivity User Experience Growth Hacking Developer Tools Artificial Intelligence Tech Books MAKER HISTORY Fablegym Read a classic book in 30 days as an email newsletter. Jan 2023 Serge Curated directory for custom illustrations at stock prices. May 2020 Researchify Research tool for kids during a COVID-19 schools shutdown. Mar 2020 🎉 Joined Product Hunt April 16th, 2018 Report",
            "Id Reference": "id=377100"
        }
    ]
    },
    {
        "Id": 376954,
        "Name": "ClipNinja",
        "Tagline": "Minimal copy and paste tool for Mac",
        "Url": "https://www.producthunt.com/posts/clipninja-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 44,
        "Profile_Url": "https://www.producthunt.com/@liborhuspenina",
        "Information":   
    [
        {
            "All_Urls": "https://www.producthunt.com/@liborhuspenina",
            "Profile Information": "https://www.producthunt.com/@liborhuspenina Libor Huspenina Apple platforms developer #1694039 23 followers 70 following 7 points ⚡️ 4 day streak Follow ABOUT I'm interested in software architecture, tests, and applying old-school principles to modern technologies. I dabble in macOS - open-source tool ClipNinja and sometimes write for mobileit.cz LINKS Mastodon Twitter INTERESTS Productivity User Experience Developer Tools MAKER HISTORY ClipNinja macos, copy, paste, open-source Jan 2023 ClipNinja Clipboard manager that enables you to paste effectively. Feb 2019 🎉 Joined Product Hunt February 24th, 2019 Report",
            "Id Reference": "id=376954"
        }
    ]
    },
    {
        "Id": 377071,
        "Name": "DeveloperHub.io",
        "Tagline": "The most advanced tool for creating product and API docs",
        "Url": "https://www.producthunt.com/posts/developerhub-io-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Profile_Url": "https://www.producthunt.com/@zaid_daba_een1",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@zaid_daba_een1",
            "Profile Information": "https://www.producthunt.com/@zaid_daba_een1 Zaid Daba'een CEO & Founder - DeveloperHub #1647775 32 followers 0 following 48 points Follow ABOUT Guardian angel for technical writers around the world 🌍  MAKER HISTORY DeveloperHub.io Your Product Deserves to be Understood DeveloperHub.io Jan 2023 Developerhub.io Jul 2018 🎉 Joined Product Hunt January 26th, 2019 Report",
            "Id Reference": "id=377071"
        }
    ]
    },
    {
        "Id": 376994,
        "Name": "Qeraunos",
        "Tagline": "An ultrafast, lightweight caching solution for GraphQL",
        "Url": "https://www.producthunt.com/posts/qeraunos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 40,
        "Profile_Url": "https://www.producthunt.com/@arthurynh, https://www.producthunt.com/@dennis_cheung, https://www.producthunt.com/@amrit_vela",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@arthurynh",
            "Profile Information": "https://www.producthunt.com/@arthurynh Arthur Huynh Software Engineer at Qeraunos #5055002 1 follower 0 following 4 points Follow MAKER HISTORY Qeraunos An ultrafast, lightweight caching solution for GraphQL. Jan 2023 🎉 Joined Product Hunt January 20th, 2023 Report",
            "Id Reference": "id=376994"
        },
        {
            "All_Urls": "https://www.producthunt.com/@dennis_cheung",
            "Profile Information": "https://www.producthunt.com/@dennis_cheung Dennis Cheung software engineer #5088711 1 follower 0 following 3 points Follow MAKER HISTORY Qeraunos An ultrafast, lightweight caching solution for GraphQL. Jan 2023 🎉 Joined Product Hunt January 29th, 2023 Report",
            "Id Reference": "id=376994"
        },
        {
            "All_Urls": "https://www.producthunt.com/@amrit_vela",
            "Profile Information": "https://www.producthunt.com/@amrit_vela Amrit Ramos Software Engineer. #5088716 0 followers 2 following 3 points Follow MAKER HISTORY Qeraunos An ultrafast, lightweight caching solution for GraphQL. Jan 2023 🎉 Joined Product Hunt January 29th, 2023 Report",
            "Id Reference": "id=376994"
        }
    ]
    },
    {
        "Id": 377245,
        "Name": "Deploy Button for custom GPT-3 APIs",
        "Tagline": "Instant GPT-3 backend hosting so you can focus on product",
        "Url": "https://www.producthunt.com/posts/deploy-button-for-custom-gpt-3-apis?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 44,
        "Profile_Url": "https://www.producthunt.com/@edwardbenson",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@edwardbenson",
            "Profile Information": "https://www.producthunt.com/@edwardbenson Ted Benson I turn research into product. #122399 612 followers 614 following 56 points ☀️ 2 day streak Follow LINKS Website Twitter BADGES Veteran MAKER HISTORY Production LangChain Hosting Turn LangChains into production multi-user APIs. Feb 2023 Deploy Button for custom GPT-3 APIs Instant GPT-3 backend hosting so you can focus on product. Jan 2023 Shipped with AI Weekly, focused AI commentary for builders and investors Dec 2022 Magic Forms by Cloudstitch Use Google Sheets as a database for all your web forms Cloudstitch Jul 2017 Stack in a Box, by Cloudstitch Aug 2015 Magic Forms by Cloudstitch Aug 2015 Buttonjoy WiFi buttons that donate to charity, send email, SMS & more Feb 2017 🎉 Joined Product Hunt December 13th, 2014 Report",
            "Id Reference": "id=377245"
        }
    ]
    },
    {
        "Id": 376612,
        "Name": "Free Valentine's Day 3d illustrations",
        "Tagline": "Lovely 3d illustrations for your design projects",
        "Url": "https://www.producthunt.com/posts/free-valentine-s-day-3d-illustrations?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 36,
        "Profile_Url": "https://www.producthunt.com/@anton_mishin, https://www.producthunt.com/@egozavria, https://www.producthunt.com/@new_user_92c4ffb9ee",
        "Information":   
    [
        {
            "All_Urls": "https://www.producthunt.com/@anton_mishin",
            "Profile Information": "https://www.producthunt.com/@anton_mishin Anton Mishin Co-founder at Wannathis.one #616880 128 followers 25 following 761 points Follow LINKS Website INTERESTS Productivity Home GIFs Developer Tools Augmented Reality BADGES 12 Top Product Veteran View all badges MAKER HISTORY 3d illustration plugin Simple plugin with huge 3d library right in Figma Mar 2023 Wannathis 3d products for digital designers to save time and work more efficient Free Valentine's Day 3d illustrations Jan 2023 MacBook Pro Mockups Dec 2022 iPhone 14 Pro Mockups Nov 2022 Holographic Abstract 3D Backgrounds Nov 2022 Free Halloween 3D illustrations (2.0) Oct 2022 Big Sale Oct 2022 Abstract 3d illustrations Aug 2022 Inflatable 3d alphabet Aug 2022 Space 3d illustration May 2022 Retro 3d illustrations Apr 2022 Humans 3D Characters V3.0 Jan 2022 3D Charts Dec 2021 Free Christmas 3D Illustrations Nov 2021 Free 3D Halloween Illustrations Oct 2021 Kukla 3d icon kit (v2.0) Oct 2021 Security 3D Icons Aug 2021 Emoji Jul 2021 LOOPS Feb 2021 Xmas 3d icons Dec 2020 Humans Oct 2020 Kukla kit Jun 2020 The Dot. Prototype easy and fast with ready-to-go wireframe UI pack Oct 2020 Design Starter Kit for Sketch A starting point for your next design project. May 2019 Charts The most comprehensive collection of charts for Sketch Mar 2019 View more Report",
            "Id Reference": "id=376612"
        },
        {
            "All_Urls": "https://www.producthunt.com/@egozavria",
            "Profile Information": "https://www.producthunt.com/@egozavria Egor Mishin #1726448 23 followers 0 following 322 points Follow BADGES 7 Top Product MAKER HISTORY 3d illustration plugin Simple plugin with huge 3d library right in Figma Mar 2023 Wannathis 3d products for digital designers to save time and work more efficient Free Valentine's Day 3d illustrations Jan 2023 MacBook Pro Mockups Dec 2022 iPhone 14 Pro Mockups Nov 2022 Holographic Abstract 3D Backgrounds Nov 2022 Free Halloween 3D illustrations (2.0) Oct 2022 Big Sale Oct 2022 Abstract 3d illustrations Aug 2022 Inflatable 3d alphabet Aug 2022 Space 3d illustration May 2022 Retro 3d illustrations Apr 2022 Humans 3D Characters V3.0 Jan 2022 3D Charts Dec 2021 Free Christmas 3D Illustrations Nov 2021 Free 3D Halloween Illustrations Oct 2021 Kukla 3d icon kit (v2.0) Oct 2021 Security 3D Icons Aug 2021 Emoji Jul 2021 LOOPS Feb 2021 Xmas 3d icons Dec 2020 Humans Oct 2020 Kukla kit Jun 2020 🎉 Joined Product Hunt March 13th, 2019 Report",
            "Id Reference": "id=376612"
        },
        {
            "All_Urls": "https://www.producthunt.com/@new_user_92c4ffb9ee",
            "Profile Information": "https://www.producthunt.com/@new_user_92c4ffb9ee Veronika Bochkareva 3D Artist #1766409 4 followers 2 following 37 points Follow ABOUT 3D artist, Blender and Cinema4D master, and all-around object, characters and mock-ups creator. Ready to make your designs pop and put a smile on people's faces. Let's make something awesome together!  LINKS Dribbble Behance Instagram INTERESTS Design Tools Home Marketing Internet of Things Photography Artificial Intelligence Tech MAKER HISTORY Wannathis 3d products for digital designers to save time and work more efficient MacBook Pro Mockups Dec 2022 iPhone 14 Pro Mockups Nov 2022 Holographic Abstract 3D Backgrounds Nov 2022 Free Halloween 3D illustrations (2.0) Oct 2022 Big Sale Oct 2022 Abstract 3d illustrations Aug 2022 Inflatable 3d alphabet Aug 2022 🎉 Joined Product Hunt April 4th, 2019 Report",
            "Id Reference": "id=376612"
        }
    ]
    },
    {
        "Id": 373387,
        "Name": "Read Me Aloud",
        "Tagline": "iPad tales for kids who are learning to read",
        "Url": "https://www.producthunt.com/posts/read-me-aloud?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 36,
        "Profile_Url": "https://www.producthunt.com/@nutsmuggler",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@nutsmuggler",
            "Profile Information": "https://www.producthunt.com/@nutsmuggler Davide Benini Maker of Menu Plan and Read me Aloud #4927581 9 followers 9 following 6 points ☀️ 2 day streak Follow ABOUT Davide is a freelance iOs designer and developer. He has got himself an English Lit degree and a PhD in Irish literature. After a brief period working as a technical translator, he started pursuing his passion for computers and development. Davide has been working on iOS ever since the first SDK was released. He has worked on a huge number of projects, mostly with the good folks at NTNext and with his pal Filippo.  Davide is married to Michela and has two kids, Federico and Caterina.  When not coding or playing with his kids, Davide plays Irish music on the fiddle and mandolin or tends to his vegetable garden.  You can find some extra info on Davide on his country life blog, quagliodromo.it, or his work website davidebenini.it. LINKS Menu Plan Read Me Aloud INTERESTS iOS Music Cooking Kids & Parenting Online Learning MAKER HISTORY Read Me Aloud iPad tales for kids who are learning to read Jan 2023 🎉 Joined Product Hunt December 16th, 2022 Report",
            "Id Reference": "id=373387"
        }
    ]
    },
    {
        "Id": 377229,
        "Name": "DeepReview",
        "Tagline": "Write CVs, cover letters, perf reviews with the power of AI",
        "Url": "https://www.producthunt.com/posts/deepreview?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 30,
        "Profile_Url": "https://www.producthunt.com/@horia141, https://www.producthunt.com/@liviu_coman",
        "Information": 
   
    [
        {
            "All_Urls": "https://www.producthunt.com/@horia141",
            "Profile Information": "https://www.producthunt.com/@horia141 Horia Coman Software engineer at Stack Overflow #1084158 1 follower 0 following 3 points Follow LINKS Website INTERESTS Web App Slack Health & Fitness Design Tools Productivity API Open Source Writing User Experience Prototyping Marketing Education Growth Hacking Wearables Developer Tools Artificial Intelligence Books BADGES Veteran MAKER HISTORY DeepReview Write CVs, cover letters, perf reviews with the power of AI Jan 2023 🎉 Joined Product Hunt November 17th, 2017 Report",
            "Id Reference": "id=377229"
        },
        {
            "All_Urls": "https://www.producthunt.com/@liviu_coman",
            "Profile Information": "https://www.producthunt.com/@liviu_coman Liviu Coman #621551 16 followers 0 following 12 points Follow INTERESTS Android iOS BADGES Veteran MAKER HISTORY DeepReview Write CVs, cover letters, perf reviews with the power of AI Jan 2023 Boxxit Find gift ideas for friends based on their Facebook likes. Nov 2017 🎉 Joined Product Hunt August 1st, 2016 Report",
            "Id Reference": "id=377229"
        }
    ]
    },
    {
        "Id": 377177,
        "Name": "Git Assistant",
        "Tagline": "Describe a feature; get a pull request. Github + Chat GPT",
        "Url": "https://www.producthunt.com/posts/git-assistant?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 26,
        "Profile_Url": "https://www.producthunt.com/@akondelin",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@akondelin",
            "Profile Information": "https://www.producthunt.com/@akondelin Andrew Kondelin Developer, improving my marketing skills #5043781 4 followers 0 following 2 points ☀️ 2 day streak Follow INTERESTS Productivity Marketing Developer Tools Artificial Intelligence MAKER HISTORY Git Assistant Describe a feature; get a pull request. Github + Chat GPT Jan 2023 🎉 Joined Product Hunt January 19th, 2023 Report",
            "Id Reference": "id=377177"
        }
    ]
    },
    {
        "Id": 377160,
        "Name": "Anagramish",
        "Tagline": "web based word game combining anagrams and word ladders ",
        "Url": "https://www.producthunt.com/posts/anagramish?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 28,
        "Profile_Url": "https://www.producthunt.com/@emh",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@emh",
            "Profile Information": "https://www.producthunt.com/@emh Evan Haveman #119614 88 followers 187 following 40 points Follow LINKS Twitter BADGES Veteran MAKER HISTORY Anagramish web based word game combining anagrams and word ladders Jan 2023 thisopenspace Find the creative space you need Feb 2016 Gnusfeed Product Hunt for crowdfunding projects Apr 2015 🎉 Joined Product Hunt December 9th, 2014 Report",
            "Id Reference": "id=377160"
        }
    ]
    },
    {
        "Id": 377249,
        "Name": "EffectiveGPT",
        "Tagline": "Get accurate ChatGPT prompts",
        "Url": "https://www.producthunt.com/posts/effectivegpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 26,
        "Profile_Url": "https://www.producthunt.com/@recurrsed",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@recurrsed",
            "Profile Information": "https://www.producthunt.com/@recurrsed Recurrsed I build random useless stuff... #5061404 5 followers 13 following 2 points Follow INTERESTS Video Streaming Streaming Services Tech MAKER HISTORY EffectiveGPT Get accurate ChatGPT prompts Jan 2023 🎉 Joined Product Hunt January 22nd, 2023 Report",
            "Id Reference": "id=377249"
        }
    ]
    },
    {
        "Id": 377231,
        "Name": "Bubbly",
        "Tagline": "Resolve customer queries 10x faster with OpenAI",
        "Url": "https://www.producthunt.com/posts/bubbly-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 13,
        "Profile_Url": "https://www.producthunt.com/@andy_andy123",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@andy_andy123",
            "Profile Information": "https://www.producthunt.com/@andy_andy123 Andy Bubbly Team #4874262 2 followers 0 following 2 points Follow MAKER HISTORY Bubbly Automate Marketing & Engagement Campaigns Over Slack Bubbly Jan 2023 Bubbly Jan 2023 Bubbly Dec 2022 🎉 Joined Product Hunt December 4th, 2022 Report",
            "Id Reference": "id=377231"
        }
    ]
    },
    {
        "Id": 374958,
        "Name": "Twitter for Noobs",
        "Tagline": "All-in-one Twitter growth framework and resource hub",
        "Url": "https://www.producthunt.com/posts/twitter-for-noobs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 331,
        "Profile_Url": "No",
        "Information":[{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376775,
        "Name": "ChatGenie",
        "Tagline": "Talk to any character, dead or alive, real or made up",
        "Url": "https://www.producthunt.com/posts/chatgenie?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 248,
        "Profile_Url": "https://www.producthunt.com/@web3slinger",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@web3slinger",
            "Profile Information": "https://www.producthunt.com/@web3slinger Patrick 26 | Crafting stuff #3822698 6 followers 0 following 36 points Follow BADGES Top Product MAKER HISTORY ChatGenie Talk to any character, dead or alive, real or made up Jan 2023 mintibbl Draw, guess, and mint with your frens! Aug 2022 cryptip.me The friendly way to accept tips in ETH. Jun 2022 🎉 Joined Product Hunt October 29th, 2021 Report",
            "Id Reference": "id=376775"
        }
    ]
    },
    {
        "Id": 376839,
        "Name": "Recipes By AI",
        "Tagline": "Generate recipes from a list of ingredients, powered by AI",
        "Url": "https://www.producthunt.com/posts/recipes-by-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 195,
        "Profile_Url": "https://www.producthunt.com/@introvertgeekuk",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@introvertgeekuk",
            "Profile Information": "https://www.producthunt.com/@introvertgeekuk Lewis Crutch Building Content Websites and AI Tools #4744987 87 followers 14 following 22 points Follow INTERESTS Marketing Artificial Intelligence BADGES Top Product MAKER HISTORY Recipes By AI Generate Recipes from a List of Ingredients, Powered By AI Jan 2023 🎉 Joined Product Hunt October 25th, 2022 Report",
            "Id Reference": "id=376839"
        }
    ]
    },
    {
        "Id": 377000,
        "Name": "wallaroo",
        "Tagline": "Wallpapers just for you (from the maker of Twitterrific)!",
        "Url": "https://www.producthunt.com/posts/wallaroo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 151,
        "Profile_Url": "https://www.producthunt.com/@vonster, https://www.producthunt.com/@chockenberry",
        "Information": 
  
    [
        {
            "All_Urls": "https://www.producthunt.com/@vonster",
            "Profile Information": "https://www.producthunt.com/@vonster Von Glitschka I create design and live near Bigfoot. #4237016 0 followers 0 following 12 points Follow LINKS Website INTERESTS Productivity MAKER HISTORY wallaroo Wallpapers just for you! Jan 2023 🎉 Joined Product Hunt April 21st, 2022 Report",
            "Id Reference": "id=377000"
        },
        {
            "All_Urls": "https://www.producthunt.com/@chockenberry",
            "Profile Information": "https://www.producthunt.com/@chockenberry Craig Hockenberry I GET PAID TO TYPE #3953190 2 followers 0 following 74 points Follow LINKS Website MAKER HISTORY wallaroo Wallpapers just for you! Jan 2023 WorldWideWeb A simple web server Jun 2022 Notchmeister Notches gone wild Dec 2021 Frenzic: Overtime Frantic puzzles, full-time fun Apr 2021 Tot Your tiny text companion. Feb 2020 View more Report",
            "Id Reference": "id=377000"
        }
    ]
    },
    {
        "Id": 376815,
        "Name": "Møbel",
        "Tagline": "Transform your room with artificial intelligence.",
        "Url": "https://www.producthunt.com/posts/mobel-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 135,
        "Profile_Url": "https://www.producthunt.com/@pwntus",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@pwntus",
            "Profile Information": "https://www.producthunt.com/@pwntus Pontus Aurdal IoT, AWS, serverless, event-driven. #4138244 4 followers 0 following 42 points Follow INTERESTS Web App Internet of Things Developer Tools Tech Development BADGES Top Product MAKER HISTORY Change Style AI Create new styles of your pictures with the same structure Feb 2023 AI Photo Robot Train your own LoRA AI subject and generate photos. Feb 2023 AI Food Robot Food pictures and recipes generated by A.I. Feb 2023 Møbel Transform your room with artificial intelligence. Jan 2023 Iotnite The leading sourcing platform for digitization and IoT Apr 2022 🎉 Joined Product Hunt March 11th, 2022 Report",
            "Id Reference": "id=376815"
        }
    ]
    },
    {
        "Id": 376741,
        "Name": "Atomic",
        "Tagline": "Solve all your scheduling problems using AI for everyone",
        "Url": "https://www.producthunt.com/posts/atomic-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 115,
        "Profile_Url": "https://www.producthunt.com/@rushi_parikh",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@rushi_parikh",
            "Profile Information": "https://www.producthunt.com/@rushi_parikh Rish Indiehacker running a solo biz #2466251 62 followers 7 following 42 points Follow ABOUT Hi,  This is Rish. Looking to make my app Atomic a success and live off of it if possible.  BADGES Top Product MAKER HISTORY Atomic Save time planning your Google calendar using AI Aug 2022 Atomic Solve all your scheduling problems using AI for everyone Jan 2023 GPT Overflow AI Battle of prompts StackOverflow style Dec 2022 🎉 Joined Product Hunt March 27th, 2020 Report",
            "Id Reference": "id=376741"
        }
    ]
    },
    {
        "Id": 376414,
        "Name": "Loti",
        "Tagline": "Remove non-consensual intimate images of yourself online.",
        "Url": "https://www.producthunt.com/posts/loti-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 97,
        "Profile_Url": "https://www.producthunt.com/@lukearrigoni, https://www.producthunt.com/@rebekah_arrigoni, https://www.producthunt.com/@hirak_chhatbar",
        "Information":    
   
   
    [
        {
            "All_Urls": "https://www.producthunt.com/@lukearrigoni",
            "Profile Information": "https://www.producthunt.com/@lukearrigoni Luke Arrigoni Founder of multiple AI companies. #4741117 4 followers 4 following 21 points Follow ABOUT Helping companies build state-of-the-art ML/AI programs.  Built and contributed to ML/AI programs at GettyImages, Janssen (J&J), UPS, AT&T, Thomson Reuters, Stryker, Goldman Sachs, FOX Networks, Sephora, Little Caesars and others.  I've designed custom machine learning models and data pipelines at a petabyte scale while developing market-wide strategic directions for my clients. LINKS Forbes Next 1000 LinkedIn INTERESTS Marketing Artificial Intelligence MAKER HISTORY Loti Remove non-consensual intimate images of yourself online. Jan 2023 🎉 Joined Product Hunt October 24th, 2022 Report",
            "Id Reference": "id=376414"
        },
        {
            "All_Urls": "https://www.producthunt.com/@rebekah_arrigoni",
            "Profile Information": "https://www.producthunt.com/@rebekah_arrigoni Rebekah Arrigoni Co-founder and CEO of Loti #5090551 1 follower 4 following 14 points ☀️ 2 day streak Follow ABOUT Co-founder and CEO of Loti. Loti is an AI product that uses facial recognition to find and remove non-consensual intimate images and videos (aka Revenge Porn) from the internet.  LINKS Loti LinkedIn INTERESTS Artificial Intelligence Tech MAKER HISTORY Loti Remove non-consensual intimate images of yourself online. Jan 2023 🎉 Joined Product Hunt January 29th, 2023 Report",
            "Id Reference": "id=376414"
        },
        {
            "All_Urls": "https://www.producthunt.com/@hirak_chhatbar",
            "Profile Information": "https://www.producthunt.com/@hirak_chhatbar Hirak Chhatbar Co-founder and Chief Technology Officer #5090722 2 followers 0 following 8 points ☀️ 2 day streak Follow MAKER HISTORY Loti Remove non-consensual intimate images of yourself online. Jan 2023 🎉 Joined Product Hunt January 29th, 2023 Report",
            "Id Reference": "id=376414"
        }
    ]
    },
    {
        "Id": 376977,
        "Name": "Wifi QR Code",
        "Tagline": "Share your Wifi with friends & family",
        "Url": "https://www.producthunt.com/posts/wifi-qr-code?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 95,
        "Profile_Url": "https://www.producthunt.com/@max_sommer",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@max_sommer",
            "Profile Information": "https://www.producthunt.com/@max_sommer Max Sommer Web Developer. Curious person. #5059466 11 followers 3 following 15 points Follow ABOUT Trying to leave a positive dent in the universe. LINKS GitHub maxsommer.de Twitter LinkedIn INTERESTS Linux Browser Extensions Mac Web App PlayStation VR Virtual Reality Email Design Tools Productivity Task Management Parenting API Open Source Writing User Experience Analytics Prototyping Ad Blockers A/B Testing Typography MAKER HISTORY Wifi QR Code Share your Wifi with friends & family Jan 2023 🎉 Joined Product Hunt January 21st, 2023 Report",
            "Id Reference": "id=376977"
        }
    ]
    },
    {
        "Id": 376966,
        "Name": "ChatGPT Prompts",
        "Tagline": "Prompts tailored for entrepreneurs, marketers, developers...",
        "Url": "https://www.producthunt.com/posts/chatgpt-prompts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 96,
        "Profile_Url": "https://www.producthunt.com/@adrienf",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@adrienf",
            "Profile Information": "https://www.producthunt.com/@adrienf Adrien #2235632 4 followers 0 following 14 points Follow ABOUT I'm a tech entrepreneur driven by a passion for creating things that make a positive impact on people's lives. INTERESTS Productivity User Experience Marketing Developer Tools Artificial Intelligence MAKER HISTORY ChatGPT Prompts Prompts tailored for entrepreneurs, marketers, developers... Jan 2023 Hypnosis Hypnosis app to help you manage your emotions Dec 2019 🎉 Joined Product Hunt November 30th, 2019 Report",
            "Id Reference": "id=376966"
        }
    ]
    },
    {
        "Id": 373699,
        "Name": "Text2SQL.AI",
        "Tagline": "Generate SQL with AI",
        "Url": "https://www.producthunt.com/posts/text2sql-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 85,
        "Profile_Url": "https://www.producthunt.com/@gergo_miklos",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@gergo_miklos",
            "Profile Information": "https://www.producthunt.com/@gergo_miklos Gary Miklos Bootstrapped solopreneur. #4792361 21 followers 28 following 25 points Follow ABOUT Data Science @ University, Software Engineer @ Cloudera, Father @ 2 Kids, Indie Maker @ Late-night!   I will build 6 SaaS products in 2023 to reach 10k MRR and leave my corp job! I am still a lump of fresh meat here, so please follow and support my journey, and I am also open to giving it back!   Projects: - Boosted Writing: productivity tool with paid time limits (0 users) - Text2SQL.AI - Generate SQL with AI (1000 users)  Planned: GPT detector, NoCode AI builder, AI speech assistant, LinkedIn growth tool, Python analytics framework  Thanks for reading this! LINKS Text2SQL.AI INTERESTS Productivity User Experience Analytics Marketing Growth Hacking Developer Tools Artificial Intelligence Tech MAKER HISTORY Text2SQL.AI Generate SQL with AI! Jan 2023 🎉 Joined Product Hunt November 9th, 2022 Report",
            "Id Reference": "id=373699"
        }
    ]
    },
    {
        "Id": 376878,
        "Name": "Jobs Scout",
        "Tagline": "Improve your resume with the power of AI",
        "Url": "https://www.producthunt.com/posts/jobs-scout?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 90,
        "Profile_Url": "https://www.producthunt.com/@sasishan",
        "Information":  
  

    [
        {
            "All_Urls": "https://www.producthunt.com/@sasishan",
            "Profile Information": "https://www.producthunt.com/@sasishan Sasi I like to build stuff! #1700183 27 followers 36 following 16 points ☀️ 2 day streak Follow ABOUT Hey there!   I've been working in the tech industry for over 10 years now. I've always had a passion for building practical things and I think that's what led me to become a computer engineer.   I've been into tech since the days of Atari, and I've always been fascinated by the practical uses of AI. I believe that technology should be accessible to everyone and I'm dedicated to creating innovative and useful technology for the benefit of others.   When I'm not working, you can find me tinkering with new ideas or playing video games.   Thanks for stopping by! LINKS Twitter INTERESTS Productivity Artificial Intelligence Tech MAKER HISTORY Jobs Scout Improve your resume with the power of AI Jan 2023 Honcho An organizational tool built for managers by managers Apr 2019 🎉 Joined Product Hunt February 27th, 2019 Report",
            "Id Reference": "id=376878"
        }
    ]
    },
    {
        "Id": 377018,
        "Name": "What Word Is That?",
        "Tagline": "Find the right word when you need it",
        "Url": "https://www.producthunt.com/posts/what-word-is-that?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 79,
        "Profile_Url": "https://www.producthunt.com/@michael_li4",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@michael_li4",
            "Profile Information": "https://www.producthunt.com/@michael_li4 Michael Li Software Engineer #1365154 27 followers 0 following 7 points Follow ABOUT I like building cool products LINKS Website INTERESTS Productivity Task Management Home API User Experience Prototyping Internet of Things Developer Tools Artificial Intelligence Tech Games Books MAKER HISTORY What Word Is That? Find the right word when you need it Jan 2023 🎉 Joined Product Hunt July 27th, 2018 Report",
            "Id Reference": "id=377018"
        }
    ]
    },
    {
        "Id": 376967,
        "Name": "Pencil AI",
        "Tagline": "Bring you the power of GPT-3 to you on telegram.",
        "Url": "https://www.producthunt.com/posts/pencil-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Profile_Url": "https://www.producthunt.com/@arafat_akata",
        "Information":[
        {
            "All_Urls": "https://www.producthunt.com/@arafat_akata",
            "Profile Information": "https://www.producthunt.com/@arafat_akata Arafat Akata A software developer #3428828 3 followers 2 following 9 points ✨ 3 day streak Follow MAKER HISTORY Pencil AI Bring you the power of GPT-3 to you on telegram. Jan 2023 🎉 Joined Product Hunt May 24th, 2021 Report",
            "Id Reference": "id=376967"
        }
    ]
    },
    {
        "Id": 376951,
        "Name": "Vucac",
        "Tagline": "Online whiteboard collaboration tool for every team",
        "Url": "https://www.producthunt.com/posts/vucac?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 50,
        "Profile_Url": "https://www.producthunt.com/@vaux_calvert",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@vaux_calvert",
            "Profile Information": "https://www.producthunt.com/@vaux_calvert Vaux Calvert A board #4626266 1 follower 0 following 4 points Follow MAKER HISTORY Vucac Online Whiteboard Collaboration Tool for Every Team Jan 2023 🎉 Joined Product Hunt September 14th, 2022 Report",
            "Id Reference": "id=376951"
        }
    ]
    },
    {
        "Id": 376953,
        "Name": "Circle",
        "Tagline": "Buy, store, receive and send Bitcoin super fast.",
        "Url": "https://www.producthunt.com/posts/circle-98339679-23ac-4593-a2f8-b9b63a697717?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Profile_Url": "https://www.producthunt.com/@pirhofermanuel",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@pirhofermanuel",
            "Profile Information": "https://www.producthunt.com/@pirhofermanuel Manuel Pirhofer 👋 Hi, I am Manuel #4986211 2 followers 3 following 11 points Follow ABOUT Entrepreneur with 6+ years of experience.   I've created different startups in different fields (food delivery, bitcoin wallet, social commerce, e-commerce). LINKS Website Today Twitter INTERESTS Health & Fitness Design Tools Productivity User Experience Investing Bitcoin Dieting MAKER HISTORY Today Calendar designed to help you focus Feb 2023 Today A calendar designed to help you focus. Feb 2023 Circle - Social Bitcoin Wallet Buy, store, receive and send Bitcoin super fast. Jan 2023 🎉 Joined Product Hunt January 9th, 2023 Report",
            "Id Reference": "id=376953"
        }
    ]
    },
    {
        "Id": 376940,
        "Name": "Time Boxing Planner",
        "Tagline": "Take back control of your time",
        "Url": "https://www.producthunt.com/posts/time-boxing-planner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 249,
        "Profile_Url": "https://www.producthunt.com/@iamsourabhshen",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@iamsourabhshen",
            "Profile Information": "https://www.producthunt.com/@iamsourabhshen Sourabh The Notion Buddy #4529667 217 followers 16 following 98 points 🥳 12 day streak Follow ABOUT I'll help you learn and create Notion templates. LINKS Twitter Instagram Website INTERESTS Notion BADGES Gemologist 3 Top Product View all badges MAKER HISTORY Notion Template Bundle 14 Premium Notion Template wrapped in an exclusive bundle. Feb 2023 Notebook Manager Manage all your notes in beautiful and minimal Notebooks Feb 2023 Personal CRM Take your networking to the next level and stay organized. Feb 2023 Time Boxing Planner Take back control of your time. Jan 2023 Notion Personal Task HQ Get productive and stay organised with the Personal Task HQ. Jan 2023 View more Report",
            "Id Reference": "id=376940"
        }
    ]
    },
    {
        "Id": 376914,
        "Name": "Mirror",
        "Tagline": "The home for web3 publishing",
        "Url": "https://www.producthunt.com/posts/mirror-11?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 223,
        "Profile_Url": "No",
        "Information":  [{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376834,
        "Name": "Notion Ultimate Life Planner",
        "Tagline": "Plan and achieve your goals effortlessly",
        "Url": "https://www.producthunt.com/posts/notion-ultimate-life-planner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 288,
        "Profile_Url": "https://www.producthunt.com/@mitkus",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@mitkus",
            "Profile Information": "https://www.producthunt.com/@mitkus Modest Mitkus Solopreneur #3357966 1,252 followers 241 following 251 points ☀️ 2 day streak Follow ABOUT Building one-person businesses and sharing the process with others. LINKS Twitter Linkedin Website INTERESTS Productivity Notes Marketing No-Code BADGES Buddy System 3 Top Product MAKER HISTORY Notion Ultimate Productivity System Become twice productive and get things done. Feb 2023 Notion Ultimate Life Planner Plan and achieve your goals effortlessly. Jan 2023 Notion Ultimate Finance Tracker Track and manage all your finances from one place. Oct 2022 Notion Social Media Kit Plan and grow your social media channels Aug 2022 Notion Creator Course Make $2k/month selling Notion templates Jul 2022 View more Report",
            "Id Reference": "id=376834"
        }
    ]
    },
    {
        "Id": 376645,
        "Name": "AutoPay",
        "Tagline": "Automate any recurring payment activity on-chain w/ AutoPay",
        "Url": "https://www.producthunt.com/posts/autopay?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 167,
        "Profile_Url": "https://www.producthunt.com/@timbresociety, https://www.producthunt.com/@priyanshu_panda1",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@timbresociety",
            "Profile Information": "https://www.producthunt.com/@timbresociety Deep Sheth Solving problems for content creators #1871672 195 followers 40 following 168 points Follow LINKS Website BADGES 3 Top Product Veteran MAKER HISTORY AutoPay Automate any recurring payment activity on-chain w/ AutoPay Jan 2023 Fragments A platform for collective investments on-chain Aug 2022 Curato Save, curate and monetize your taste in content with Curato Mar 2022 Creator Stash Tools for creators to create, grow, and monetize Oct 2021 🎉 Joined Product Hunt August 5th, 2017 Report",
            "Id Reference": "id=376645"
        },
        {
            "All_Urls": "https://www.producthunt.com/@priyanshu_panda1",
            "Profile Information": "https://www.producthunt.com/@priyanshu_panda1 Priyanshu Panda #4536916 2 followers 0 following 22 points Follow BADGES Top Product MAKER HISTORY AutoPay Automate any recurring payment activity on-chain w/ AutoPay Jan 2023 Fragments A platform for collective investments on-chain Aug 2022 🎉 Joined Product Hunt August 22nd, 2022 Report",
            "Id Reference": "id=376645"
        }
    ]
    },
    {
        "Id": 376900,
        "Name": "IdeaTank",
        "Tagline": "Unlock opportunities through 1 on 1 connection with Ideators",
        "Url": "https://www.producthunt.com/posts/ideatank?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 137,
        "Profile_Url": "https://www.producthunt.com/@arpit_goyal_1, https://www.producthunt.com/@aakash074",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@arpit_goyal_1",
            "Profile Information": "https://www.producthunt.com/@arpit_goyal_1 Arpit Just Another Person Seeking Problems #3448669 72 followers 33 following 22 points Follow ABOUT I am working as an AR VR Developer. Interested in myriads of things.  LINKS Twitter IndieHackers Linkedin INTERESTS Productivity Crypto Developer Tools Artificial Intelligence Tech BADGES Top Product View all badges MAKER HISTORY IdeaTank - Connect 1 on 1 with Ideators Unlock Opportunities through Random Connections Jan 2023 🎉 Joined Product Hunt June 1st, 2021 Report",
            "Id Reference": "id=376900"
        },
        {
            "All_Urls": "https://www.producthunt.com/@aakash074",
            "Profile Information": "https://www.producthunt.com/@aakash074 Aakash Kumar Building IdeaTank #4992337 12 followers 2 following 12 points Follow ABOUT Entrepreneur, Tech Enthusiast, Ethical Hacker and Full Stack Developer LINKS Website Twitter INTERESTS Productivity Tech BADGES Top Product MAKER HISTORY IdeaTank - Connect 1 on 1 with Ideators Unlock Opportunities through Random Connections Jan 2023 🎉 Joined Product Hunt January 10th, 2023 Report",
            "Id Reference": "id=376900"
        }
    ]
    },
    {
        "Id": 376921,
        "Name": "Vikara",
        "Tagline": "Chatbot nutritionist to help you eat healthy",
        "Url": "https://www.producthunt.com/posts/vikara?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 96,
        "Profile_Url": "https://www.producthunt.com/@pravin_h",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@pravin_h",
            "Profile Information": "https://www.producthunt.com/@pravin_h Pravin Halady Building Vikara, a chatbot nutritionist #4978814 34 followers 10 following 29 points ☀️ 2 day streak Follow ABOUT I'm a Flutter developer and product designer. I like to build apps that help people lead happier and healthier lives.   I've built Vikara, a chatbot nutritionist to help people maintain a healthy body weight in the long-term by learning healthy eating habits. Vikara can be especially helpful to people who may at times find themselves overeating, occasionally binge eating, and who may have body image issues. But in general Vikara can benefit anyone interested in adopting long-term healthy eating habits.  Vikara 1.0 uses mindful eating practices and cognitive behavior psychology to help prevent overeating, curb binge eating, and build a positive image. I’m looking for feedback from early adopters as well as gauging interest from seed investors. LINKS Twitter Facebook LinkedIn Website INTERESTS iOS Health & Fitness Artificial Intelligence Diversity & Inclusion Illustration Comedy Nutrition MAKER HISTORY Vikara Chatbot nutritionist to help you eat healthy Jan 2023 🎉 Joined Product Hunt January 6th, 2023 Report",
            "Id Reference": "id=376921"
        }
    ]
    },
    {
        "Id": 376949,
        "Name": "Cron Jobs Expert",
        "Tagline": "Create Cron job without line of code",
        "Url": "https://www.producthunt.com/posts/cron-jobs-expert?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 87,
        "Profile_Url": "https://www.producthunt.com/@daniel_nikulshyn1",
        "Information":  
    
 
    [
        {
            "All_Urls": "https://www.producthunt.com/@daniel_nikulshyn1",
            "Profile Information": "https://www.producthunt.com/@daniel_nikulshyn1 Daniel Nikulshyn Senior 👨‍💻 #3462647 44 followers 5 following 92 points ☀️ 2 day streak Follow ABOUT Hello everyone, I am the founder of Welcome No-Code (WNC). What it is? This is a way to make the work of programmers easier and faster. We specialize in no-code solutions that we develop and manage ourselves 👨‍💻🪴  => https://www.welcomenocode.com  As for me, I have been developing for 6 years and involved in many projects. My job is to fix bugs and develop new ideas that can bring the product to life. LINKS Facebook INTERESTS Productivity User Experience Analytics Marketing Internet of Things Developer Tools Artificial Intelligence Tech No-Code Security BADGES Top Product MAKER HISTORY Cron Jobs Expert Create Cron Job Without Line Of Code Jan 2023 Code Vocations Work Less - Log More Sep 2022 QuickQuery - NoSQL database manager Seamlessly convert any database into Excel report QuickQuery 3.2 Apr 2022 QuickQuery 3.0 Feb 2022 QuickQuery - NoSQL database manager Jul 2021 🎉 Joined Product Hunt June 8th, 2021 Report",
            "Id Reference": "id=376949"
        }
    ]
    },
    {
        "Id": 376916,
        "Name": "Optic Weather",
        "Tagline": "Experience the weather like never before",
        "Url": "https://www.producthunt.com/posts/optic-weather?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Profile_Url": "https://www.producthunt.com/@tonye",
        "Information": 
 
    [
        {
            "All_Urls": "https://www.producthunt.com/@tonye",
            "Profile Information": "https://www.producthunt.com/@tonye Tonye #2924416 12 followers 0 following 13 points Follow LINKS Website Twitter MAKER HISTORY Optic Weather Experience the weather like never before Jan 2023 🎉 Joined Product Hunt October 17th, 2020 Report",
            "Id Reference": "id=376916"
        }
    ]
    },
    {
        "Id": 376917,
        "Name": "Tab Manager Auto",
        "Tagline": "Effortlessly boost your productivity with Tab Manager Auto.",
        "Url": "https://www.producthunt.com/posts/tab-manager-auto?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Profile_Url": "https://www.producthunt.com/@kevi",
        "Information":   
  
    [
        {
            "All_Urls": "https://www.producthunt.com/@kevi",
            "Profile Information": "https://www.producthunt.com/@kevi Kevin Wang Building chrome extensions. #5000605 8 followers 1 following 6 points Follow INTERESTS Productivity Fintech Email Marketing Developer Tools Artificial Intelligence Tech MAKER HISTORY Tab Manager Auto Effortlessly boost your productivity with Tab Manager Auto. Jan 2023 🎉 Joined Product Hunt January 12th, 2023 Report",
            "Id Reference": "id=376917"
        }
    ]
    },
    {
        "Id": 376633,
        "Name": "Plum Notes",
        "Tagline": "Note taking application with a different focus.",
        "Url": "https://www.producthunt.com/posts/plum-notes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Profile_Url": "https://www.producthunt.com/@plum_notes",
        "Information": [
        {
            "All_Urls": "https://www.producthunt.com/@plum_notes",
            "Profile Information": "https://www.producthunt.com/@plum_notes Ian Mora Cretor of plum notes app. #4734910 3 followers 0 following 7 points Follow INTERESTS Productivity Developer Tools Tech MAKER HISTORY Plum Notes Note taking application with a different focus. Jan 2023 🎉 Joined Product Hunt October 20th, 2022 Report",
            "Id Reference": "id=376633"
        }
    ]
    },
    {
        "Id": 375646,
        "Name": "mock.qa",
        "Tagline": "gRPC and HTTP mock APIs in the cloud",
        "Url": "https://www.producthunt.com/posts/mock-qa?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Profile_Url": "https://www.producthunt.com/@evgeniy_kosjakov, https://www.producthunt.com/@victor_vorobyev, https://www.producthunt.com/@vladimir_solovev2",
        "Information": 
    
    [
        {
            "All_Urls": "https://www.producthunt.com/@evgeniy_kosjakov",
            "Profile Information": "https://www.producthunt.com/@evgeniy_kosjakov Evgeniy Kosjakov Senior Test Automation Engineer #3616774 51 followers 5 following 32 points 🔥 56 day streak Follow LINKS GitHub Twitter INTERESTS Design Tools Marketing Developer Tools MAKER HISTORY mock.qa - gRPC and HTTP mock APIs in the cloud gRPC and HTTP mock APIs in the cloud Jan 2023 Cloudback - cloud backup service for GitHub repositories Automatic daily backups and instant restores of your GitHub repositories, metadata, and even LFS Aug 2021 🎉 Joined Product Hunt August 6th, 2021 Report",
            "Id Reference": "id=375646"
        },
        {
            "All_Urls": "https://www.producthunt.com/@victor_vorobyev",
            "Profile Information": "https://www.producthunt.com/@victor_vorobyev Victor Vorobyev Software Engineer #3654534 21 followers 8 following 10 points Follow INTERESTS Home API Analytics Marketing Developer Tools Artificial Intelligence GitHub Tech MAKER HISTORY mock.qa - gRPC and HTTP mock APIs in the cloud gRPC and HTTP mock APIs in the cloud Jan 2023 Cloudback - cloud backup service for GitHub repositories Automatic daily backups and instant restores of your GitHub repositories, metadata, and even LFS Aug 2021 🎉 Joined Product Hunt August 22nd, 2021 Report",
            "Id Reference": "id=375646"
        },
        {
            "All_Urls": "https://www.producthunt.com/@vladimir_solovev2",
            "Profile Information": "https://www.producthunt.com/@vladimir_solovev2 Vladimir Solovev Software Engineer #3654567 1 follower 0 following 4 points ☀️ 2 day streak Follow MAKER HISTORY mock.qa - gRPC and HTTP mock APIs in the cloud gRPC and HTTP mock APIs in the cloud Jan 2023 🎉 Joined Product Hunt August 22nd, 2021 Report",
            "Id Reference": "id=375646"
        }
    ]
    },
    {
        "Id": 376886,
        "Name": "OmniWork",
        "Tagline": "One link to run your business",
        "Url": "https://www.producthunt.com/posts/omniwork-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 56,
        "Profile_Url": "https://www.producthunt.com/@gomesf, https://www.producthunt.com/@sohrab_tellaie, https://www.producthunt.com/@lawchan, https://www.producthunt.com/@mazdak_sorosh, https://www.producthunt.com/@beezhan_rostaqi",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@gomesf",
            "Profile Information": "https://www.producthunt.com/@gomesf Flavio Solution Architect #4679562 0 followers 0 following 18 points ☀️ 2 day streak Follow ABOUT I am a software professional with over 6 years of experience working in the personalised, one to one customer engagement space.   During my career I have helped enterprise level clients deliver their large scale digital transformation programs, guiding them through the design and development of cutting edge software, with the primary goal of achieving better NPS and reduced churn rates.  In the last 3 years I have been an integral part of a tech consultancy, working with my team to grow it from a 4 people, 1 client organisation to a 80+ people organisation with staff and clients across multiple geographies. LINKS OmniWork INTERESTS Customer Success Software Engineering Tech Data & Analytics MAKER HISTORY OmniWork One link to run your business Jan 2023 🎉 Joined Product Hunt October 3rd, 2022 Report",
            "Id Reference": "id=376886"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sohrab_tellaie",
            "Profile Information": "https://www.producthunt.com/@sohrab_tellaie Sohrab Tellaie I'm Sohrab. CEO & Co-founder of OmniWork #4594633 7 followers 1 following 24 points Follow ABOUT My team & I, we are building OmniWork to be an all-in-one platform for individual service providers, empowering them to easily connect with their clients, create and capture that value, and be in control of their brand & reputation. LINKS Twitter OmniWork INTERESTS Productivity User Experience Marketing Tech MAKER HISTORY OmniWork One link to run your business Jan 2023 🎉 Joined Product Hunt September 4th, 2022 Report",
            "Id Reference": "id=376886"
        },
        {
            "All_Urls": "https://www.producthunt.com/@lawchan",
            "Profile Information": "https://www.producthunt.com/@lawchan Lawrence Chan Making Great Products Greater #4819038 0 followers 0 following 4 points Follow ABOUT Experienced Product Owner with exposure to both APAC and EMEA regions. Strong management consultant background in both Tier 1 Investment banks and multi-national vendors focused largely within the FinTech space, utilising technical expertise to bridge the gap and understanding between business and technology.   I also like cats. MAKER HISTORY OmniWork One link to run your business Jan 2023 🎉 Joined Product Hunt November 16th, 2022 Report",
            "Id Reference": "id=376886"
        },
        {
            "All_Urls": "https://www.producthunt.com/@mazdak_sorosh",
            "Profile Information": "https://www.producthunt.com/@mazdak_sorosh Mazdak Sorosh #4824063 1 follower 1 following 4 points Follow MAKER HISTORY OmniWork One link to run your business Jan 2023 🎉 Joined Product Hunt November 17th, 2022 Report",
            "Id Reference": "id=376886"
        },
        {
            "All_Urls": "https://www.producthunt.com/@beezhan_rostaqi",
            "Profile Information": "https://www.producthunt.com/@beezhan_rostaqi Beezhan #4818973 3 followers 0 following 4 points Follow MAKER HISTORY OmniWork One link to run your business Jan 2023 🎉 Joined Product Hunt November 16th, 2022 Report",
            "Id Reference": "id=376886"
        }
    ]
    },
    {
        "Id": 376929,
        "Name": "Dookey Dash",
        "Tagline": "Dookey Dash is a skill-based mint by Yuga Labs",
        "Url": "https://www.producthunt.com/posts/dookey-dash?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 46,
        "Profile_Url": "No",
        "Information": [{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376772,
        "Name": "Calendar Query",
        "Tagline": "Query your Google Calendar with SQL",
        "Url": "https://www.producthunt.com/posts/calendar-query?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 41,
        "Profile_Url": "https://www.producthunt.com/@dbradleyfl",
        "Information": 
  
    [
        {
            "All_Urls": "https://www.producthunt.com/@dbradleyfl",
            "Profile Information": "https://www.producthunt.com/@dbradleyfl Devon Bradley Shipping software products 🚀 #522593 102 followers 158 following 42 points Follow LINKS Twitter Website INTERESTS Web App Virtual Reality Productivity API Open Source Twitter Social Network Growth Hacking Global Nomad TV Streaming Services Developer Tools Augmented Reality GitHub Snapchat Search BADGES Veteran MAKER HISTORY Calendar Query Query your Google Calendar with SQL Jan 2023 Motion Security Cam Turn your laptop or mobile device into a motion camera alarm Jul 2020 Couch Live Your virtual living room for watching TV with friends! Mar 2020 Macbar Next Bus A free mac menubar application for bus stop departures! Oct 2017 🎉 Joined Product Hunt April 15th, 2016 Report",
            "Id Reference": "id=376772"
        }
    ]
    },
    {
        "Id": 376743,
        "Name": "Furmasterpiece Pet Avatar Creator",
        "Tagline": "Furmasterpiece turns any pet photo into a stunning avatar",
        "Url": "https://www.producthunt.com/posts/furmasterpiece-pet-avatar-creator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Profile_Url": "https://www.producthunt.com/@rando_tkatsenko",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@rando_tkatsenko",
            "Profile Information": "https://www.producthunt.com/@rando_tkatsenko Rando Tkatsenko Building cool stuff with Unity- VR, AI. #4942150 6 followers 0 following 3 points Follow INTERESTS Productivity Artificial Intelligence Tech MAKER HISTORY Furmasterpiece - Pet Avatar Creator Furmasterpiece turns any pet photo into a stunning avatar. Jan 2023 🎉 Joined Product Hunt December 21st, 2022 Report",
            "Id Reference": "id=376743"
        }
    ]
    },
    {
        "Id": 376937,
        "Name": "GiftBot: Love Edition",
        "Tagline": "Valentines Day gift help from a GPT-3 chatbot",
        "Url": "https://www.producthunt.com/posts/giftbot-love-edition?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 40,
        "Profile_Url": "https://www.producthunt.com/@thiteanish",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@thiteanish",
            "Profile Information": "https://www.producthunt.com/@thiteanish Anish Thite Master procrastinator #3073292 43 followers 293 following 39 points Follow LINKS Website Twitter BADGES Top Product MAKER HISTORY GiftBot Holiday Gift Help from a GPT-3 chatbot GiftBot: Love Edition Jan 2023 GiftBot Dec 2022 Circle GPT-3 powered bots Dec 2020 🎉 Joined Product Hunt December 20th, 2020 Report",
            "Id Reference": "id=376937"
        }
    ]
    },
    {
        "Id": 376701,
        "Name": "Internet Is Beautiful",
        "Tagline": "Discover the most interesting, weird and awesome websites",
        "Url": "https://www.producthunt.com/posts/internet-is-beautiful?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 747,
        "Profile_Url": "https://www.producthunt.com/@jaisalr",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@jaisalr",
            "Profile Information": "https://www.producthunt.com/@jaisalr Jaisal Rathee Building www.startups.fyi 🦄 #2711861 220 followers 17 following 887 points ✨ 3 day streak Follow LINKS Website INTERESTS Productivity Growth Hacking BADGES 6 Top Product View all badges MAKER HISTORY Startup Money Free Database of 2,000+ Startup Incubators and Accelerators Feb 2023 Internet Is Beautiful Discover the most interesting, weird and awesome websites. Jan 2023 Supernuclear A guide to coliving Jan 2023 Startups.fyi Discover the best free tools for startup founders Startups.fyi Dec 2022 Startups.fyi May 2022 Billion Dollar Business Ideas Discover billion dollar business ideas for your next project Sep 2022 View more Report",
            "Id Reference": "id=376701"
        }
    ]
    },
    {
        "Id": 376690,
        "Name": "WorkHub Connect for Mobile",
        "Tagline": "External and Internal communication on the go",
        "Url": "https://www.producthunt.com/posts/workhub-connect-for-mobile?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 651,
        "Profile_Url": "https://www.producthunt.com/@hamza_afzal_butt, https://www.producthunt.com/@qudsia_ali, https://www.producthunt.com/@sidraarifali, https://www.producthunt.com/@noshaid, https://www.producthunt.com/@bilal_anwar1, https://www.producthunt.com/@aqsa_sajjad, https://www.producthunt.com/@nabeel_amir, https://www.producthunt.com/@ali_shaheen",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@hamza_afzal_butt",
            "Profile Information": "https://www.producthunt.com/@hamza_afzal_butt Hamza Afzal Butt B2B SaaS Growth Marketing Consultant #3830504 348 followers 67 following 501 points ☀️ 2 day streak Follow ABOUT I am a B2B SaaS digital marketing manager with over ten years of experience. I am passionate about my job and staying up-to-date with the latest trends and technologies in the marketing field. My expertise is SEO, Social Media Marketing, and producing engaging online content with working knowledge of SEO practices. I have experience with CMS, ESP, and HTML too. Currently, I am responsible for developing and executing marketing strategies that drive growth and customer acquisition through inbound and outbound marketing, content creation, and lead generation. WORK Marketing Manager at WorkHub LINKS Twitter LinkedIn INTERESTS Android iOS Web App Slack Virtual Reality Email Health & Fitness Task Management Music Messaging Open Source Writing User Experience Social Network Social Media Analytics Prototyping Marketing Education Growth Hacking BADGES Contributor Top Product View all badges MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Jan 2023 🎉 Joined Product Hunt November 2nd, 2021 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@qudsia_ali",
            "Profile Information": "https://www.producthunt.com/@qudsia_ali Qudsia Ali Director at WorkHub #4136209 747 followers 278 following 2,718 points ☀️ 2 day streak Follow LINKS Twitter LinkedIn Website INTERESTS Design Tools Analytics Marketing Growth Hacking Internet of Things SaaS Developer Tools Tech BADGES Buddy System Contributor Gemologist View all badges MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform WorkHub Connect for Mobile Jan 2023 WorkHub eSignature Nov 2022 WorkHub Scheduling Sep 2022 WorkHub Sep 2022 WorkHub Spaces Aug 2022 BRAVO! Jul 2022 Bravo for Android & iOS Celebrate Wins On The Go Dec 2022 🎉 Joined Product Hunt March 10th, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sidraarifali",
            "Profile Information": "https://www.producthunt.com/@sidraarifali Sidra Ali Founder @Vadoreu #4254865 66 followers 28 following 203 points ☀️ 2 day streak Follow LINKS Website Linkedin BADGES Top Product MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Jan 2023 🎉 Joined Product Hunt April 29th, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@noshaid",
            "Profile Information": "https://www.producthunt.com/@noshaid Noshaid Ali Senior Software Engineer #4737016 10 followers 24 following 81 points Follow ABOUT Mobile Application Lead @ WorkHub LINKS GitHub Twitter Linkedin INTERESTS User Experience Developer Tools Tech Apple BADGES Top Product MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Jan 2023 🎉 Joined Product Hunt October 21st, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@bilal_anwar1",
            "Profile Information": "https://www.producthunt.com/@bilal_anwar1 Bilal Anwar Mobile App Developer @ Workhub #4219262 31 followers 8 following 144 points Follow INTERESTS Productivity User Experience Analytics Developer Tools Tech BADGES Top Product MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Jan 2023 🎉 Joined Product Hunt April 12th, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@aqsa_sajjad",
            "Profile Information": "https://www.producthunt.com/@aqsa_sajjad Aqsa Sajjad Digital Marketing #4276310 95 followers 22 following 417 points Follow LINKS Linkedin BADGES Gemologist Top Product View all badges MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Jan 2023 🎉 Joined Product Hunt May 9th, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@nabeel_amir",
            "Profile Information": "https://www.producthunt.com/@nabeel_amir Nabeel Amir I am the Product Owner @ WorkHub #4136648 178 followers 83 following 756 points Follow LINKS Website INTERESTS iOS Web App Task Management Software Engineering Developer Tools Tech BADGES Buddy System Contributor Gemologist View all badges MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform Apr 2022 🎉 Joined Product Hunt March 10th, 2022 Report",
            "Id Reference": "id=376690"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ali_shaheen",
            "Profile Information": "https://www.producthunt.com/@ali_shaheen Ali Naqi Shaheen Entrepreneur, Angel Investor #617409 220 followers 445 following 478 points ☀️ 2 day streak Follow LINKS Twitter Website INTERESTS Design Tools API User Experience Analytics Education Artificial Intelligence BADGES 2 Top Product Veteran View all badges MAKER HISTORY WorkHub AI driven team communication, collaboration, recognition and rewards platform WorkHub Connect for Mobile Jan 2023 WorkHub Connect Apr 2022 Bravo for Android & iOS Celebrate Wins On The Go Dec 2022 BullsBot Your trading assistant Feb 2021 🎉 Joined Product Hunt July 27th, 2016 Report",
            "Id Reference": "id=376690"
        }
    ]
    },
    {
        "Id": 376172,
        "Name": "The Help Center Academy",
        "Tagline": "Learn the secrets of building a successful help center",
        "Url": "https://www.producthunt.com/posts/the-help-center-academy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 332,
        "Profile_Url": "https://www.producthunt.com/@sobedominik",
        "Information":  
 
 
  
    [
        {
            "All_Urls": "https://www.producthunt.com/@sobedominik",
            "Profile Information": "https://www.producthunt.com/@sobedominik Dominik Sobe ⚡Indie Hacker building interweb products #1485377 1,702 followers 601 following 431 points Follow LINKS Website Twitter INTERESTS Analytics SaaS BADGES Gemologist 3 Top Product MAKER HISTORY The Help Center Academy Learn the secrets of building a successful help center Jan 2023 HelpKit Knowledge Base Build a professional help center or doc site with Notion Aug 2022 Notion Simple Table by HelpKit A free table generator for Notion using the equation block Sep 2021 ProductFlair Curated Product Hunt launch inspiration, tips and more Mar 2021 The only love letter you'll need Nothing says love like cold hard facts Feb 2021 View more Report",
            "Id Reference": "id=376172"
        }
    ]
    },
    {
        "Id": 376770,
        "Name": "Makelog",
        "Tagline": "Autogenerate your changelog with GPT-3",
        "Url": "https://www.producthunt.com/posts/makelog?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 286,
        "Profile_Url": "https://www.producthunt.com/@juliejennifernguyen, https://www.producthunt.com/@britonbaker, https://www.producthunt.com/@julio_farah, https://www.producthunt.com/@hubbardjacob, https://www.producthunt.com/@loganliffick",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@juliejennifernguyen",
            "Profile Information": "https://www.producthunt.com/@juliejennifernguyen JJ Nguyen #2806365 395 followers 355 following 44 points Follow LINKS Twitter MAKER HISTORY Makelog Autogenerate your changelog with GPT-3 + share to Slack, email + more! Jan 2023 🎉 Joined Product Hunt August 23rd, 2020 Report",
            "Id Reference": "id=376770"
        },
        {
            "All_Urls": "https://www.producthunt.com/@britonbaker",
            "Profile Information": "https://www.producthunt.com/@britonbaker Briton Baker Product Designer #3080336 3 followers 7 following 26 points Follow LINKS Website MAKER HISTORY Makelog Autogenerate your changelog with GPT-3 + share to Slack, email + more! Jan 2023 🎉 Joined Product Hunt December 23rd, 2020 Report",
            "Id Reference": "id=376770"
        },
        {
            "All_Urls": "https://www.producthunt.com/@julio_farah",
            "Profile Information": "https://www.producthunt.com/@julio_farah Julio Farah f #3175551 2 followers 52 following 28 points ☀️ 2 day streak Follow MAKER HISTORY Makelog Autogenerate your changelog with GPT-3 + share to Slack, email + more! Jan 2023 🎉 Joined Product Hunt January 31st, 2021 Report",
            "Id Reference": "id=376770"
        },
        {
            "All_Urls": "https://www.producthunt.com/@hubbardjacob",
            "Profile Information": "https://www.producthunt.com/@hubbardjacob Jacob Hubbard building makelog #4975999 1 follower 3 following 27 points Follow INTERESTS User Experience Developer Tools Tech MAKER HISTORY Makelog Autogenerate your changelog with GPT-3 + share to Slack, email + more! Jan 2023 🎉 Joined Product Hunt January 5th, 2023 Report",
            "Id Reference": "id=376770"
        },
        {
            "All_Urls": "https://www.producthunt.com/@loganliffick",
            "Profile Information": "https://www.producthunt.com/@loganliffick Logan Liffick Senior Designer at DigitalOcean #3905664 12 followers 0 following 26 points Follow ABOUT Designer and creative engineer working to build software that people care about. LINKS loganliffick.com INTERESTS Design Tools Productivity Developer Tools Tech MAKER HISTORY Makelog Autogenerate your changelog with GPT-3 + share to Slack, email + more! Jan 2023 🎉 Joined Product Hunt December 5th, 2021 Report",
            "Id Reference": "id=376770"
        }
    ]
    },
    {
        "Id": 375921,
        "Name": "Pitchdeck Challenge",
        "Tagline": "10 Days to master your pitchdeck creation",
        "Url": "https://www.producthunt.com/posts/pitchdeck-challenge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 269,
        "Profile_Url": "https://www.producthunt.com/@derstartupcfo",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@derstartupcfo",
            "Profile Information": "https://www.producthunt.com/@derstartupcfo Sebastian Janus - derStartupCFO Founder & Serial Entrepreneur #3086104 362 followers 279 following 545 points Follow ABOUT An energetic, pragmatic, and passionate entrepreneur with extensive experience in building and scaling digital business models + managed two company exits in the last 20 years, including 4 years as the CFO at Foot Locker for the e-commerce business in Europe, then travelling around the world for more than 10 months.  I prefer to call myself \"derstartupcfo\". 🔥  Currently, CEO & Founder of nugrow, which is the leading boutique consultancy specialized in providing strategic & operative consulting alongside support and leadership to startups, scale-ups & grown-ups.  LINKS Twitter Website LinkedIn nugrow INTERESTS Marketing Venture Capital SaaS E-Commerce Tech Fundraising BADGES Buddy System Gemologist Thought Leader View all badges MAKER HISTORY Pitchdeck Challenge 10 Days to Master your Pitchdeck Creation Jan 2023 PitchCheck Step by step instructions to the perfect Pitch Deck Dec 2022 Diversity.wiki World's largest directory for diversity & inclusion May 2022 🎉 Joined Product Hunt December 27th, 2020 Report",
            "Id Reference": "id=375921"
        }
    ]
    },
    {
        "Id": 376388,
        "Name": "Inside AI",
        "Tagline": "The most complete AI Newsletter",
        "Url": "https://www.producthunt.com/posts/inside-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 402,
        "Profile_Url": "https://www.producthunt.com/@jan_sulek",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@jan_sulek",
            "Profile Information": "https://www.producthunt.com/@jan_sulek Jan Sulek AI Newsletter - insideai.co #4877025 5 followers 1 following 32 points Follow LINKS AI Newsletter - Inside AI INTERESTS Productivity Fintech Marketing Artificial Intelligence Tech BADGES Top Product MAKER HISTORY Inside AI The most complete AI Newsletter Jan 2023 🎉 Joined Product Hunt December 5th, 2022 Report",
            "Id Reference": "id=376388"
        }
    ]
    },
    {
        "Id": 376177,
        "Name": "Product Launch AI",
        "Tagline": "Supercharge your Product Launches with the Power of AI",
        "Url": "https://www.producthunt.com/posts/product-launch-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 218,
        "Profile_Url": "https://www.producthunt.com/@adithya",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@adithya",
            "Profile Information": "https://www.producthunt.com/@adithya Adithya Shreshti Startup Launch & NoCode Consultant #443764 1,731 followers 357 following 4,290 points 🔥 74 day streak Follow ABOUT Among top Product Hunters. 225+ hunts and launches over the last many years.   As a NoCode Catalyst and Startup Launch Consultant I have had the opportunity and privilege to converse with 100s of founders/makers to help in the process of building their product and guide them through the process of launch to achieve excellent initial traction and get the ball rolling.   Conversations/Workshops with tons of aspiring creators and makers and more.  You can checkout my website or my timeline to know more. LINKS Join NoCode Tribe View my Timeline Follow on Twitter INTERESTS Windows Slack Email Productivity News Messaging Video Streaming Home Art API Open Source Writing Notes Twitter Social Media Prototyping Customer Communication Typography Marketing Advertising BADGES Beta Tester Gemologist Thought Leader View all badges MAKER HISTORY Product Launch AI Unleash the power of AI to supercharge your product launches Jan 2023 NoCode Stash Discover the best of no-code for your next maker project Nov 2021 Open Source Stash The best open-source alternatives for you next maker project Dec 2020 Knowmad Life A platform connecting you to other digital nomads 🌎 Oct 2017 🎉 Joined Product Hunt February 4th, 2016 Report",
            "Id Reference": "id=376177"
        }
    ]
    },
    {
        "Id": 376859,
        "Name": "MusicLM by Google",
        "Tagline": "A text to music AI model by Google",
        "Url": "https://www.producthunt.com/posts/musiclm-by-google?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 190,
        "Profile_Url": "No",
        "Information":[{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376393,
        "Name": "Casper",
        "Tagline": "GPT-3 in your iPhone keyboard",
        "Url": "https://www.producthunt.com/posts/casper-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 200,
        "Profile_Url": "https://www.producthunt.com/@johan_v1",
        "Information":  
  
    [
        {
            "All_Urls": "https://www.producthunt.com/@johan_v1",
            "Profile Information": "https://www.producthunt.com/@johan_v1 Johan Building and thinking AI stuff #4613682 25 followers 4 following 119 points Follow INTERESTS Design Tools Developer Tools Artificial Intelligence Tech BADGES Top Product View all badges MAKER HISTORY AI Builders - Building the future The WhatsApp group for founders, devs and builders in Gen AI Mar 2023 Frank One AI Assistant across Web, App and Keyboard Feb 2023 Casper GPT-3 in your iPhone Keyboard Jan 2023 Albert The AI-powered search & content creation app Dec 2022 Dreamland Discover and buy AI generated visuals, images and content. Sep 2022 🎉 Joined Product Hunt September 11th, 2022 Report",
            "Id Reference": "id=376393"
        }
    ]
    },
    {
        "Id": 376755,
        "Name": "Social Media Manager",
        "Tagline": "Plan your social media content like a pro",
        "Url": "https://www.producthunt.com/posts/social-media-manager-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 94,
        "Profile_Url": "https://www.producthunt.com/@heyynoon",
        "Information":
 
    [
        {
            "All_Urls": "https://www.producthunt.com/@heyynoon",
            "Profile Information": "https://www.producthunt.com/@heyynoon Brian Product Designer & Notion Creator #4570937 178 followers 52 following 70 points Follow ABOUT Product Designer & Notion Creator • Building productivity systems in Notion • Helping you to be productive, not busy. LINKS Website Products Twitter Instagram INTERESTS Productivity User Experience Education UX Design Notion MAKER HISTORY Social Media Manager Plan your social media content like a pro. Jan 2023 Twitter Content Hub Notion dashboard Write, plan and organize your Twitter content with ease. Dec 2022 Notion Resume Builder Build your resume easily within Notion Nov 2022 Notion CRM System Capture leads, increase sales, organize your contacts. Oct 2022 Habit Journal Your daily companion for routines, habits and reflections. Oct 2022 View more Report",
            "Id Reference": "id=376755"
        }
    ]
    },
    {
        "Id": 376125,
        "Name": "dbt-infer",
        "Tagline": "Next-Gen analytics for dbt, supercharge models with Infer",
        "Url": "https://www.producthunt.com/posts/dbt-infer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 86,
        "Profile_Url": "https://www.producthunt.com/@ryanrgarland, https://www.producthunt.com/@erik_mathiesen_dreyfus",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@ryanrgarland",
            "Profile Information": "https://www.producthunt.com/@ryanrgarland Ryan Garland Hello! #4554646 0 followers 0 following 9 points Follow MAKER HISTORY Infer Next-Gen Analytics for dbt. Supercharge models with Infer. Jan 2023 🎉 Joined Product Hunt August 25th, 2022 Report",
            "Id Reference": "id=376125"
        },
        {
            "All_Urls": "https://www.producthunt.com/@erik_mathiesen_dreyfus",
            "Profile Information": "https://www.producthunt.com/@erik_mathiesen_dreyfus Erik Mathiesen-Dreyfus Founder@Infer #4564117 7 followers 0 following 20 points Follow ABOUT Hi! I am Erik - co-founder of Infer.  At Infer we are building a new generation of data exploration and research tools focused around giving analysts the tools to do better analysis using machine learning.  Previously, I led and built data science and analytics teams at a few different companies - mainly scaleups. I also founded two companies around machine learning and analytics. One in recruitment and one in risk management.  Prior to that I was a quant at a number of investment banks and an academic working on mathematical logic and the foundations of computation.  I am also co-organiser of MancML - a quarterly-ish machine learning conference in Manchester, with offsprings in Leeds and Edinburgh. LINKS Infer LinkedIn INTERESTS Data & Analytics Data Science MAKER HISTORY Infer Next-Gen Analytics for dbt. Supercharge models with Infer. Jan 2023 🎉 Joined Product Hunt August 26th, 2022 Report",
            "Id Reference": "id=376125"
        }
    ]
    },
    {
        "Id": 376565,
        "Name": "The Guest Posts App",
        "Tagline": "A new way to find guest posts faster",
        "Url": "https://www.producthunt.com/posts/the-guest-posts-app?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 82,
        "Profile_Url": "https://www.producthunt.com/@siddharth_verma1",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@siddharth_verma1",
            "Profile Information": "https://www.producthunt.com/@siddharth_verma1 Siddharth Verma SAAS Consultant | Startups | AI/NLP #1435795 3 followers 0 following 38 points Follow ABOUT Hi, I am Siddharth Verma. A start-up enthusiast with 6+ years of experience. I have worked with over 50+ SAAS companies helping them build robust scalable solutions, product and engineering problems. I am a full-stack developer with a knack for marketing and product development. LINKS Twitter Linkedin INTERESTS Productivity Marketing Developer Tools Artificial Intelligence MAKER HISTORY The Guest Posts App A New Way To Find Guest Posts Faster Jan 2023 One Click Article Generator 500-800 Words Comprehensive Articles In A Single Click Jan 2023 Linkedin Posts Generator Generate Linkedin Posts In Seconds From Articles Jan 2023 Best Tools For Your SAAS Product A curated list of 72 tools. Filter and Save your picks Oct 2022 🎉 Joined Product Hunt September 21st, 2018 Report",
            "Id Reference": "id=376565"
        }
    ]
    },
    {
        "Id": 376789,
        "Name": "hai Infusions Smart Showerhead",
        "Tagline": "Your daily shower, reimagined with smart tech",
        "Url": "https://www.producthunt.com/posts/hai-infusions-smart-showerhead?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 209,
        "Profile_Url": "https://www.producthunt.com/@leah_stigile, https://www.producthunt.com/@gina_oh, https://www.producthunt.com/@kate_starr, https://www.producthunt.com/@monika_markovinovic, https://www.producthunt.com/@lbrody, https://www.producthunt.com/@madi_fisk",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@leah_stigile",
            "Profile Information": "https://www.producthunt.com/@leah_stigile Leah Stigile Co-founder & CEO #5026146 7 followers 6 following 27 points ☀️ 2 day streak Follow BADGES Buddy System MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt January 18th, 2023 Report",
            "Id Reference": "id=376789"
        },
        {
            "All_Urls": "https://www.producthunt.com/@gina_oh",
            "Profile Information": "https://www.producthunt.com/@gina_oh Gina Oh Cofounder #5049098 2 followers 0 following 8 points Follow MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt January 20th, 2023 Report",
            "Id Reference": "id=376789"
        },
        {
            "All_Urls": "https://www.producthunt.com/@kate_starr",
            "Profile Information": "https://www.producthunt.com/@kate_starr Kate Starr VP and storyteller of amazing showers. #4992957 5 followers 4 following 16 points Follow INTERESTS Marketing MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt January 10th, 2023 Report",
            "Id Reference": "id=376789"
        },
        {
            "All_Urls": "https://www.producthunt.com/@monika_markovinovic",
            "Profile Information": "https://www.producthunt.com/@monika_markovinovic Monika Markovinovic content person. loves the internet. #5048420 2 followers 5 following 15 points Follow INTERESTS Marketing Internet of Things Biohacking MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt January 20th, 2023 Report",
            "Id Reference": "id=376789"
        },
        {
            "All_Urls": "https://www.producthunt.com/@lbrody",
            "Profile Information": "https://www.producthunt.com/@lbrody Leonard Brody CEO #50765 326 followers 140 following 8 points Follow LINKS Twitter BADGES Veteran MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt August 23rd, 2014 Report",
            "Id Reference": "id=376789"
        },
        {
            "All_Urls": "https://www.producthunt.com/@madi_fisk",
            "Profile Information": "https://www.producthunt.com/@madi_fisk Madi Fisk Intern @hai #5072272 3 followers 2 following 8 points Follow INTERESTS Biohacking Climate Tech Quantified Self MAKER HISTORY hai Infusions Smart Showerhead Your daily shower, reimagined with smart tech. Jan 2023 🎉 Joined Product Hunt January 24th, 2023 Report",
            "Id Reference": "id=376789"
        }
    ]
    },
    {
        "Id": 376731,
        "Name": "Welma",
        "Tagline": "Understand and retain complex text with the help of AI",
        "Url": "https://www.producthunt.com/posts/welma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 75,
        "Profile_Url": "https://www.producthunt.com/@verfasor",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@verfasor",
            "Profile Information": "https://www.producthunt.com/@verfasor Mighil globe-earther and schnauzer enthusiast #3955223 127 followers 1 following 175 points ☀️ 2 day streak Follow ABOUT Seasoned professional with diverse work experience in marketing and technology. In my free time, I enjoy reading, writing, tinkering, and experimenting new sound design techniques. Key member of EarlyBird, HeyForm, and TinySnap. I'm down for a coffee and chinwag if you're in Chengdu. Weixin @mighil. LINKS side dishes mighil.com portfolio old blog INTERESTS Productivity Writing User Experience Marketing Developer Tools BADGES Gemologist Top Product View all badges MAKER HISTORY GPT 3.5 Turbo Playground A micro app to try the new ChatGPT API Mar 2023 SEO Stan An AI-powered micro SEO tool for bloggers and makers Feb 2023 Linked XP Elevate your LinkedIn game Feb 2023 This Product Does Not Exist Reinventing the wheel. One AI-generated product at a time. Jan 2023 Welma Understand and retain complex text with the help of AI Jan 2023 View more Report",
            "Id Reference": "id=376731"
        }
    ]
    },
    {
        "Id": 376786,
        "Name": "Followup Fish",
        "Tagline": "Bubble up emails back to the top of your inbox",
        "Url": "https://www.producthunt.com/posts/followup-fish?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 67,
        "Profile_Url": "https://www.producthunt.com/@marckohlbrugge",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@marckohlbrugge",
            "Profile Information": "https://www.producthunt.com/@marckohlbrugge Marc Köhlbrugge Founder of BetaList #497 16,734 followers 131 following 3,002 points ☀️ 2 day streak Follow LINKS Twitter Website INTERESTS Task Management BADGES 13 Top Product Veteran View all badges MAKER HISTORY This Job Does Not Exist Jobs of the future, imagined by AI Mar 2023 Startup Jobs Join a startup. Build the future. Interview Questions Mar 2023 Startup Jobs Sep 2018 Followup Fish Bubble up emails back to the top of your inbox 🐟 Jan 2023 Handle Horse Monitor when your desired Twitter handle becomes available Dec 2022 AI Jobs Apply to 1,000+ jobs in AI and Machine Learning Nov 2022 View more Report",
            "Id Reference": "id=376786"
        }
    ]
    },
    {
        "Id": 376802,
        "Name": "Extractify",
        "Tagline": "Convert Youtube videos into Tweets and LinkedIn posts",
        "Url": "https://www.producthunt.com/posts/extractify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Profile_Url": "https://www.producthunt.com/@ahsan_shahid",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@ahsan_shahid",
            "Profile Information": "https://www.producthunt.com/@ahsan_shahid Ahsan Shahid Builder #4339504 2 followers 0 following 10 points Follow INTERESTS Productivity Marketing Tech MAKER HISTORY Extractify Convert Youtube videos into Tweets and LinkedIn posts Jan 2023 🎉 Joined Product Hunt June 3rd, 2022 Report",
            "Id Reference": "id=376802"
        }
    ]
    },
    {
        "Id": 375422,
        "Name": "Spot a Bot",
        "Tagline": "Get insights into the bot activity for Twitter trends",
        "Url": "https://www.producthunt.com/posts/spot-a-bot?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 77,
        "Profile_Url": "https://www.producthunt.com/@nicolas_graf, https://www.producthunt.com/@kevin_harizaj, https://www.producthunt.com/@lener, https://www.producthunt.com/@dadonia_",
        "Information":    [
        {
            "All_Urls": "https://www.producthunt.com/@nicolas_graf",
            "Profile Information": "https://www.producthunt.com/@nicolas_graf Nicolas Graf Heavy web consumer and creator. #4992419 16 followers 4 following 7 points Follow LINKS Twitter INTERESTS User Experience Twitter Social Network Artificial Intelligence Tech Web Design MAKER HISTORY Spot A Bot Get insights into the bot activity for Twitter trends Jan 2023 🎉 Joined Product Hunt January 10th, 2023 Report",
            "Id Reference": "id=375422"
        },
        {
            "All_Urls": "https://www.producthunt.com/@kevin_harizaj",
            "Profile Information": "https://www.producthunt.com/@kevin_harizaj Kevin Harizaj Developer #4996795 3 followers 11 following 10 points Follow LINKS Twitter MAKER HISTORY Spot A Bot Get insights into the bot activity for Twitter trends Jan 2023 🎉 Joined Product Hunt January 11th, 2023 Report",
            "Id Reference": "id=375422"
        },
        {
            "All_Urls": "https://www.producthunt.com/@lener",
            "Profile Information": "https://www.producthunt.com/@lener Lena Heiglauer Developer @ Spot A Bot #4049106 10 followers 6 following 16 points Follow MAKER HISTORY Spot A Bot Get insights into the bot activity for Twitter trends Jan 2023 🎉 Joined Product Hunt February 1st, 2022 Report",
            "Id Reference": "id=375422"
        },
        {
            "All_Urls": "https://www.producthunt.com/@dadonia_",
            "Profile Information": "https://www.producthunt.com/@dadonia_ Daniela Dottolo Web Development student from Austria 🌈 #5012622 13 followers 3 following 14 points Follow INTERESTS Developer Tools Artificial Intelligence Tech MAKER HISTORY Spot A Bot Get insights into the bot activity for Twitter trends Jan 2023 🎉 Joined Product Hunt January 15th, 2023 Report",
            "Id Reference": "id=375422"
        }
    ]
    },
    {
        "Id": 376669,
        "Name": "Semantic AI",
        "Tagline": "The fullstack AI writing suite, that gives you back control",
        "Url": "https://www.producthunt.com/posts/semantic-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 52,
        "Profile_Url": "https://www.producthunt.com/@amartya_varma",
        "Information":   [
        {
            "All_Urls": "https://www.producthunt.com/@amartya_varma",
            "Profile Information": "https://www.producthunt.com/@amartya_varma Amu Founder of Sentiment #3598879 19 followers 1 following 33 points ✨ 3 day streak Follow LINKS Website INTERESTS Developer Tools Artificial Intelligence Tech BADGES Gemologist View all badges MAKER HISTORY Ensurit Integrated tools for teachers to detect AI Feb 2023 Semantic AI The fullstack AI writing suite, that gives you back control! Jan 2023 Whiskey AI Get your thoughts down faster than ever Jan 2023 Semantic AI-based search and question answering in a hosted database Jun 2022 Sentiment Opensource APIs for stock social media data Aug 2021 🎉 Joined Product Hunt July 31st, 2021 Report",
            "Id Reference": "id=376669"
        }
    ]
    },
    {
        "Id": 376685,
        "Name": "MailGPT",
        "Tagline": "Experience the convenience",
        "Url": "https://www.producthunt.com/posts/mailgpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 48,
        "Profile_Url": "https://www.producthunt.com/@sourav204",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@sourav204",
            "Profile Information": "https://www.producthunt.com/@sourav204 Sourav Kumar Pradhan Developer #985273 60 followers 70 following 52 points Follow INTERESTS Web App Chrome Extensions API Open Source WordPress Developer Tools Bots BADGES Veteran MAKER HISTORY MailGPT - AI powered email generator. Experience the convenience Jan 2023 Advanced Twitter Search v2 Unlock the hidden gems of Twitter. Jun 2021 Advanced Twitter Search Unlock the hidden gems of Twitter. Jul 2020 AFS Prime Perform Facebook graph searches. Jul 2019 AFS (Advanced Facebook Search) Find stories, connections and photos of people on Facebook Aug 2017 🎉 Joined Product Hunt August 26th, 2017 Report",
            "Id Reference": "id=376685"
        }
    ]
    },
    {
        "Id": 376717,
        "Name": "Multichain Playbook",
        "Tagline": "Unlock the potential of NFT Project with multichain playbook",
        "Url": "https://www.producthunt.com/posts/multichain-playbook?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Profile_Url": "https://www.producthunt.com/@dineshkruplani, https://www.producthunt.com/@ramees_p_s, https://www.producthunt.com/@gitgat, https://www.producthunt.com/@sahil639, https://www.producthunt.com/@avinash_kumar31, https://www.producthunt.com/@harikrishnaraj",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@dineshkruplani",
            "Profile Information": "https://www.producthunt.com/@dineshkruplani Dinesh Kruplani Growth & Marketing at Dehidden #3696955 50 followers 115 following 39 points ☀️ 2 day streak Follow ABOUT 👋 Hi, I’m Dinesh Kruplani  I’m currently working at Dehidden, a web3 CRM tool, we've worked with 25+ clients, including Coinbase, Flipkart, Adidas, Prada and more!   Previously built and sold a social gaming and esports platform with 50,000+ users.   Apart from this, I love cooking, reading business, finance and psychology books. Happy to connect and explore synergies. LINKS Twitter INTERESTS Newsletters User Experience Public Relations Twitter Branding Marketing Startup Books Growth Hacking Advertising Crypto Growth Hacks Web3 Ethereum Bitcoin DAO DApp Cryptocurrency Blockchain DeFi Marketing calendar BADGES Top Product MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 NFT Wrapped Experience your 2022 NFT journey the Degen way! Dec 2022 🎉 Joined Product Hunt September 8th, 2021 Report",
            "Id Reference": "id=376717"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ramees_p_s",
            "Profile Information": "https://www.producthunt.com/@ramees_p_s Ramees P S Product | Growth | Crypto #3064307 53 followers 42 following 66 points ✨ 3 day streak Follow LINKS Website BADGES 2 Top Product MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 NFT Wrapped Experience your 2022 NFT journey the Degen way! Dec 2022 MovingOn Go back in time and find your missed crypto investments Jun 2021 🎉 Joined Product Hunt December 16th, 2020 Report",
            "Id Reference": "id=376717"
        },
        {
            "All_Urls": "https://www.producthunt.com/@gitgat",
            "Profile Information": "https://www.producthunt.com/@gitgat Sangeet Muralidhar building stuff #5075749 1 follower 0 following 3 points Follow INTERESTS Tech MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 🎉 Joined Product Hunt January 25th, 2023 Report",
            "Id Reference": "id=376717"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sahil639",
            "Profile Information": "https://www.producthunt.com/@sahil639 Sahil Pednekar Product Designer, NFT Artist #3952116 55 followers 101 following 78 points Follow ABOUT Designing products and visuals for web3. Scaling mountains and products. Cat lover LINKS Twitter Behance INTERESTS Web App Design Tools Productivity User Experience Prototyping Growth Hacking Artificial Intelligence Product Hunt Bots Tech Books BADGES Gemologist Top Product MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 NFT Wrapped Experience your 2022 NFT journey the Degen way! Dec 2022 🎉 Joined Product Hunt December 29th, 2021 Report",
            "Id Reference": "id=376717"
        },
        {
            "All_Urls": "https://www.producthunt.com/@avinash_kumar31",
            "Profile Information": "https://www.producthunt.com/@avinash_kumar31 Avinash Kumar Product Designer #4962795 2 followers 0 following 3 points Follow LINKS Twitter MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 🎉 Joined Product Hunt December 29th, 2022 Report",
            "Id Reference": "id=376717"
        },
        {
            "All_Urls": "https://www.producthunt.com/@harikrishnaraj",
            "Profile Information": "https://www.producthunt.com/@harikrishnaraj Harikrishnaraj Project Manager #5075850 1 follower 0 following 3 points Follow MAKER HISTORY Multichain Playbook Unlock the potential of NFT Project with Multichain Playbook Jan 2023 🎉 Joined Product Hunt January 25th, 2023 Report",
            "Id Reference": "id=376717"
        }
    ]
    },
    {
        "Id": 376640,
        "Name": "Oura for Apple Watch",
        "Tagline": "Be mindful of your health data while you’re on the go",
        "Url": "https://www.producthunt.com/posts/oura-for-apple-watch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 34,
        "Profile_Url": "https://www.producthunt.com/@thisisthequick, https://www.producthunt.com/@plahtela",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@thisisthequick",
            "Profile Information": "https://www.producthunt.com/@thisisthequick Jason Russell Director of Product at Oura Ring #226335 150 followers 177 following 31 points Follow LINKS Twitter BADGES Veteran MAKER HISTORY Oura for Apple Watch Be mindful of your health data while you’re on the go Jan 2023 Oura The world's first wellness ring and app Oura Gen3 Horizon Ring Sep 2022 Oura Ring Gen3 Oct 2021 Pandora Find the music you love, and let the music you love find you. Oct 2016 🎉 Joined Product Hunt May 15th, 2015 Report",
            "Id Reference": "id=376640"
        },
        {
            "All_Urls": "https://www.producthunt.com/@plahtela",
            "Profile Information": "https://www.producthunt.com/@plahtela Petteri Lahtela CEO, Co-Founder at ŌURA #295979 296 followers 198 following 65 points Follow LINKS Twitter Website BADGES Veteran MAKER HISTORY Oura for Apple Watch Be mindful of your health data while you’re on the go Jan 2023 Oura The world's first wellness ring and app Oura Gen3 Horizon Ring Sep 2022 Oura Ring Gen3 Oct 2021 ŌURA Ring v2.0 Dec 2017 ŌURA Ring Jan 2016 🎉 Joined Product Hunt August 23rd, 2015 Report",
            "Id Reference": "id=376640"
        }
    ]
    },
    {
        "Id": 376756,
        "Name": "ciphergoat",
        "Tagline": "Encrypt and backup your recovery seed phrases",
        "Url": "https://www.producthunt.com/posts/ciphergoat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Profile_Url": "https://www.producthunt.com/@aaronpardes, https://www.producthunt.com/@danilo_bandovic, https://www.producthunt.com/@ronedg",
        "Information":  
    [
        {
            "All_Urls": "https://www.producthunt.com/@aaronpardes",
            "Profile Information": "https://www.producthunt.com/@aaronpardes Aaron Pardes Building things with code #82197 39 followers 142 following 14 points 🎉 6 day streak Follow ABOUT Professional web dev, crypto enthusiast, enjoyer of cool cars. LINKS Twitter BADGES Veteran MAKER HISTORY ciphergoat Encrypt and backup your recovery seed phrases Jan 2023 🎉 Joined Product Hunt October 9th, 2014 Report",
            "Id Reference": "id=376756"
        },
        {
            "All_Urls": "https://www.producthunt.com/@danilo_bandovic",
            "Profile Information": "https://www.producthunt.com/@danilo_bandovic Danilo Bandovic Lawyer with a business mindset. #5014999 0 followers 0 following 2 points ☀️ 2 day streak Follow INTERESTS Tech MAKER HISTORY ciphergoat Encrypt and backup your recovery seed phrases Jan 2023 🎉 Joined Product Hunt January 16th, 2023 Report",
            "Id Reference": "id=376756"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ronedg",
            "Profile Information": "https://www.producthunt.com/@ronedg Ron Edgar CEO & Co-founder | Genius Goat Labs Inc. #4916950 7 followers 0 following 5 points Follow ABOUT Brewing liberty, zen and technology. INTERESTS Developer Tools Tech MAKER HISTORY ciphergoat Encrypt and backup your recovery seed phrases Jan 2023 🎉 Joined Product Hunt December 14th, 2022 Report",
            "Id Reference": "id=376756"
        }
    ]
    },
    {
        "Id": 376757,
        "Name": "SULO-Y",
        "Tagline": "Trash bins just got smarter",
        "Url": "https://www.producthunt.com/posts/sulo-y?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 21,
        "Profile_Url": "No",
        "Information": [{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376750,
        "Name": "SpicyHR",
        "Tagline": "Forget Lever. SpicyHR is lightweight, intuitive, and FAST.",
        "Url": "https://www.producthunt.com/posts/spicyhr?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Profile_Url": "https://www.producthunt.com/@alimir, https://www.producthunt.com/@meisamm",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@alimir",
            "Profile Information": "https://www.producthunt.com/@alimir Ali Mir Co-founder at Spicy.hr #1193949 9 followers 0 following 9 points ☀️ 2 day streak Follow ABOUT Founder at Spicy.hr  Previously software engineer and eng leader at Doordash, Meta, Rippling, and Moralis. LINKS SpicyHR LinkedIn BADGES Veteran MAKER HISTORY BestSales.jobs Remote Tech Sales Jobs - SDR, ISR, BDR, and AE roles Feb 2023 SpicyHR SpicyHR is a FAST hiring software - made for startups who value time Jan 2023 Vasona Hire Lightweight recruiting platform with video cover letters Jan 2023 Hiring Cafe See who’s still hiring right now Dec 2022 Hekob Udemy but in real life Feb 2018 🎉 Joined Product Hunt February 21st, 2018 Report",
            "Id Reference": "id=376750"
        },
        {
            "All_Urls": "https://www.producthunt.com/@meisamm",
            "Profile Information": "https://www.producthunt.com/@meisamm Meisam Movassat Co-founder at Vasona; simplify hiring. #4975789 0 followers 0 following 4 points ☀️ 2 day streak Follow INTERESTS Design Tools Productivity Tech MAKER HISTORY SpicyHR SpicyHR is a FAST hiring software - made for startups who value time Jan 2023 Vasona Hire Lightweight recruiting platform with video cover letters Jan 2023 🎉 Joined Product Hunt January 5th, 2023 Report",
            "Id Reference": "id=376750"
        }
    ]
    },
    {
        "Id": 376841,
        "Name": "Shell GPT",
        "Tagline": "CLI tool for developers, helps you accomplish tasks faster",
        "Url": "https://www.producthunt.com/posts/shell-gpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Profile_Url": "No",
        "Information": [{"All_Urls":""},{ "Profile Information":""}, {"Id Reference":""}
    ]
    },
    {
        "Id": 376758,
        "Name": "Lightness",
        "Tagline": "App for meeting new people, exploring cultures and messaging",
        "Url": "https://www.producthunt.com/posts/lightness?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Profile_Url": "https://www.producthunt.com/@stefano_ippolito_gitto",
        "Information": [
        {
            "All_Urls": "https://www.producthunt.com/@stefano_ippolito_gitto",
            "Profile Information": "https://www.producthunt.com/@stefano_ippolito_gitto Stefano Ippolito Gitto Founder of Lightness #5081944 0 followers 0 following 2 points ☀️ 2 day streak Follow MAKER HISTORY Lightness App for meeting new people, exploring cultures and messaging Jan 2023 Destiny Lights A new social to express all your thoughts, ideas and secrets Jun 2022 🎉 Joined Product Hunt May 18th, 2022 Report",
            "Id Reference": "id=376758"
        }
    ]
    },
    {
        "Id": 376855,
        "Name": "Moodlody",
        "Tagline": "make you feel relaxed",
        "Url": "https://www.producthunt.com/posts/moodlody?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Profile_Url": "https://www.producthunt.com/@deathtinyz",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@deathtinyz",
            "Profile Information": "https://www.producthunt.com/@deathtinyz Dream.Chayutpong Front-End Developer. #5012375 10 followers 0 following 1 point Follow ABOUT My name is Chayutpong Jamneanpongphan. I am a Front-End Developer. I create professional websites. I love art and always try to show unique views to the audience through my design. I will go beyond the limits. LINKS Facebook Instagram Linkedin MAKER HISTORY Moodlody make you feel relaxed. Jan 2023 🎉 Joined Product Hunt January 14th, 2023 Report",
            "Id Reference": "id=376855"
        }
    ]
    },
    {
        "Id": 376875,
        "Name": "Todidlist",
        "Tagline": "Simple place to track what you've done",
        "Url": "https://www.producthunt.com/posts/todidlist?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 18,
        "Profile_Url": "https://www.producthunt.com/@patrick_tran1",
        "Information":  [
        {
            "All_Urls": "https://www.producthunt.com/@patrick_tran1",
            "Profile Information": "https://www.producthunt.com/@patrick_tran1 Patrick Tran #1707886 1 follower 0 following 7 points ✨ 3 day streak Follow MAKER HISTORY Translate Park English sentence simplifier and translator Mar 2023 Todidlist Simple place to track what you've done Jan 2023 🎉 Joined Product Hunt March 4th, 2019 Report",
            "Id Reference": "id=376875"
        }
    ]
    },
    {
        "Id": 376434,
        "Name": "Ask by Slite",
        "Tagline": "Use AI to ask your workspace questions",
        "Url": "https://www.producthunt.com/posts/ask-by-slite?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 906,
        "Profile_Url": "https://www.producthunt.com/@christophepas, https://www.producthunt.com/@jonmccull, https://www.producthunt.com/@pierre_renaudin, https://www.producthunt.com/@fadeelah_al_horaibi, https://www.producthunt.com/@ani_cordani, https://www.producthunt.com/@clara_rua, https://www.producthunt.com/@brieuc1, https://www.producthunt.com/@aduban, https://www.producthunt.com/@mydigitalself, https://www.producthunt.com/@arnaudrinquin, https://www.producthunt.com/@laure_albouy, https://www.producthunt.com/@calyhre, https://www.producthunt.com/@rob_mcmackin, https://www.producthunt.com/@ataravant, https://www.producthunt.com/@guillaume_morin, https://www.producthunt.com/@shahor, https://www.producthunt.com/@teubeu2",
        "Information":
   
   
   
    [
        {
            "All_Urls": "https://www.producthunt.com/@christophepas",
            "Profile Information": "https://www.producthunt.com/@christophepas Christophe Pasquier Founder @ Slite #40739 1,445 followers 541 following 1,179 points ☀️ 2 day streak Follow ABOUT I have been building a product company, Slite, in remote since 2016,  a workspace for modern teams to adapt to the new work era.  I constantly think, write about the next frontiers of work, share and discuss these thoughts here, on Linkedin,  and on slite.com/blog.  I'm lucky enough to have built a brilliant team of 40 incredible human beings, spread in 12 countries 🇲🇦🇱🇹🇦🇷🇬🇧🇳🇱🇫🇷🇳🇴🇺🇸🇪🇸🇩🇪🇨🇦🇵🇹, to have attended YC in 2018, raised more than 15M$ with incredible investors such as Spark capital and Index ventures, and to serve dozens of thousands teams every month! LINKS Website Twitter INTERESTS Design Tools Productivity Writing User Experience Artificial Intelligence BADGES 7 Top Product Veteran View all badges MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Slite + Excalidraw Feb 2021 Slite 2.0 Oct 2020 Lead by Writing Sep 2019 Slite for Mobile Dec 2018 Slite Jan 2018 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt August 8th, 2014 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@jonmccull",
            "Profile Information": "https://www.producthunt.com/@jonmccull Jon McCullough Product Marketing at Slite #476481 170 followers 315 following 274 points Follow ABOUT Canadian in Norway • Product Marketing at @SliteHQ • Talks about marketing, remote work and my dog. 🐼 • On Mastodon 👉 stegodon.org/@jon LINKS Website Twitter INTERESTS Mac Slack Productivity News Music Home Social Media Growth Hacking Global Nomad Coffee Developer Tools Artificial Intelligence Product Hunt Tech BADGES 2 Top Product Veteran View all badges MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Vivaldi Hyper-customizable browser that puts you in control. Vivaldi Translate Jun 2021 Vivaldi Browser 3.0 Apr 2020 Vivaldi Browser for Android – Beta Sep 2019 Vivaldi Browser 2.0 Sep 2018 Vertical Reader Mode in Vivaldi Jan 2018 Vivaldi History Mar 2017 Vivaldi 1.5 Nov 2016 🎉 Joined Product Hunt March 2nd, 2016 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@pierre_renaudin",
            "Profile Information": "https://www.producthunt.com/@pierre_renaudin Pierre Renaudin Sliter #1014532 355 followers 79 following 668 points ✨ 3 day streak Follow LINKS Twitter BADGES 7 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Slite 2.0 Oct 2020 Slite for Mobile Dec 2018 Slite Jan 2018 Templates by Slite Jan 2018 Slite Oct 2017 Drubbbler Team Schedule and coordinate your Dribbble shots, in team. May 2016 Drubbbler Buffer for Dribbble. Schedule your posts. Dec 2015 Azendoo Turn conversations into actions Azendoo Calendar Nov 2015 Azendoo Dashboards Oct 2015 Azendoo Direct Messages Sep 2015 Azendoo Task Pilot May 2015 🎉 Joined Product Hunt September 19th, 2017 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@fadeelah_al_horaibi",
            "Profile Information": "https://www.producthunt.com/@fadeelah_al_horaibi Fadeelah Al-horaibi Head of Product @Slite #2386400 12 followers 1 following 136 points Follow LINKS Website BADGES 2 Top Product MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 🎉 Joined Product Hunt February 14th, 2020 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ani_cordani",
            "Profile Information": "https://www.producthunt.com/@ani_cordani Ani Cordani #4352008 11 followers 0 following 128 points Follow BADGES 2 Top Product MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 🎉 Joined Product Hunt June 9th, 2022 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@clara_rua",
            "Profile Information": "https://www.producthunt.com/@clara_rua Clara Rua Product designer #1081895 298 followers 422 following 779 points Follow LINKS Website Twitter INTERESTS Android iOS Slack Design Tools Productivity Task Management User Experience Fintech Prototyping A/B Testing Education Growth Hacking Crypto Internet of Things SaaS Photography Tech BADGES 9 Top Product Veteran View all badges MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Slite 2.0 Oct 2020 Draft by Slite Jul 2020 Startup Bibles May 2019 Employee onboarding checklist Feb 2019 Slite for Mobile Dec 2018 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt November 15th, 2017 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@brieuc1",
            "Profile Information": "https://www.producthunt.com/@brieuc1 Brieuc Sebillotte #796877 193 followers 267 following 497 points Follow LINKS Twitter Linkedin INTERESTS Android iOS Productivity User Experience Growth Hacking Artificial Intelligence BADGES 4 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Slite Jan 2018 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt January 31st, 2017 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@aduban",
            "Profile Information": "https://www.producthunt.com/@aduban Antoine Duban #1126563 6 followers 0 following 300 points Follow INTERESTS Productivity Developer Tools Artificial Intelligence Tech Books BADGES 2 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Slite + Excalidraw Feb 2021 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt January 5th, 2018 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@mydigitalself",
            "Profile Information": "https://www.producthunt.com/@mydigitalself michael bartlett #18940 355 followers 278 following 294 points ☀️ 2 day streak Follow LINKS Twitter BADGES 2 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Slite 2.0 Oct 2020 Slite Oct 2017 Gitter Where communities thrive Oct 2015 🎉 Joined Product Hunt June 17th, 2014 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@arnaudrinquin",
            "Profile Information": "https://www.producthunt.com/@arnaudrinquin Arnaud Rinquin #109130 273 followers 361 following 517 points Follow LINKS Github Twitter BADGES 5 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Draft by Slite Jul 2020 Slite for Mobile Dec 2018 Slite Jan 2018 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt November 19th, 2014 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@laure_albouy",
            "Profile Information": "https://www.producthunt.com/@laure_albouy Laure Albouy marketing @ bonsai #704767 393 followers 346 following 782 points Follow LINKS Website Twitter INTERESTS Productivity Writing Notes Marketing SaaS Product Hunt BADGES 6 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Draft by Slite Jul 2020 Lead by Writing Sep 2019 Startup Bibles May 2019 Employee onboarding checklist Feb 2019 Slite Jan 2018 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt November 8th, 2016 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@calyhre",
            "Profile Information": "https://www.producthunt.com/@calyhre Charley D. #109053 121 followers 18 following 673 points Follow LINKS Website BADGES 6 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Slite Discussions Jun 2022 Draft by Slite Jul 2020 Slite for Mobile Dec 2018 Slite Oct 2017 Azendoo Turn conversations into actions Azendoo Task Boards Sep 2017 Azendoo Time-Tracking May 2017 Azendoo Direct Messages Sep 2015 Drubbbler Team Schedule and coordinate your Dribbble shots, in team. May 2016 Papier Open a new tab and trap your best thoughts. Mar 2016 Drubbbler Buffer for Dribbble. Schedule your posts. Drubbbler Pro Dec 2015 Drubbbler Nov 2014 🎉 Joined Product Hunt November 19th, 2014 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@rob_mcmackin",
            "Profile Information": "https://www.producthunt.com/@rob_mcmackin Rob McMackin Product designer @ Slite #731864 214 followers 263 following 315 points Follow LINKS Twitter INTERESTS News Newsletters Prototyping Education Artificial Intelligence BADGES 2 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Lead by Writing Sep 2019 Slite Oct 2017 Under Glass An analysis of the world's best digital products May 2018 🎉 Joined Product Hunt December 6th, 2016 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ataravant",
            "Profile Information": "https://www.producthunt.com/@ataravant Adrien Taravant #140517 103 followers 186 following 459 points Follow LINKS Twitter Linkedin BADGES 4 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Startup Bibles May 2019 Employee onboarding checklist Feb 2019 Slite Oct 2017 🎉 Joined Product Hunt January 20th, 2015 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@guillaume_morin",
            "Profile Information": "https://www.producthunt.com/@guillaume_morin Guillaume Morin Lead Mobile engineer @slitehq 👨‍💻📱⚛️ #588483 42 followers 201 following 297 points ☀️ 2 day streak Follow LINKS Website Twitter INTERESTS Android iOS Design Tools Writing Social Network Photography Developer Tools Tech BADGES 2 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Slite for Mobile Dec 2018 Slite Oct 2017 Fwdapp Profile pages deserves better contents. Publish others' pics Jun 2017 🎉 Joined Product Hunt June 22nd, 2016 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@shahor",
            "Profile Information": "https://www.producthunt.com/@shahor Alexandre Gaudencio Spaceship launcher @ Slite #25271 107 followers 107 following 363 points Follow LINKS Website Twitter INTERESTS Web App Productivity Developer Tools Games BADGES 3 Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Ask by Slite Jan 2023 Templates by Slite Jan 2018 Slite Oct 2017 🎉 Joined Product Hunt July 4th, 2014 Report",
            "Id Reference": "id=376434"
        },
        {
            "All_Urls": "https://www.producthunt.com/@teubeu2",
            "Profile Information": "https://www.producthunt.com/@teubeu2 Clément Rucheton #1126564 23 followers 23 following 72 points Follow INTERESTS Productivity Developer Tools Artificial Intelligence Tech Books BADGES Top Product Veteran MAKER HISTORY Slite Bring clarity to your team Jan 2018 🎉 Joined Product Hunt January 5th, 2018 Report",
            "Id Reference": "id=376434"
        }
    ]
    },
    {
        "Id": 375110,
        "Name": "Charlie",
        "Tagline": "Helping everyone create marketing content",
        "Url": "https://www.producthunt.com/posts/charlie-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 974,
        "Profile_Url": "https://www.producthunt.com/@brennanwoodruff, https://www.producthunt.com/@kostas_hatalis, https://www.producthunt.com/@despina_christou",
        "Information":   
   
    [
        {
            "All_Urls": "https://www.producthunt.com/@brennanwoodruff",
            "Profile Information": "https://www.producthunt.com/@brennanwoodruff Brennan Woodruff Finance guy gone AI Product Developer #4598581 48 followers 3 following 306 points Follow ABOUT Hoosier gone rogue to California.  After working at KPMG, Uber's Product Finance Team, and Softbank's Vision Funds I decided that I want to focus on building products that help people make entrepreneurship more accessible and sustainable. That lead me to work with a few AI Mad Scientists to build GoCharlie.ai. We're focused on building a first of it's kind AI Content Creation Tool that is purpose built for marketing.  In my spare time, I listen to podcasts, read, write a newsletter and editorials, and volunteer with the Guardsmen in San Francisco.  INTERESTS Art Marketing Artificial Intelligence Growth Hacks BADGES Buddy System 2 Top Product MAKER HISTORY GoCharlie.ai Making Content Creation as fun as playing with a puppy Charlie Jan 2023 Charlie 2.0 Sep 2022 🎉 Joined Product Hunt September 5th, 2022 Report",
            "Id Reference": "id=375110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@kostas_hatalis",
            "Profile Information": "https://www.producthunt.com/@kostas_hatalis Kostas Hatalis CEO of GoCharlie.ai #4652960 5 followers 3 following 85 points ☀️ 2 day streak Follow ABOUT I love AI and structured my life around it! From getting a Ph.D. in it to building an AI startup, I genuinely believe it is the future! LINKS GoCharlie LinkedIn INTERESTS Productivity Developer Tools Artificial Intelligence BADGES Top Product MAKER HISTORY GoCharlie.ai Making Content Creation as fun as playing with a puppy Jan 2023 🎉 Joined Product Hunt September 22nd, 2022 Report",
            "Id Reference": "id=375110"
        },
        {
            "All_Urls": "https://www.producthunt.com/@despina_christou",
            "Profile Information": "https://www.producthunt.com/@despina_christou Despina Christou . #4650944 5 followers 0 following 73 points ☀️ 2 day streak Follow BADGES Top Product MAKER HISTORY GoCharlie.ai Making Content Creation as fun as playing with a puppy Jan 2023 🎉 Joined Product Hunt September 22nd, 2022 Report",
            "Id Reference": "id=375110"
        }
    ]
    },
    {
        "Id": 374952,
        "Name": "NeevaAI",
        "Tagline": "Search powered by AI to get answers, not ads",
        "Url": "https://www.producthunt.com/posts/neevaai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 1117,
        "Profile_Url": "https://www.producthunt.com/@hwi, https://www.producthunt.com/@yusuf_ozuysal, https://www.producthunt.com/@sethli, https://www.producthunt.com/@jiwoong_lee, https://www.producthunt.com/@coopslarhette, https://www.producthunt.com/@rajhans_samdani, https://www.producthunt.com/@edmundloo, https://www.producthunt.com/@darinwf, https://www.producthunt.com/@sridhar_ramaswamy1, https://www.producthunt.com/@ahraycho, https://www.producthunt.com/@tyggy",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@hwi",
            "Profile Information": "https://www.producthunt.com/@hwi Hwi Lee Head of Design @Neeva #3979291 13 followers 19 following 99 points Follow ABOUT Activate design within teams, colleagues, and community. Make search 10x better.  LINKS Twitter LinkedIn INTERESTS Artificial Intelligence Design BADGES Buddy System Top Product MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jan 2023 🎉 Joined Product Hunt January 12th, 2022 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@yusuf_ozuysal",
            "Profile Information": "https://www.producthunt.com/@yusuf_ozuysal Yusuf Ozuysal Mobile @Neeva #3988463 10 followers 0 following 94 points ⚡️ 4 day streak Follow BADGES Top Product MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jan 2023 Neeva Search for Android Get honest results. Free from corporate bias & trackers. Aug 2022 🎉 Joined Product Hunt January 13th, 2022 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sethli",
            "Profile Information": "https://www.producthunt.com/@sethli Seth Li Growth @ Neeva #3553263 14 followers 0 following 229 points ☀️ 2 day streak Follow LINKS Website INTERESTS iOS BADGES 2 Top Product MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. NeevaAI Jan 2023 Neeva Jul 2021 Neeva Search for Android Get honest results. Free from corporate bias & trackers. Aug 2022 🎉 Joined Product Hunt July 15th, 2021 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@jiwoong_lee",
            "Profile Information": "https://www.producthunt.com/@jiwoong_lee Jiwoong Lee UX designer, Neeva #588834 79 followers 2 following 96 points Follow ABOUT Design User Interface. Draw things. Write code. Solve problems. Take photos. Love people. Dad INTERESTS Virtual Reality Design Tools Productivity Home User Experience Prototyping Photography Coffee Developer Tools Artificial Intelligence BADGES Top Product Veteran MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jan 2023 🎉 Joined Product Hunt June 22nd, 2016 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@coopslarhette",
            "Profile Information": "https://www.producthunt.com/@coopslarhette Cooper LaRhette SWE @ Neeva #3990531 2 followers 0 following 88 points Follow LINKS Website BADGES Top Product MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jan 2023 🎉 Joined Product Hunt January 14th, 2022 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@rajhans_samdani",
            "Profile Information": "https://www.producthunt.com/@rajhans_samdani Rajhans Samdani Head of Machine Learning, Neeva #880868 187 followers 48 following 201 points ✨ 3 day streak Follow LINKS Twitter Website INTERESTS Slack Productivity Analytics Growth Hacking Artificial Intelligence Bots Tech BADGES 2 Top Product Veteran MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jan 2023 Atspoke Modern Internal Ticketing Mar 2018 🎉 Joined Product Hunt May 5th, 2017 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@edmundloo",
            "Profile Information": "https://www.producthunt.com/@edmundloo Edmund Loo edmundloo.com #971504 28 followers 15 following 121 points Follow ABOUT Engineering Leader; Previously at Neeva, CZI, Plaid, Tinder, and Facebook LINKS Website Twitter INTERESTS Web App Slack Productivity Home Growth Hacking Internet of Things Photography Wearables Developer Tools Artificial Intelligence Tech Games BADGES Top Product Veteran MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jul 2021 🎉 Joined Product Hunt August 10th, 2017 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@darinwf",
            "Profile Information": "https://www.producthunt.com/@darinwf Darin Fisher browser builder @neeva #3557018 29 followers 0 following 163 points Follow LINKS Linkedin INTERESTS User Experience Developer Tools Tech BADGES Top Product MAKER HISTORY Neeva Search for Android Get honest results. Free from corporate bias & trackers. Aug 2022 Neeva Search powered by AI. Get answers. Not ads. Jul 2021 🎉 Joined Product Hunt July 15th, 2021 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@sridhar_ramaswamy1",
            "Profile Information": "https://www.producthunt.com/@sridhar_ramaswamy1 Sridhar Ramaswamy @neeva Co-Founder Ex-@Google SVP Ads #3522651 111 followers 2 following 488 points Follow LINKS Linkedin INTERESTS Productivity Artificial Intelligence Tech BADGES 2 Top Product MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. NeevaAI Jan 2023 Neeva Jul 2021 Neeva Search for Android Get honest results. Free from corporate bias & trackers. Aug 2022 🎉 Joined Product Hunt July 2nd, 2021 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ahraycho",
            "Profile Information": "https://www.producthunt.com/@ahraycho Rachel Cheng Product Designer #819888 145 followers 378 following 105 points ☀️ 2 day streak Follow LINKS Twitter Website INTERESTS iOS Mac Design Tools Productivity Task Management Spotify Writing User Experience Analytics Prototyping Time Tracking Internet of Things Privacy Wearables Tech BADGES Top Product Veteran MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jul 2021 🎉 Joined Product Hunt February 26th, 2017 Report",
            "Id Reference": "id=374952"
        },
        {
            "All_Urls": "https://www.producthunt.com/@tyggy",
            "Profile Information": "https://www.producthunt.com/@tyggy Anton Borzov Product Design. Formerly @WhatsApp. #167543 376 followers 1,266 following 97 points Follow LINKS Twitter Website BADGES Top Product Veteran MAKER HISTORY Neeva Search powered by AI. Get answers. Not ads. Jul 2021 Save 21 days per year while typing fast speed typing, save time, productivity, Groups for competition Sep 2019 Average typing speed infographic Aug 2019 Instruction about how to touch type Aug 2019 Ratatype Free Online Typing Tutor Apr 2015 🎉 Joined Product Hunt March 2nd, 2015 Report",
            "Id Reference": "id=374952"
        }
    ]
    },
    {
        "Id": 376466,
        "Name": "WritingMate.ai",
        "Tagline": "Free ChatGPT alternative that works as a Chrome extension",
        "Url": "https://www.producthunt.com/posts/writingmate-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 739,
        "Profile_Url": "https://www.producthunt.com/@ednevsky, https://www.producthunt.com/@artem_vysotsky",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@ednevsky",
            "Profile Information": "https://www.producthunt.com/@ednevsky Alexander Nevedovsky #1105511 356 followers 1,675 following 458 points ☀️ 2 day streak Follow ABOUT 2x founder. Ex WANNA (exit to Farfetch) and Palta (startup studio behind Flo) LINKS Twitter Linkedin INTERESTS iOS Health & Fitness Productivity Messaging Social Network Meditation Artificial Intelligence Social Impact BADGES 4 Top Product Veteran MAKER HISTORY Writingmate.ai Free ChatGPT alternative that works as a Chrome extension Jan 2023 Alms A well-being social app focused on IRL actions Nov 2021 Wanna Kicks Try on and shop footwear in AR! Jan 2019 WANNABY Our mission is to break online shopping barriers. Jun 2018 🎉 Joined Product Hunt December 9th, 2017 Report",
            "Id Reference": "id=376466"
        },
        {
            "All_Urls": "https://www.producthunt.com/@artem_vysotsky",
            "Profile Information": "https://www.producthunt.com/@artem_vysotsky Artem Vysotsky #1616664 24 followers 8 following 148 points Follow BADGES 2 Top Product MAKER HISTORY Writingmate.ai Free ChatGPT alternative that works as a Chrome extension Jan 2023 Gainy Thematic investing platform Feb 2022 🎉 Joined Product Hunt January 13th, 2019 Report",
            "Id Reference": "id=376466"
        }
    ]
    },
    {
        "Id": 375784,
        "Name": "Conektto API-First Design Studio",
        "Tagline": "API design studio for product managers",
        "Url": "https://www.producthunt.com/posts/conektto-api-first-design-studio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 541,
        "Profile_Url": "https://www.producthunt.com/@rams_211, https://www.producthunt.com/@amol_dewhare, https://www.producthunt.com/@madhu_v_swamy1",
        "Information":   

    [
        {
            "All_Urls": "https://www.producthunt.com/@rams_211",
            "Profile Information": "https://www.producthunt.com/@rams_211 Ram Sathia Automation obsessed technologist #4344282 78 followers 222 following 381 points 🔥 7 day streak Follow ABOUT Have been automating tech for 20+ years. Automation is not just my passion but an obsession. We only have scratched the surface. So much more to automate and endless possibilities.  6+ patents and innovation, much more to go.   My ideal / nirvana of automation: 1. Connect brain and google search (without computer / phone) so knowledge is not just in your fingertips but right in your train of thoughts - neuro mirroring? 2. Power conversations through API 3. Personal upvotes - true upvotes to motivate kind acts, favors / deeds, leadership, professional help, a true social help platform through automation across all social channels 4. Space travel simplified and cheap 5. Time travel and teleportation (joke?) INTERESTS Productivity API Developer Tools Artificial Intelligence Tech Design BADGES Buddy System 2 Top Product View all badges MAKER HISTORY Conektto Powering the innovators of tomorrow Conektto API-First Design Studio Jan 2023 EZAPI Lifecycle Fabric Jun 2022 Conektto API Test Harness Autonomous API Testing Platform Oct 2022 🎉 Joined Product Hunt June 7th, 2022 Report",
            "Id Reference": "id=375784"
        },
        {
            "All_Urls": "https://www.producthunt.com/@amol_dewhare",
            "Profile Information": "https://www.producthunt.com/@amol_dewhare Amol Dewhare Founder & CEO of Conektto #4641853 18 followers 43 following 265 points Follow BADGES Buddy System 2 Top Product MAKER HISTORY Conektto Powering the innovators of tomorrow Jan 2023 Conektto API Test Harness Autonomous API Testing Platform Oct 2022 🎉 Joined Product Hunt September 20th, 2022 Report",
            "Id Reference": "id=375784"
        },
        {
            "All_Urls": "https://www.producthunt.com/@madhu_v_swamy1",
            "Profile Information": "https://www.producthunt.com/@madhu_v_swamy1 Madhu V Swamy Technopreneur building digital products #4161146 43 followers 83 following 54 points Follow ABOUT Helping startups and enterprises build digital innovations. More than a decade of experience in building and leading teams to build software solutions for the world. LINKS Cumulations Technologies Twitter INTERESTS Android API Software Engineering Coffee Developer Tools Tech No-Code Change Management SDK BADGES Top Product Veteran MAKER HISTORY Conektto Powering the innovators of tomorrow Jan 2023 🎉 Joined Product Hunt September 22nd, 2014 Report",
            "Id Reference": "id=375784"
        }
    ]
    },
    {
        "Id": 375864,
        "Name": "Figma to WordPress Beta",
        "Tagline": "Convert Figma to WordPress websites & themes automatically",
        "Url": "https://www.producthunt.com/posts/figma-to-wordpress-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 462,
        "Profile_Url": "https://www.producthunt.com/@garciafrey, https://www.producthunt.com/@cackbone, https://www.producthunt.com/@maublum, https://www.producthunt.com/@alimot15881733, https://www.producthunt.com/@ilyes_el_ayeb, https://www.producthunt.com/@saninemoreira",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@garciafrey",
            "Profile Information": "https://www.producthunt.com/@garciafrey Alfonso García Frey Building nextgen design technology #877476 131 followers 1,468 following 241 points Follow LINKS Twitter Website INTERESTS Design Tools Open Source Prototyping Growth Hacking Developer Tools Artificial Intelligence BADGES Veteran View all badges MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 Yotako Dec 2018 🎉 Joined Product Hunt May 2nd, 2017 Report",
            "Id Reference": "id=375864"
        },
        {
            "All_Urls": "https://www.producthunt.com/@cackbone",
            "Profile Information": "https://www.producthunt.com/@cackbone Cédric Legendre #1555388 14 followers 35 following 46 points Follow LINKS Github Twitter MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 🎉 Joined Product Hunt December 4th, 2018 Report",
            "Id Reference": "id=375864"
        },
        {
            "All_Urls": "https://www.producthunt.com/@maublum",
            "Profile Information": "https://www.producthunt.com/@maublum Maurício Software Dev, gamer and guitar player #4556405 9 followers 51 following 53 points Follow LINKS Website Twitter INTERESTS Developer Tools Tech MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 🎉 Joined Product Hunt August 25th, 2022 Report",
            "Id Reference": "id=375864"
        },
        {
            "All_Urls": "https://www.producthunt.com/@alimot15881733",
            "Profile Information": "https://www.producthunt.com/@alimot15881733 Ali mot Software engineer #4553224 6 followers 1 following 46 points Follow LINKS Linkedin INTERESTS Design Tools Artificial Intelligence Tech MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 🎉 Joined Product Hunt August 25th, 2022 Report",
            "Id Reference": "id=375864"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ilyes_el_ayeb",
            "Profile Information": "https://www.producthunt.com/@ilyes_el_ayeb Ilyes El ayeb software engineer #4492146 7 followers 6 following 60 points Follow MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 🎉 Joined Product Hunt August 5th, 2022 Report",
            "Id Reference": "id=375864"
        },
        {
            "All_Urls": "https://www.producthunt.com/@saninemoreira",
            "Profile Information": "https://www.producthunt.com/@saninemoreira Sanine Moreira #1197996 4 followers 0 following 46 points Follow LINKS Website BADGES Veteran MAKER HISTORY Yotako Bring Figma/AdobeXD designs to WordPress automatically Figma to WordPress Beta Jan 2023 WordPress for Adobe XD Sep 2022 🎉 Joined Product Hunt February 25th, 2018 Report",
            "Id Reference": "id=375864"
        }
    ]
    },
    {
        "Id": 376506,
        "Name": "Alt Sprints",
        "Tagline": "Idea to MVP in 2 weeks",
        "Url": "https://www.producthunt.com/posts/alt-sprints?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 295,
        "Profile_Url": "https://www.producthunt.com/@ali_haider32, https://www.producthunt.com/@ahsan_asghar29, https://www.producthunt.com/@ahsan_sohail2, https://www.producthunt.com/@yetunde_lopez, https://www.producthunt.com/@abcorn",
        "Information": 
    [
        {
            "All_Urls": "https://www.producthunt.com/@ali_haider32",
            "Profile Information": "https://www.producthunt.com/@ali_haider32 Ali Haider Building a venture studio #4885174 26 followers 13 following 87 points Follow LINKS Twitter Alt Sprints Alt Ventures Linkedin MAKER HISTORY Alt Sprints Idea to MVP in 2 Weeks NoLoCo Stack Feb 2023 Alt Sprints Jan 2023 Alt Pass - A future without OTPs Sign up users with WhatsApp Jan 2023 🎉 Joined Product Hunt December 7th, 2022 Report",
            "Id Reference": "id=376506"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ahsan_asghar29",
            "Profile Information": "https://www.producthunt.com/@ahsan_asghar29 Ahsan Asghar Product Manager #4688836 15 followers 9 following 44 points ✨ 3 day streak Follow INTERESTS Design Tools Productivity Developer Tools Artificial Intelligence Tech MAKER HISTORY Alt Sprints Idea to MVP in 2 Weeks NoLoCo Stack Feb 2023 Alt Sprints Jan 2023 🎉 Joined Product Hunt October 5th, 2022 Report",
            "Id Reference": "id=376506"
        },
        {
            "All_Urls": "https://www.producthunt.com/@ahsan_sohail2",
            "Profile Information": "https://www.producthunt.com/@ahsan_sohail2 Ahsan Sohail Venture Builder @ Alt Sprints #4688852 24 followers 53 following 65 points Follow ABOUT Building new ventures @ Alt Sprints LINKS Alt Sprints MAKER HISTORY Alt Sprints Idea to MVP in 2 Weeks NoLoCo Stack Feb 2023 Alt Sprints Jan 2023 🎉 Joined Product Hunt October 5th, 2022 Report",
            "Id Reference": "id=376506"
        },
        {
            "All_Urls": "https://www.producthunt.com/@yetunde_lopez",
            "Profile Information": "https://www.producthunt.com/@yetunde_lopez Yetunde Lopez Product designer #4160460 6 followers 6 following 27 points Follow MAKER HISTORY Alt Sprints Idea to MVP in 2 Weeks Jan 2023 🎉 Joined Product Hunt March 22nd, 2022 Report",
            "Id Reference": "id=376506"
        },
        {
            "All_Urls": "https://www.producthunt.com/@abcorn",
            "Profile Information": "https://www.producthunt.com/@abcorn Umair Abdullah Founder, digital nomad and storyteller. #4976712 5 followers 0 following 35 points Follow MAKER HISTORY Alt Sprints Idea to MVP in 2 Weeks Jan 2023 🎉 Joined Product Hunt January 5th, 2023 Report",
            "Id Reference": "id=376506"
        }
    ]
    }

]
   
   
  
 
  
  
 
  
   
   
  
   
   
 
  
   
  
 
   

 
   
   
  
  
  
 
  



























































































































# Write the combined data to a new file
with open('producthuntdata.json', 'w') as fout:
    json.dump(final_json, fout) 








   