# # take the json file for profile information and id reference !important
# import json 
# # Open and read the JSON file
# with open('content3.json') as f:
#     dict_list = json.load(f)
# list = []
# list2 = []
# #list Print the Python object
# print("data",dict_list)
# lists_of_dicts = []
# ids_added = {}

# for d in dict_list:
#     id_val = d['Id Reference']
#     print("id_val",id_val)
#     if id_val not in ids_added:
#         ids_added[id_val] = len(lists_of_dicts)
#         lists_of_dicts.append([d])
#     else:
#         lists_of_dicts[ids_added[id_val]].append(d)
        
# print("lists_of_dicts",lists_of_dicts)
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
import pandas as pd
final_json = [
    {
        "Id": 375989,
        "Name": "Live Video Calling SDK by Dyte",
        "Tagline": "Integrate into your product within minutes",
        "Url": "https://www.producthunt.com/posts/live-video-calling-sdk-by-dyte?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 1022,
        "Makers": [
            {
                "Name": "Abhishek Kankani",
                "Desgination": "CEO & Co-founder @Dyte",
                "Hashtag_value": "#3253855",
                "Followers_value": "45 followers",
                "Following_value": "18 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Palash Golecha",
                "Desgination": "Co-founder dyte.io",
                "Hashtag_value": "#3640660",
                "Followers_value": "23 followers",
                "Following_value": "7 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Kushagra Vaish",
                "Desgination": "Maker and reluctant leader",
                "Hashtag_value": "#3102152",
                "Followers_value": "27 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377157,
        "Name": "LINER AI",
        "Tagline": "A trustworthy ChatGPT search assistant",
        "Url": "https://www.producthunt.com/posts/liner-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 466,
        "Makers": [
            {
                "Name": "Brian Woo",
                "Desgination": "",
                "Hashtag_value": "#3630467",
                "Followers_value": "286 followers",
                "Following_value": "98 following",
                "Twitter Url": "https://twitter.com/wcm0505",
                "Linkedin Url": ""
            },
            {
                "Name": "Jinu Kim",
                "Desgination": "LINER CEO",
                "Hashtag_value": "#247375",
                "Followers_value": "89 followers",
                "Following_value": "10 following",
                "Twitter Url": "https://twitter.com/jinukim21",
                "Linkedin Url": ""
            },
            {
                "Name": "Jinu Kim",
                "Desgination": "",
                "Hashtag_value": "#1545376",
                "Followers_value": "8 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Sung Cho",
                "Desgination": "",
                "Hashtag_value": "#23565",
                "Followers_value": "844 followers",
                "Following_value": "33 following",
                "Twitter Url": "https://twitter.com/sungmoon",
                "Linkedin Url": ""
            },
            {
                "Name": "Min Park",
                "Desgination": "https://nexybit.com",
                "Hashtag_value": "#473726",
                "Followers_value": "119 followers",
                "Following_value": "14 following",
                "Twitter Url": "https://twitter.com/mynhpark",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376810,
        "Name": "Getgud.io",
        "Tagline": "Making online games toxic free",
        "Url": "https://www.producthunt.com/posts/getgud-io?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 370,
        "Makers": [
            {
                "Name": "Art Kulakov",
                "Desgination": "ML Lead, B2B gaming startup founder",
                "Hashtag_value": "#4950832",
                "Followers_value": "51 followers",
                "Following_value": "1 following",
                "Twitter Url": "https://twitter.com/artkulak",
                "Linkedin Url": "https://www.linkedin.com/mwlite/in/art-kulakov"
            },
            {
                "Name": "guy kroupp",
                "Desgination": "Tech entrepreneur",
                "Hashtag_value": "#366814",
                "Followers_value": "19 followers",
                "Following_value": "2 following",
                "Twitter Url": "https://twitter.com/guykroupp",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376335,
        "Name": "littlecook",
        "Tagline": "Turn unused ingredients into delicious new dishes",
        "Url": "https://www.producthunt.com/posts/littlecook?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 251,
        "Makers": [
            {
                "Name": "Nimesh",
                "Desgination": "Founder littlecook.io ✦ ex-amazon",
                "Hashtag_value": "#4228846",
                "Followers_value": "159 followers",
                "Following_value": "233 following",
                "Twitter Url": "https://twitter.com/sup_nim",
                "Linkedin Url": "https://www.linkedin.com/in/nimeshnr/"
            },
            {
                "Name": "Amir Andohkosh",
                "Desgination": "Founder",
                "Hashtag_value": "#5064271",
                "Followers_value": "23 followers",
                "Following_value": "16 following",
                "Twitter Url": "https://twitter.com/amir__bio",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376853,
        "Name": "Terrastruct",
        "Tagline": "The diagramming tool for developers",
        "Url": "https://www.producthunt.com/posts/terrastruct-3?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 261,
        "Makers": [
            {
                "Name": "Alexander Wang",
                "Desgination": "",
                "Hashtag_value": "#1981849",
                "Followers_value": "99 followers",
                "Following_value": "193 following",
                "Twitter Url": "https://twitter.com/alixanderwang",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377091,
        "Name": "PriceWell Bubble Plugin for Stripe",
        "Tagline": "No fuss, no-code Stripe subscriptions for Bubble apps",
        "Url": "https://www.producthunt.com/posts/pricewell-bubble-plugin-for-stripe?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 271,
        "Makers": [
            {
                "Name": "Matthew Reid",
                "Desgination": "Co-Founder PriceWell.io",
                "Hashtag_value": "#2985088",
                "Followers_value": "38 followers",
                "Following_value": "71 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Σπυρος Κοντοπριας",
                "Desgination": "A storyteller",
                "Hashtag_value": "#5090787",
                "Followers_value": "8 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377162,
        "Name": "ChatGPT Famous Resumes",
        "Tagline": "1000+ AI generated resumes of famous people",
        "Url": "https://www.producthunt.com/posts/chatgpt-famous-resumes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 232,
        "Makers": [
            {
                "Name": "Viktor Kirilov",
                "Desgination": "Software Engineer, Car Enthusiast",
                "Hashtag_value": "#1723797",
                "Followers_value": "9 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376934,
        "Name": "Delibr AI",
        "Tagline": "AI-assisted end-to-end product management platform",
        "Url": "https://www.producthunt.com/posts/delibr-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 272,
        "Makers": [
            {
                "Name": "Nils Janse",
                "Desgination": "Founder of Delibr",
                "Hashtag_value": "#1913411",
                "Followers_value": "34 followers",
                "Following_value": "22 following",
                "Twitter Url": "https://twitter.com/nilsjanse",
                "Linkedin Url": ""
            },
            {
                "Name": "André Dantorp",
                "Desgination": "Startup and tech lover",
                "Hashtag_value": "#2157216",
                "Followers_value": "3 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Fredrika Andersson",
                "Desgination": "Product designer @Delibr",
                "Hashtag_value": "#4044997",
                "Followers_value": "14 followers",
                "Following_value": "9 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Erik Wenneborg",
                "Desgination": "Co founder at Delibr",
                "Hashtag_value": "#1919776",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Farid Bonawiede",
                "Desgination": "Co founder at Delibr",
                "Hashtag_value": "#806283",
                "Followers_value": "35 followers",
                "Following_value": "23 following",
                "Twitter Url": "https://twitter.com/fbonawiede",
                "Linkedin Url": ""
            },
            {
                "Name": "Nicole Landgraff",
                "Desgination": "Launching Delibr AI for Product Managers",
                "Hashtag_value": "#4045032",
                "Followers_value": "29 followers",
                "Following_value": "101 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377110,
        "Name": "Kayyo",
        "Tagline": "AI-powered personal MMA trainer",
        "Url": "https://www.producthunt.com/posts/kayyo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 206,
        "Makers": [
            {
                "Name": "Labib Yasir",
                "Desgination": "Co-Founder & CEO of Kayyo",
                "Hashtag_value": "#5069345",
                "Followers_value": "7 followers",
                "Following_value": "5 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Ayman Saleh",
                "Desgination": "ML Engineer, Building perception systems",
                "Hashtag_value": "#5091242",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "tedjouc1",
                "Desgination": "Product Designer at Kayyo",
                "Hashtag_value": "#5065014",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Mohamed Jaber",
                "Desgination": "iOS Software Engineer @ Kayyo",
                "Hashtag_value": "#5086282",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Messipsa Tamazouzt",
                "Desgination": "software engineer",
                "Hashtag_value": "#5086489",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Michael Paik",
                "Desgination": "Building Kayyo",
                "Hashtag_value": "#5072246",
                "Followers_value": "3 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377104,
        "Name": "Femme Stock",
        "Tagline": "Beautiful, feminine Ai stock images",
        "Url": "https://www.producthunt.com/posts/femme-stock?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 160,
        "Makers": [
            {
                "Name": "Zeng",
                "Desgination": "Founder of FemmeStock & WhoWhatWhyAi",
                "Hashtag_value": "#4432284",
                "Followers_value": "824 followers",
                "Following_value": "78 following",
                "Twitter Url": "https://twitter.com/zeng_wt",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376474,
        "Name": "Zoom Timer BlueSky Apps",
        "Tagline": "Timer shared directly in your Zoom meetings",
        "Url": "https://www.producthunt.com/posts/zoom-timer-bluesky-apps?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 138,
        "Makers": [
            {
                "Name": "Ben Ross",
                "Desgination": "",
                "Hashtag_value": "#791361",
                "Followers_value": "45 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Mahin Ali",
                "Desgination": "SaaS Marketing",
                "Hashtag_value": "#4382539",
                "Followers_value": "7 followers",
                "Following_value": "44 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377113,
        "Name": "WhatsApp Beta",
        "Tagline": "A more seamless experience for WhatsApp users on macOS",
        "Url": "https://www.producthunt.com/posts/whatsapp-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 120,
        "Makers": [
            {
                "Name": "Santhosh Kumar Elango",
                "Desgination": "Co-Founder and CEO at Leadfriday",
                "Hashtag_value": "#3406702",
                "Followers_value": "94 followers",
                "Following_value": "335 following",
                "Twitter Url": "https://twitter.com/iamsandysk",
                "Linkedin Url": "https://www.linkedin.com/in/santhosh-kumar-elango/"
            },
            {
                "Name": "Alexandru Rosianu",
                "Desgination": "Co-founder & CTO @ Proptee",
                "Hashtag_value": "#94699",
                "Followers_value": "242 followers",
                "Following_value": "0 following",
                "Twitter Url": "https://twitter.com/aluxian",
                "Linkedin Url": "https://www.linkedin.com/in/aluxian/"
            }
        ]
    },
    {
        "Id": 376809,
        "Name": "balancez",
        "Tagline": "Achieving balance, one day at a time",
        "Url": "https://www.producthunt.com/posts/balancez?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 117,
        "Makers": [
            {
                "Name": "Elif Duran",
                "Desgination": "Co-founder @BeforeSunset, learner&maker",
                "Hashtag_value": "#4366845",
                "Followers_value": "708 followers",
                "Following_value": "1,112 following",
                "Twitter Url": "https://twitter.com/productivelif",
                "Linkedin Url": "https://www.linkedin.com/in/elif-duran/"
            }
        ]
    },
    {
        "Id": 377095,
        "Name": "Tibio",
        "Tagline": "Track your mood, habits, make notes, and more",
        "Url": "https://www.producthunt.com/posts/tibio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 133,
        "Makers": [
            {
                "Name": "Patrik Svoboda",
                "Desgination": "Product designer, Tibio co-creator.",
                "Hashtag_value": "#370268",
                "Followers_value": "116 followers",
                "Following_value": "103 following",
                "Twitter Url": "https://twitter.com/thesvob",
                "Linkedin Url": "https://www.linkedin.com/in/patrik-svoboda-59526041/"
            },
            {
                "Name": "Duc Phi Viet",
                "Desgination": "Hi, I am a creator of Tibio app.",
                "Hashtag_value": "#5081562",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375586,
        "Name": "Monse",
        "Tagline": "Privacy-friendly personal finance application",
        "Url": "https://www.producthunt.com/posts/monse-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 123,
        "Makers": [
            {
                "Name": "Víctor Falcón",
                "Desgination": "",
                "Hashtag_value": "#1861319",
                "Followers_value": "17 followers",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377115,
        "Name": "Nike Training Club on Netflix",
        "Tagline": "Just stream it",
        "Url": "https://www.producthunt.com/posts/nike-training-club-on-netflix?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 89,
        "Makers": [
            {
                "Name": "Dave Schlafman",
                "Desgination": "",
                "Hashtag_value": "#385046",
                "Followers_value": "488 followers",
                "Following_value": "180 following",
                "Twitter Url": "https://twitter.com/schlafman",
                "Linkedin Url": ""
            },
            {
                "Name": "Navin Iyengar",
                "Desgination": "Product Designer, Netflix",
                "Hashtag_value": "#139257",
                "Followers_value": "664 followers",
                "Following_value": "672 following",
                "Twitter Url": "https://twitter.com/navin_",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375401,
        "Name": "bestcodingpractices.dev",
        "Tagline": "A place to learn, inspire and share best coding practices",
        "Url": "https://www.producthunt.com/posts/bestcodingpractices-dev?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 87,
        "Makers": [
            {
                "Name": "Cédric Teyton",
                "Desgination": "CEO & co-founder @Promyze",
                "Hashtag_value": "#3283109",
                "Followers_value": "5 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Heloïse Birot",
                "Desgination": "https://promyze.com/",
                "Hashtag_value": "#3694934",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Corentin Latappy",
                "Desgination": "Dev @Promyze",
                "Hashtag_value": "#3769713",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Arthur Magne",
                "Desgination": "Co-founder & CTO @ Promyze",
                "Hashtag_value": "#3537745",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Xavier Blanc",
                "Desgination": "I am interested in software development",
                "Hashtag_value": "#3756491",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Malo Couaran",
                "Desgination": "Budding software craftman",
                "Hashtag_value": "#5022568",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377208,
        "Name": "Moonwalkers",
        "Tagline": "Seriously fast walking shoes",
        "Url": "https://www.producthunt.com/posts/moonwalkers?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 68,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376579,
        "Name": "Squaredance for Shopify",
        "Tagline": "Partner marketplace for DTC brands, get customers,grow sales",
        "Url": "https://www.producthunt.com/posts/squaredance-for-shopify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 76,
        "Makers": [
            {
                "Name": "Shilpa Mandhan",
                "Desgination": "Head of Growth @ Squaredance",
                "Hashtag_value": "#4539037",
                "Followers_value": "9 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/shilpa-mandhan/"
            },
            {
                "Name": "Natalie Mastracci",
                "Desgination": "Product @ Squaredance",
                "Hashtag_value": "#4861991",
                "Followers_value": "17 followers",
                "Following_value": "19 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/natalie-mastracci/"
            },
            {
                "Name": "Michael Fulton",
                "Desgination": "Growth Marketing Director",
                "Hashtag_value": "#4973029",
                "Followers_value": "8 followers",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Camay Lee",
                "Desgination": "Product marketer",
                "Hashtag_value": "#4975124",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377154,
        "Name": "7-Day UX Job Hunting Challenge",
        "Tagline": "Go from 0 to 10 job applications, in 7 days",
        "Url": "https://www.producthunt.com/posts/7-day-ux-job-hunting-challenge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Makers": [
            {
                "Name": "Christopher Nguyen",
                "Desgination": "Making UX Playbook",
                "Hashtag_value": "#3390344",
                "Followers_value": "119 followers",
                "Following_value": "6 following",
                "Twitter Url": "https://twitter.com/uxchrisnguyen",
                "Linkedin Url": "https://www.linkedin.com/in/uxchrisnguyen/"
            },
            {
                "Name": "Bryant Castro",
                "Desgination": "Design leader growing teams & products",
                "Hashtag_value": "#4654449",
                "Followers_value": "3 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377195,
        "Name": "Whispr",
        "Tagline": "Alternative to ChatGPT",
        "Url": "https://www.producthunt.com/posts/whispr-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 60,
        "Makers": [
            {
                "Name": "Álvaro Pintado",
                "Desgination": "Co-Founder at Gox.",
                "Hashtag_value": "#5016060",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377087,
        "Name": "This Product Does Not Exist",
        "Tagline": "Reinventing the wheel with AI, one product at a time",
        "Url": "https://www.producthunt.com/posts/this-product-does-not-exist-1?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 56,
        "Makers": [
            {
                "Name": "Mighil",
                "Desgination": "globe-earther and schnauzer enthusiast",
                "Hashtag_value": "#3955223",
                "Followers_value": "142 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377100,
        "Name": "Fablegym",
        "Tagline": "Read a classic book in 30 days as an email newsletter",
        "Url": "https://www.producthunt.com/posts/fablegym?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 59,
        "Makers": [
            {
                "Name": "Solomon Kingsnorth",
                "Desgination": "Teacher",
                "Hashtag_value": "#1253561",
                "Followers_value": "146 followers",
                "Following_value": "17 following",
                "Twitter Url": "https://twitter.com/solomon_teach",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376954,
        "Name": "ClipNinja",
        "Tagline": "Minimal copy and paste tool for Mac",
        "Url": "https://www.producthunt.com/posts/clipninja-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 44,
        "Makers": [
            {
                "Name": "Libor Huspenina",
                "Desgination": "Apple platforms developer",
                "Hashtag_value": "#1694039",
                "Followers_value": "23 followers",
                "Following_value": "70 following",
                "Twitter Url": "https://twitter.com/liborhuspenina",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377071,
        "Name": "DeveloperHub.io",
        "Tagline": "The most advanced tool for creating product and API docs",
        "Url": "https://www.producthunt.com/posts/developerhub-io-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Makers": [
            {
                "Name": "Zaid Daba'een",
                "Desgination": "CEO & Founder - DeveloperHub",
                "Hashtag_value": "#1647775",
                "Followers_value": "32 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376994,
        "Name": "Qeraunos",
        "Tagline": "An ultrafast, lightweight caching solution for GraphQL",
        "Url": "https://www.producthunt.com/posts/qeraunos?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 40,
        "Makers": [
            {
                "Name": "Arthur Huynh",
                "Desgination": "Software Engineer at Qeraunos",
                "Hashtag_value": "#5055002",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Dennis Cheung",
                "Desgination": "software engineer",
                "Hashtag_value": "#5088711",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Amrit Ramos",
                "Desgination": "Software Engineer.",
                "Hashtag_value": "#5088716",
                "Followers_value": "0 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377245,
        "Name": "Deploy Button for custom GPT-3 APIs",
        "Tagline": "Instant GPT-3 backend hosting so you can focus on product",
        "Url": "https://www.producthunt.com/posts/deploy-button-for-custom-gpt-3-apis?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 44,
        "Makers": [
            {
                "Name": "Ted Benson",
                "Desgination": "I turn research into product.",
                "Hashtag_value": "#122399",
                "Followers_value": "614 followers",
                "Following_value": "614 following",
                "Twitter Url": "https://twitter.com/edwardbenson",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376612,
        "Name": "Free Valentine's Day 3d illustrations",
        "Tagline": "Lovely 3d illustrations for your design projects",
        "Url": "https://www.producthunt.com/posts/free-valentine-s-day-3d-illustrations?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 36,
        "Makers": [
            {
                "Name": "Egor Mishin",
                "Desgination": "",
                "Hashtag_value": "#1726448",
                "Followers_value": "23 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Veronika Bochkareva",
                "Desgination": "3D Artist",
                "Hashtag_value": "#1766409",
                "Followers_value": "4 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Anton Mishin",
                "Desgination": "Co-founder at Wannathis.one",
                "Hashtag_value": "#616880",
                "Followers_value": "128 followers",
                "Following_value": "25 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 373387,
        "Name": "Read Me Aloud",
        "Tagline": "iPad tales for kids who are learning to read",
        "Url": "https://www.producthunt.com/posts/read-me-aloud?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 36,
        "Makers": [
            {
                "Name": "Davide Benini",
                "Desgination": "Maker of Menu Plan and Read me Aloud",
                "Hashtag_value": "#4927581",
                "Followers_value": "9 followers",
                "Following_value": "9 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377229,
        "Name": "DeepReview",
        "Tagline": "Write CVs, cover letters, perf reviews with the power of AI",
        "Url": "https://www.producthunt.com/posts/deepreview?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 30,
        "Makers": [
            {
                "Name": "Liviu Coman",
                "Desgination": "",
                "Hashtag_value": "#621551",
                "Followers_value": "16 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Horia Coman",
                "Desgination": "Software engineer at Stack Overflow",
                "Hashtag_value": "#1084158",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377177,
        "Name": "Git Assistant",
        "Tagline": "Describe a feature; get a pull request. Github + Chat GPT",
        "Url": "https://www.producthunt.com/posts/git-assistant?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 26,
        "Makers": [
            {
                "Name": "Andrew Kondelin",
                "Desgination": "Developer, improving my marketing skills",
                "Hashtag_value": "#5043781",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377160,
        "Name": "Anagramish",
        "Tagline": "web based word game combining anagrams and word ladders ",
        "Url": "https://www.producthunt.com/posts/anagramish?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 28,
        "Makers": [
            {
                "Name": "Evan Haveman",
                "Desgination": "",
                "Hashtag_value": "#119614",
                "Followers_value": "88 followers",
                "Following_value": "187 following",
                "Twitter Url": "https://twitter.com/emh",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377249,
        "Name": "EffectiveGPT",
        "Tagline": "Get accurate ChatGPT prompts",
        "Url": "https://www.producthunt.com/posts/effectivegpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 26,
        "Makers": [
            {
                "Name": "Recurrsed",
                "Desgination": "I build random useless stuff...",
                "Hashtag_value": "#5061404",
                "Followers_value": "5 followers",
                "Following_value": "13 following",
                "Twitter Url": "",
                "Linkedin Url": ""
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
        "Makers": [
            {
                "Name": "Andy",
                "Desgination": "Bubbly Team",
                "Hashtag_value": "#4874262",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 374958,
        "Name": "Twitter for Noobs",
        "Tagline": "All-in-one Twitter growth framework and resource hub",
        "Url": "https://www.producthunt.com/posts/twitter-for-noobs?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 331,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376775,
        "Name": "ChatGenie",
        "Tagline": "Talk to any character, dead or alive, real or made up",
        "Url": "https://www.producthunt.com/posts/chatgenie?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 248,
        "Makers": [
            {
                "Name": "Patrick",
                "Desgination": "26 | Crafting stuff",
                "Hashtag_value": "#3822698",
                "Followers_value": "6 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376839,
        "Name": "Recipes By AI",
        "Tagline": "Generate recipes from a list of ingredients, powered by AI",
        "Url": "https://www.producthunt.com/posts/recipes-by-ai-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 195,
        "Makers": [
            {
                "Name": "Lewis Crutch",
                "Desgination": "Building Content Websites and AI Tools",
                "Hashtag_value": "#4744987",
                "Followers_value": "88 followers",
                "Following_value": "14 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377000,
        "Name": "wallaroo",
        "Tagline": "Wallpapers just for you (from the maker of Twitterrific)!",
        "Url": "https://www.producthunt.com/posts/wallaroo?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 151,
        "Makers": [
            {
                "Name": "Von Glitschka",
                "Desgination": "I create design and live near Bigfoot.",
                "Hashtag_value": "#4237016",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Craig Hockenberry",
                "Desgination": "I GETPAID TO TYPE",
                "Hashtag_value": "#3953190",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376815,
        "Name": "Møbel",
        "Tagline": "Transform your room with artificial intelligence.",
        "Url": "https://www.producthunt.com/posts/mobel-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 135,
        "Makers": [
            {
                "Name": "Pontus Aurdal",
                "Desgination": "IoT, AWS, serverless, event-driven.",
                "Hashtag_value": "#4138244",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376741,
        "Name": "Atomic",
        "Tagline": "Solve all your scheduling problems using AI for everyone",
        "Url": "https://www.producthunt.com/posts/atomic-4?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 115,
        "Makers": [
            {
                "Name": "Rish",
                "Desgination": "Indiehacker running a solo biz",
                "Hashtag_value": "#2466251",
                "Followers_value": "70 followers",
                "Following_value": "15 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376414,
        "Name": "Loti",
        "Tagline": "Remove non-consensual intimate images of yourself online.",
        "Url": "https://www.producthunt.com/posts/loti-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 97,
        "Makers": [
            {
                "Name": "Luke Arrigoni",
                "Desgination": "Founder of multiple AI companies.",
                "Hashtag_value": "#4741117",
                "Followers_value": "4 followers",
                "Following_value": "4 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/lukearrigoni/"
            },
            {
                "Name": "Rebekah Arrigoni",
                "Desgination": "Co-founder and CEO of Loti",
                "Hashtag_value": "#5090551",
                "Followers_value": "1 follower",
                "Following_value": "4 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/rebekah-arrigoni/"
            },
            {
                "Name": "Hirak Chhatbar",
                "Desgination": "Co-founder and Chief Technology Officer",
                "Hashtag_value": "#5090722",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376977,
        "Name": "Wifi QR Code",
        "Tagline": "Share your Wifi with friends & family",
        "Url": "https://www.producthunt.com/posts/wifi-qr-code?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 95,
        "Makers": [
            {
                "Name": "Max Sommer",
                "Desgination": "Web Developer. Curious person.",
                "Hashtag_value": "#5059466",
                "Followers_value": "11 followers",
                "Following_value": "3 following",
                "Twitter Url": "https://twitter.com/maxsommertweets",
                "Linkedin Url": "https://www.linkedin.com/in/max-sommer/"
            }
        ]
    },
    {
        "Id": 376966,
        "Name": "ChatGPT Prompts",
        "Tagline": "Prompts tailored for entrepreneurs, marketers, developers...",
        "Url": "https://www.producthunt.com/posts/chatgpt-prompts?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 96,
        "Makers": [
            {
                "Name": "Adrien",
                "Desgination": "",
                "Hashtag_value": "#2235632",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 373699,
        "Name": "Text2SQL.AI",
        "Tagline": "Generate SQL with AI",
        "Url": "https://www.producthunt.com/posts/text2sql-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 85,
        "Makers": [
            {
                "Name": "Gary Miklos",
                "Desgination": "Bootstrapped solopreneur.",
                "Hashtag_value": "#4792361",
                "Followers_value": "21 followers",
                "Following_value": "28 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376878,
        "Name": "Jobs Scout",
        "Tagline": "Improve your resume with the power of AI",
        "Url": "https://www.producthunt.com/posts/jobs-scout?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 90,
        "Makers": [
            {
                "Name": "Sasi",
                "Desgination": "I like to build stuff!",
                "Hashtag_value": "#1700183",
                "Followers_value": "29 followers",
                "Following_value": "36 following",
                "Twitter Url": "https://twitter.com/sasishan",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 377018,
        "Name": "What Word Is That?",
        "Tagline": "Find the right word when you need it",
        "Url": "https://www.producthunt.com/posts/what-word-is-that?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 79,
        "Makers": [
            {
                "Name": "Michael Li",
                "Desgination": "Software Engineer",
                "Hashtag_value": "#1365154",
                "Followers_value": "27 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376967,
        "Name": "Pencil AI",
        "Tagline": "Bring you the power of GPT-3 to you on telegram.",
        "Url": "https://www.producthunt.com/posts/pencil-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Makers": [
            {
                "Name": "Arafat Akata",
                "Desgination": "A software developer",
                "Hashtag_value": "#3428828",
                "Followers_value": "3 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376951,
        "Name": "Vucac",
        "Tagline": "Online whiteboard collaboration tool for every team",
        "Url": "https://www.producthunt.com/posts/vucac?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 50,
        "Makers": [
            {
                "Name": "Vaux Calvert",
                "Desgination": "A board",
                "Hashtag_value": "#4626266",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376953,
        "Name": "Circle",
        "Tagline": "Buy, store, receive and send Bitcoin super fast.",
        "Url": "https://www.producthunt.com/posts/circle-98339679-23ac-4593-a2f8-b9b63a697717?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Makers": [
            {
                "Name": "Manuel Pirhofer",
                "Desgination": "👋 Hi, I am Manuel",
                "Hashtag_value": "#4986211",
                "Followers_value": "2 followers",
                "Following_value": "3 following",
                "Twitter Url": "https://twitter.com/pirhofermanuel",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376940,
        "Name": "Time Boxing Planner",
        "Tagline": "Take back control of your time",
        "Url": "https://www.producthunt.com/posts/time-boxing-planner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 249,
        "Makers": [
            {
                "Name": "Sourabh",
                "Desgination": "The Notion Buddy",
                "Hashtag_value": "#4529667",
                "Followers_value": "228 followers",
                "Following_value": "17 following",
                "Twitter Url": "https://twitter.com/iamsourabhshen",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376914,
        "Name": "Mirror",
        "Tagline": "The home for web3 publishing",
        "Url": "https://www.producthunt.com/posts/mirror-11?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 223,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376834,
        "Name": "Notion Ultimate Life Planner",
        "Tagline": "Plan and achieve your goals effortlessly",
        "Url": "https://www.producthunt.com/posts/notion-ultimate-life-planner?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 288,
        "Makers": [
            {
                "Name": "Modest Mitkus",
                "Desgination": "Solopreneur",
                "Hashtag_value": "#3357966",
                "Followers_value": "1,278 followers",
                "Following_value": "241 following",
                "Twitter Url": "https://twitter.com/modestmitkus",
                "Linkedin Url": "https://www.linkedin.com/in/modestmitkus/"
            }
        ]
    },
    {
        "Id": 376645,
        "Name": "AutoPay",
        "Tagline": "Automate any recurring payment activity on-chain w/ AutoPay",
        "Url": "https://www.producthunt.com/posts/autopay?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 167,
        "Makers": [
            {
                "Name": "Priyanshu Panda",
                "Desgination": "",
                "Hashtag_value": "#4536916",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Deep Sheth",
                "Desgination": "Solving problems for content creators",
                "Hashtag_value": "#1871672",
                "Followers_value": "194 followers",
                "Following_value": "40 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376900,
        "Name": "IdeaTank",
        "Tagline": "Unlock opportunities through 1 on 1 connection with Ideators",
        "Url": "https://www.producthunt.com/posts/ideatank?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 137,
        "Makers": [
            {
                "Name": "Arpit",
                "Desgination": "Just Another Person Seeking Problems",
                "Hashtag_value": "#3448669",
                "Followers_value": "77 followers",
                "Following_value": "33 following",
                "Twitter Url": "https://twitter.com/0xarpitg",
                "Linkedin Url": "https://www.linkedin.com/in/arpit-goyal007/"
            },
            {
                "Name": "Aakash Kumar",
                "Desgination": "Building IdeaTank",
                "Hashtag_value": "#4992337",
                "Followers_value": "12 followers",
                "Following_value": "2 following",
                "Twitter Url": "https://twitter.com/kumaaraakash074",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376921,
        "Name": "Vikara",
        "Tagline": "Chatbot nutritionist to help you eat healthy",
        "Url": "https://www.producthunt.com/posts/vikara?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 96,
        "Makers": [
            {
                "Name": "Pravin Halady",
                "Desgination": "Building Vikara, a chatbot nutritionist",
                "Hashtag_value": "#4978814",
                "Followers_value": "33 followers",
                "Following_value": "10 following",
                "Twitter Url": "https://twitter.com/appvikara",
                "Linkedin Url": "https://www.linkedin.com/in/pravinhalady/"
            }
        ]
    },
    {
        "Id": 376949,
        "Name": "Cron Jobs Expert",
        "Tagline": "Create Cron job without line of code",
        "Url": "https://www.producthunt.com/posts/cron-jobs-expert?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 87,
        "Makers": [
            {
                "Name": "Daniel Nikulshyn",
                "Desgination": "Senior 👨‍💻",
                "Hashtag_value": "#3462647",
                "Followers_value": "43 followers",
                "Following_value": "5 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376916,
        "Name": "Optic Weather",
        "Tagline": "Experience the weather like never before",
        "Url": "https://www.producthunt.com/posts/optic-weather?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Makers": [
            {
                "Name": "Tonye",
                "Desgination": "No",
                "Hashtag_value": "#2924416",
                "Followers_value": "11 followers",
                "Following_value": "1 following",
                "Twitter Url": "https://twitter.com/truevined",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376917,
        "Name": "Tab Manager Auto",
        "Tagline": "Effortlessly boost your productivity with Tab Manager Auto.",
        "Url": "https://www.producthunt.com/posts/tab-manager-auto?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Makers": [
            {
                "Name": "Kevin Wang",
                "Desgination": "Building chrome extensions.",
                "Hashtag_value": "#5000605",
                "Followers_value": "8 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376633,
        "Name": "Plum Notes",
        "Tagline": "Note taking application with a different focus.",
        "Url": "https://www.producthunt.com/posts/plum-notes?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Makers": [
            {
                "Name": "Ian Mora",
                "Desgination": "Cretor of plum notes app.",
                "Hashtag_value": "#4734910",
                "Followers_value": "3 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375646,
        "Name": "mock.qa",
        "Tagline": "gRPC and HTTP mock APIs in the cloud",
        "Url": "https://www.producthunt.com/posts/mock-qa?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 66,
        "Makers": [
            {
                "Name": "Evgeniy Kosjakov",
                "Desgination": "Senior Test Automation Engineer",
                "Hashtag_value": "#3616774",
                "Followers_value": "58 followers",
                "Following_value": "5 following",
                "Twitter Url": "https://twitter.com/elv1s42",
                "Linkedin Url": ""
            },
            {
                "Name": "Victor Vorobyev",
                "Desgination": "Software Engineer",
                "Hashtag_value": "#3654534",
                "Followers_value": "20 followers",
                "Following_value": "8 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Vladimir Solovev",
                "Desgination": "Software Engineer",
                "Hashtag_value": "#3654567",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376886,
        "Name": "OmniWork",
        "Tagline": "One link to run your business",
        "Url": "https://www.producthunt.com/posts/omniwork-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 56,
        "Makers": [
            {
                "Name": "Flavio",
                "Desgination": "Developer",
                "Hashtag_value": "#4679562",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Sohrab Tellaie",
                "Desgination": "I'm Sohrab. CEO & Co-founder of OmniWork",
                "Hashtag_value": "#4594633",
                "Followers_value": "7 followers",
                "Following_value": "1 following",
                "Twitter Url": "https://twitter.com/sohrabtellaie",
                "Linkedin Url": ""
            },
            {
                "Name": "Lawrence Chan",
                "Desgination": "Making Great Products Greater",
                "Hashtag_value": "#4819038",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Mazdak Sorosh",
                "Desgination": "",
                "Hashtag_value": "#4824063",
                "Followers_value": "1 follower",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Beezhan",
                "Desgination": "",
                "Hashtag_value": "#4818973",
                "Followers_value": "3 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376929,
        "Name": "Dookey Dash",
        "Tagline": "Dookey Dash is a skill-based mint by Yuga Labs",
        "Url": "https://www.producthunt.com/posts/dookey-dash?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 46,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376772,
        "Name": "Calendar Query",
        "Tagline": "Query your Google Calendar with SQL",
        "Url": "https://www.producthunt.com/posts/calendar-query?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 41,
        "Makers": [
            {
                "Name": "Devon Bradley",
                "Desgination": "Shipping software products 🚀",
                "Hashtag_value": "#522593",
                "Followers_value": "102 followers",
                "Following_value": "160 following",
                "Twitter Url": "https://twitter.com/devonsbradley",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376743,
        "Name": "Furmasterpiece Pet Avatar Creator",
        "Tagline": "Furmasterpiece turns any pet photo into a stunning avatar",
        "Url": "https://www.producthunt.com/posts/furmasterpiece-pet-avatar-creator?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Makers": [
            {
                "Name": "Rando Tkatsenko",
                "Desgination": "Building cool stuff with Unity- VR, AI.",
                "Hashtag_value": "#4942150",
                "Followers_value": "7 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376937,
        "Name": "GiftBot: Love Edition",
        "Tagline": "Valentines Day gift help from a GPT-3 chatbot",
        "Url": "https://www.producthunt.com/posts/giftbot-love-edition?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 40,
        "Makers": [
            {
                "Name": "Anish Thite",
                "Desgination": "Master procrastinator",
                "Hashtag_value": "#3073292",
                "Followers_value": "44 followers",
                "Following_value": "294 following",
                "Twitter Url": "https://twitter.com/thiteanish",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376701,
        "Name": "Internet Is Beautiful",
        "Tagline": "Discover the most interesting, weird and awesome websites",
        "Url": "https://www.producthunt.com/posts/internet-is-beautiful?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 747,
        "Makers": [
            {
                "Name": "Jaisal Rathee",
                "Desgination": "Building www.startups.fyi 🦄",
                "Hashtag_value": "#2711861",
                "Followers_value": "221 followers",
                "Following_value": "17 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376690,
        "Name": "WorkHub Connect for Mobile",
        "Tagline": "External and Internal communication on the go",
        "Url": "https://www.producthunt.com/posts/workhub-connect-for-mobile?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 651,
        "Makers": [
            {
                "Name": "Hamza Afzal Butt",
                "Desgination": "B2B SaaS Growth Marketing Consultant",
                "Hashtag_value": "#3830504",
                "Followers_value": "361 followers",
                "Following_value": "68 following",
                "Twitter Url": "https://twitter.com/hamzabuttt40",
                "Linkedin Url": "https://www.linkedin.com/in/hamzaafzalbutt/"
            },
            {
                "Name": "Qudsia Ali",
                "Desgination": "Director at WorkHub",
                "Hashtag_value": "#4136209",
                "Followers_value": "759 followers",
                "Following_value": "278 following",
                "Twitter Url": "https://twitter.com/qudsiapiracha",
                "Linkedin Url": "https://www.linkedin.com/in/qudsia-piracha-77760571/"
            },
            {
                "Name": "Sidra Ali",
                "Desgination": "Founder @Vadoreu",
                "Hashtag_value": "#4254865",
                "Followers_value": "66 followers",
                "Following_value": "28 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/sidraarifali/"
            },
            {
                "Name": "Noshaid Ali",
                "Desgination": "Senior Software Engineer",
                "Hashtag_value": "#4737016",
                "Followers_value": "11 followers",
                "Following_value": "28 following",
                "Twitter Url": "https://twitter.com/thenoshade",
                "Linkedin Url": "https://www.linkedin.com/in/noshaid/"
            },
            {
                "Name": "Bilal Anwar",
                "Desgination": "Mobile App Developer @ Workhub",
                "Hashtag_value": "#4219262",
                "Followers_value": "31 followers",
                "Following_value": "8 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Aqsa Sajjad",
                "Desgination": "Digital Marketing",
                "Hashtag_value": "#4276310",
                "Followers_value": "98 followers",
                "Following_value": "22 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/aqsa-sajjad/"
            },
            {
                "Name": "Ali Naqi Shaheen",
                "Desgination": "Entrepreneur, Angel Investor",
                "Hashtag_value": "#617409",
                "Followers_value": "222 followers",
                "Following_value": "445 following",
                "Twitter Url": "https://twitter.com/alishaheen",
                "Linkedin Url": ""
            },
            {
                "Name": "Nabeel Amir",
                "Desgination": "I am the Product Owner @ WorkHub",
                "Hashtag_value": "#4136648",
                "Followers_value": "178 followers",
                "Following_value": "83 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376172,
        "Name": "The Help Center Academy",
        "Tagline": "Learn the secrets of building a successful help center",
        "Url": "https://www.producthunt.com/posts/the-help-center-academy?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 332,
        "Makers": [
            {
                "Name": "Dominik Sobe",
                "Desgination": "⚡Indie Hacker building interweb products",
                "Hashtag_value": "#1485377",
                "Followers_value": "1,707 followers",
                "Following_value": "602 following",
                "Twitter Url": "https://twitter.com/sobedominik",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376770,
        "Name": "Makelog",
        "Tagline": "Autogenerate your changelog with GPT-3",
        "Url": "https://www.producthunt.com/posts/makelog?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 286,
        "Makers": [
            {
                "Name": "JJ Nguyen",
                "Desgination": "",
                "Hashtag_value": "#2806365",
                "Followers_value": "395 followers",
                "Following_value": "355 following",
                "Twitter Url": "https://twitter.com/hijuliejennifer",
                "Linkedin Url": ""
            },
            {
                "Name": "Julio Farah",
                "Desgination": "f",
                "Hashtag_value": "#3175551",
                "Followers_value": "2 followers",
                "Following_value": "52 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Jacob Hubbard",
                "Desgination": "building makelog",
                "Hashtag_value": "#4975999",
                "Followers_value": "1 follower",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Logan Liffick",
                "Desgination": "Senior Designer at DigitalOcean",
                "Hashtag_value": "#3905664",
                "Followers_value": "12 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Briton Baker",
                "Desgination": "Product Designer",
                "Hashtag_value": "#3080336",
                "Followers_value": "3 followers",
                "Following_value": "7 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375921,
        "Name": "Pitchdeck Challenge",
        "Tagline": "10 Days to master your pitchdeck creation",
        "Url": "https://www.producthunt.com/posts/pitchdeck-challenge?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 269,
        "Makers": [
            {
                "Name": "Sebastian Janus - derStartupCFO",
                "Desgination": "Founder & Serial Entrepreneur",
                "Hashtag_value": "#3086104",
                "Followers_value": "402 followers",
                "Following_value": "292 following",
                "Twitter Url": "https://twitter.com/sebjanuscom",
                "Linkedin Url": "https://www.linkedin.com/in/sebjanus/"
            }
        ]
    },
    {
        "Id": 376388,
        "Name": "Inside AI",
        "Tagline": "The most complete AI Newsletter",
        "Url": "https://www.producthunt.com/posts/inside-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 402,
        "Makers": [
            {
                "Name": "Jan Sulek",
                "Desgination": "AI Newsletter - insideai.co",
                "Hashtag_value": "#4877025",
                "Followers_value": "5 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376177,
        "Name": "Product Launch AI",
        "Tagline": "Supercharge your Product Launches with the Power of AI",
        "Url": "https://www.producthunt.com/posts/product-launch-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 218,
        "Makers": [
            {
                "Name": "Adithya Shreshti",
                "Desgination": "Startup Launch & NoCode Consultant",
                "Hashtag_value": "#443764",
                "Followers_value": "1,742 followers",
                "Following_value": "357 following",
                "Twitter Url": "https://twitter.com/adithyashreshti",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376859,
        "Name": "MusicLM by Google",
        "Tagline": "A text to music AI model by Google",
        "Url": "https://www.producthunt.com/posts/musiclm-by-google?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 190,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376393,
        "Name": "Casper",
        "Tagline": "GPT-3 in your iPhone keyboard",
        "Url": "https://www.producthunt.com/posts/casper-5?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 200,
        "Makers": [
            {
                "Name": "Johan",
                "Desgination": "Building and thinking AI stuff",
                "Hashtag_value": "#4613682",
                "Followers_value": "34 followers",
                "Following_value": "4 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376755,
        "Name": "Social Media Manager",
        "Tagline": "Plan your social media content like a pro",
        "Url": "https://www.producthunt.com/posts/social-media-manager-2?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 94,
        "Makers": [
            {
                "Name": "Brian",
                "Desgination": "Product Designer & Notion Creator",
                "Hashtag_value": "#4570937",
                "Followers_value": "190 followers",
                "Following_value": "18 following",
                "Twitter Url": "https://twitter.com/heyybrian_",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376125,
        "Name": "dbt-infer",
        "Tagline": "Next-Gen analytics for dbt, supercharge models with Infer",
        "Url": "https://www.producthunt.com/posts/dbt-infer?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 86,
        "Makers": [
            {
                "Name": "Ryan Garland",
                "Desgination": "Hello!",
                "Hashtag_value": "#4554646",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Erik Mathiesen-Dreyfus",
                "Desgination": "Founder@Infer",
                "Hashtag_value": "#4564117",
                "Followers_value": "7 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/erikarne/"
            }
        ]
    },
    {
        "Id": 376565,
        "Name": "The Guest Posts App",
        "Tagline": "A new way to find guest posts faster",
        "Url": "https://www.producthunt.com/posts/the-guest-posts-app?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 82,
        "Makers": [
            {
                "Name": "Siddharth Verma",
                "Desgination": "SAAS Consultant | Startups | AI/NLP",
                "Hashtag_value": "#1435795",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "https://twitter.com/sidieverma",
                "Linkedin Url": "https://www.linkedin.com/in/4r7ur/"
            }
        ]
    },
    {
        "Id": 376789,
        "Name": "hai Infusions Smart Showerhead",
        "Tagline": "Your daily shower, reimagined with smart tech",
        "Url": "https://www.producthunt.com/posts/hai-infusions-smart-showerhead?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 209,
        "Makers": [
            {
                "Name": "Leah Stigile",
                "Desgination": "Co-founder & CEO",
                "Hashtag_value": "#5026146",
                "Followers_value": "7 followers",
                "Following_value": "6 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Gina Oh",
                "Desgination": "Cofounder",
                "Hashtag_value": "#5049098",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Kate Starr",
                "Desgination": "VP and storyteller of amazing showers.",
                "Hashtag_value": "#4992957",
                "Followers_value": "5 followers",
                "Following_value": "4 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Monika Markovinovic",
                "Desgination": "content person. loves the internet.",
                "Hashtag_value": "#5048420",
                "Followers_value": "2 followers",
                "Following_value": "5 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Leonard Brody",
                "Desgination": "CEO",
                "Hashtag_value": "#50765",
                "Followers_value": "327 followers",
                "Following_value": "140 following",
                "Twitter Url": "https://twitter.com/lbrody",
                "Linkedin Url": ""
            },
            {
                "Name": "Madi Fisk",
                "Desgination": "Intern @hai",
                "Hashtag_value": "#5072272",
                "Followers_value": "3 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376731,
        "Name": "Welma",
        "Tagline": "Understand and retain complex text with the help of AI",
        "Url": "https://www.producthunt.com/posts/welma?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 75,
        "Makers": [
            {
                "Name": "Mighil",
                "Desgination": "globe-earther and schnauzer enthusiast",
                "Hashtag_value": "#3955223",
                "Followers_value": "142 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376786,
        "Name": "Followup Fish",
        "Tagline": "Bubble up emails back to the top of your inbox",
        "Url": "https://www.producthunt.com/posts/followup-fish?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 67,
        "Makers": [
            {
                "Name": "Marc Köhlbrugge",
                "Desgination": "Founder of BetaList",
                "Hashtag_value": "#497",
                "Followers_value": "16,768 followers",
                "Following_value": "132 following",
                "Twitter Url": "https://twitter.com/marckohlbrugge",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376802,
        "Name": "Extractify",
        "Tagline": "Convert Youtube videos into Tweets and LinkedIn posts",
        "Url": "https://www.producthunt.com/posts/extractify?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 64,
        "Makers": [
            {
                "Name": "Ahsan Shahid",
                "Desgination": "Builder",
                "Hashtag_value": "#4339504",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375422,
        "Name": "Spot a Bot",
        "Tagline": "Get insights into the bot activity for Twitter trends",
        "Url": "https://www.producthunt.com/posts/spot-a-bot?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 77,
        "Makers": [
            {
                "Name": "Nicolas Graf",
                "Desgination": "Heavy web consumer and creator.",
                "Hashtag_value": "#4992419",
                "Followers_value": "15 followers",
                "Following_value": "4 following",
                "Twitter Url": "https://twitter.com/nckgrf",
                "Linkedin Url": ""
            },
            {
                "Name": "Kevin Harizaj",
                "Desgination": "Developer",
                "Hashtag_value": "#4996795",
                "Followers_value": "3 followers",
                "Following_value": "11 following",
                "Twitter Url": "https://twitter.com/realkevharizaj",
                "Linkedin Url": ""
            },
            {
                "Name": "Lena Heiglauer",
                "Desgination": "Developer @ Spot A Bot",
                "Hashtag_value": "#4049106",
                "Followers_value": "10 followers",
                "Following_value": "6 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Daniela Dottolo",
                "Desgination": "Web Development student from Austria 🌈",
                "Hashtag_value": "#5012622",
                "Followers_value": "13 followers",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376669,
        "Name": "Semantic AI",
        "Tagline": "The fullstack AI writing suite, that gives you back control",
        "Url": "https://www.producthunt.com/posts/semantic-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 52,
        "Makers": [
            {
                "Name": "Amu",
                "Desgination": "Founder of Sentiment",
                "Hashtag_value": "#3598879",
                "Followers_value": "19 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376685,
        "Name": "MailGPT",
        "Tagline": "Experience the convenience",
        "Url": "https://www.producthunt.com/posts/mailgpt?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 48,
        "Makers": [
            {
                "Name": "Sourav Kumar Pradhan",
                "Desgination": "Developer",
                "Hashtag_value": "#985273",
                "Followers_value": "60 followers",
                "Following_value": "73 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376717,
        "Name": "Multichain Playbook",
        "Tagline": "Unlock the potential of NFT Project with multichain playbook",
        "Url": "https://www.producthunt.com/posts/multichain-playbook?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 42,
        "Makers": [
            {
                "Name": "Dinesh Kruplani",
                "Desgination": "Growth & Marketing at Dehidden",
                "Hashtag_value": "#3696955",
                "Followers_value": "50 followers",
                "Following_value": "115 following",
                "Twitter Url": "https://twitter.com/dineshkruplani",
                "Linkedin Url": ""
            },
            {
                "Name": "Ramees P S",
                "Desgination": "Product | Growth | Crypto",
                "Hashtag_value": "#3064307",
                "Followers_value": "54 followers",
                "Following_value": "42 following",
                "Twitter Url": "https://twitter.com/ramzps",
                "Linkedin Url": ""
            },
            {
                "Name": "Sangeet Muralidhar",
                "Desgination": "building stuff",
                "Hashtag_value": "#5075749",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Sahil Pednekar",
                "Desgination": "Product Designer, NFT Artist",
                "Hashtag_value": "#3952116",
                "Followers_value": "55 followers",
                "Following_value": "103 following",
                "Twitter Url": "https://twitter.com/sahil6339",
                "Linkedin Url": ""
            },
            {
                "Name": "Avinash Kumar",
                "Desgination": "Product Designer",
                "Hashtag_value": "#4962795",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "https://twitter.com/__avinashkumar_",
                "Linkedin Url": ""
            },
            {
                "Name": "Harikrishnaraj",
                "Desgination": "Project Manager",
                "Hashtag_value": "#5075850",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376640,
        "Name": "Oura for Apple Watch",
        "Tagline": "Be mindful of your health data while you’re on the go",
        "Url": "https://www.producthunt.com/posts/oura-for-apple-watch?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 34,
        "Makers": [
            {
                "Name": "Jason Russell",
                "Desgination": "Director of Product at Oura Ring",
                "Hashtag_value": "#226335",
                "Followers_value": "150 followers",
                "Following_value": "177 following",
                "Twitter Url": "https://twitter.com/thisisthequick",
                "Linkedin Url": ""
            },
            {
                "Name": "Petteri Lahtela",
                "Desgination": "CEO, Co-Founder at ŌURA",
                "Hashtag_value": "#295979",
                "Followers_value": "296 followers",
                "Following_value": "198 following",
                "Twitter Url": "https://twitter.com/plahtela",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376756,
        "Name": "ciphergoat",
        "Tagline": "Encrypt and backup your recovery seed phrases",
        "Url": "https://www.producthunt.com/posts/ciphergoat?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 54,
        "Makers": [
            {
                "Name": "Aaron Pardes",
                "Desgination": "Building things with code",
                "Hashtag_value": "#82197",
                "Followers_value": "39 followers",
                "Following_value": "142 following",
                "Twitter Url": "https://twitter.com/aaronpardes",
                "Linkedin Url": ""
            },
            {
                "Name": "Danilo Bandovic",
                "Desgination": "Lawyer with a business mindset.",
                "Hashtag_value": "#5014999",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Ron Edgar",
                "Desgination": "CEO & Co-founder | Genius Goat Labs Inc.",
                "Hashtag_value": "#4916950",
                "Followers_value": "7 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376757,
        "Name": "SULO-Y",
        "Tagline": "Trash bins just got smarter",
        "Url": "https://www.producthunt.com/posts/sulo-y?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 21,
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376750,
        "Name": "SpicyHR",
        "Tagline": "Forget Lever. SpicyHR is lightweight, intuitive, and FAST.",
        "Url": "https://www.producthunt.com/posts/spicyhr?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Makers": [
            {
                "Name": "Ali Mir",
                "Desgination": "Co-founder at Spicy.hr",
                "Hashtag_value": "#1193949",
                "Followers_value": "8 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/ali-mir-44541a253/"
            },
            {
                "Name": "Meisam Movassat",
                "Desgination": "Co-founder at Vasona; simplify hiring.",
                "Hashtag_value": "#4975789",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
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
        "Makers": [
            {
                "Name": "",
                "Desgination": "",
                "Hashtag_value": "",
                "Followers_value": "",
                "Following_value": "",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376758,
        "Name": "Lightness",
        "Tagline": "App for meeting new people, exploring cultures and messaging",
        "Url": "https://www.producthunt.com/posts/lightness?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Makers": [
            {
                "Name": "Stefano Ippolito Gitto",
                "Desgination": "Founder of Lightness",
                "Hashtag_value": "#5081944",
                "Followers_value": "0 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376855,
        "Name": "Moodlody",
        "Tagline": "make you feel relaxed",
        "Url": "https://www.producthunt.com/posts/moodlody?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 20,
        "Makers": [
            {
                "Name": "Dream.Chayutpong",
                "Desgination": "Front-End Developer.",
                "Hashtag_value": "#5012375",
                "Followers_value": "9 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/chayutpong/"
            }
        ]
    },
    {
        "Id": 376875,
        "Name": "Todidlist",
        "Tagline": "Simple place to track what you've done",
        "Url": "https://www.producthunt.com/posts/todidlist?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 18,
        "Makers": [
            {
                "Name": "Patrick Tran",
                "Desgination": "",
                "Hashtag_value": "#1707886",
                "Followers_value": "1 follower",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376434,
        "Name": "Ask by Slite",
        "Tagline": "Use AI to ask your workspace questions",
        "Url": "https://www.producthunt.com/posts/ask-by-slite?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 906,
        "Makers": [
            {
                "Name": "Christophe Pasquier",
                "Desgination": "Founder @ Slite",
                "Hashtag_value": "#40739",
                "Followers_value": "1,446 followers",
                "Following_value": "541 following",
                "Twitter Url": "https://twitter.com/christophepas",
                "Linkedin Url": ""
            },
            {
                "Name": "Jon McCullough",
                "Desgination": "Product Marketing at Slite",
                "Hashtag_value": "#476481",
                "Followers_value": "172 followers",
                "Following_value": "315 following",
                "Twitter Url": "https://twitter.com/jonmccull",
                "Linkedin Url": ""
            },
            {
                "Name": "Pierre Renaudin",
                "Desgination": "Sliter",
                "Hashtag_value": "#1014532",
                "Followers_value": "356 followers",
                "Following_value": "79 following",
                "Twitter Url": "https://twitter.com/pierrerenaudin",
                "Linkedin Url": ""
            },
            {
                "Name": "Ani Cordani",
                "Desgination": "",
                "Hashtag_value": "#4352008",
                "Followers_value": "11 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Clara Rua",
                "Desgination": "Product designer",
                "Hashtag_value": "#1081895",
                "Followers_value": "299 followers",
                "Following_value": "422 following",
                "Twitter Url": "https://twitter.com/clara_rua",
                "Linkedin Url": ""
            },
            {
                "Name": "Brieuc Sebillotte",
                "Desgination": "",
                "Hashtag_value": "#796877",
                "Followers_value": "193 followers",
                "Following_value": "268 following",
                "Twitter Url": "https://twitter.com/brieuc1",
                "Linkedin Url": "https://www.linkedin.com/"
            },
            {
                "Name": "Antoine Duban",
                "Desgination": "",
                "Hashtag_value": "#1126563",
                "Followers_value": "6 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "michael bartlett",
                "Desgination": "",
                "Hashtag_value": "#18940",
                "Followers_value": "355 followers",
                "Following_value": "279 following",
                "Twitter Url": "https://twitter.com/mydigitalself",
                "Linkedin Url": ""
            },
            {
                "Name": "Arnaud Rinquin",
                "Desgination": "",
                "Hashtag_value": "#109130",
                "Followers_value": "274 followers",
                "Following_value": "361 following",
                "Twitter Url": "https://twitter.com/arnaudrinquin",
                "Linkedin Url": ""
            },
            {
                "Name": "Laure Albouy",
                "Desgination": "marketing @ bonsai",
                "Hashtag_value": "#704767",
                "Followers_value": "393 followers",
                "Following_value": "346 following",
                "Twitter Url": "https://twitter.com/laure_albouy",
                "Linkedin Url": ""
            },
            {
                "Name": "Rob McMackin",
                "Desgination": "Product designer @ Slite",
                "Hashtag_value": "#731864",
                "Followers_value": "214 followers",
                "Following_value": "263 following",
                "Twitter Url": "https://twitter.com/robbmcm",
                "Linkedin Url": ""
            },
            {
                "Name": "Adrien Taravant",
                "Desgination": "",
                "Hashtag_value": "#140517",
                "Followers_value": "103 followers",
                "Following_value": "187 following",
                "Twitter Url": "https://twitter.com/ataravant",
                "Linkedin Url": "https://www.linkedin.com/in/adrien-taravant/"
            },
            {
                "Name": "Guillaume Morin",
                "Desgination": "Lead Mobile engineer @slitehq 👨‍💻📱⚛️",
                "Hashtag_value": "#588483",
                "Followers_value": "42 followers",
                "Following_value": "201 following",
                "Twitter Url": "https://twitter.com/guillaume_morin",
                "Linkedin Url": ""
            },
            {
                "Name": "Alexandre Gaudencio",
                "Desgination": "Spaceship launcher @ Slite",
                "Hashtag_value": "#25271",
                "Followers_value": "108 followers",
                "Following_value": "107 following",
                "Twitter Url": "https://twitter.com/shahor",
                "Linkedin Url": ""
            },
            {
                "Name": "Clément Rucheton",
                "Desgination": "",
                "Hashtag_value": "#1126564",
                "Followers_value": "23 followers",
                "Following_value": "23 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Charley D.",
                "Desgination": "",
                "Hashtag_value": "#109053",
                "Followers_value": "121 followers",
                "Following_value": "18 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Fadeelah Al-horaibi",
                "Desgination": "Head of Product @Slite",
                "Hashtag_value": "#2386400",
                "Followers_value": "12 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375110,
        "Name": "Charlie",
        "Tagline": "Helping everyone create marketing content",
        "Url": "https://www.producthunt.com/posts/charlie-6?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 974,
        "Makers": [
            {
                "Name": "Brennan Woodruff",
                "Desgination": "Finance guy gone AI Product Developer",
                "Hashtag_value": "#4598581",
                "Followers_value": "48 followers",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Kostas Hatalis",
                "Desgination": "CEO of GoCharlie.ai",
                "Hashtag_value": "#4652960",
                "Followers_value": "5 followers",
                "Following_value": "3 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/kostashatalis/"
            },
            {
                "Name": "Despina Christou",
                "Desgination": ".",
                "Hashtag_value": "#4650944",
                "Followers_value": "5 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 374952,
        "Name": "NeevaAI",
        "Tagline": "Search powered by AI to get answers, not ads",
        "Url": "https://www.producthunt.com/posts/neevaai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 1117,
        "Makers": [
            {
                "Name": "Hwi Lee",
                "Desgination": "Head of Design @Neeva",
                "Hashtag_value": "#3979291",
                "Followers_value": "14 followers",
                "Following_value": "19 following",
                "Twitter Url": "https://twitter.com/hwiilee",
                "Linkedin Url": "https://www.linkedin.com/in/hwikyounglee/"
            },
            {
                "Name": "Yusuf Ozuysal",
                "Desgination": "Mobile @Neeva",
                "Hashtag_value": "#3988463",
                "Followers_value": "10 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Jiwoong Lee",
                "Desgination": "UX designer, Neeva",
                "Hashtag_value": "#588834",
                "Followers_value": "79 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Rajhans Samdani",
                "Desgination": "Head of Machine Learning, Neeva",
                "Hashtag_value": "#880868",
                "Followers_value": "188 followers",
                "Following_value": "48 following",
                "Twitter Url": "https://twitter.com/rajhans_samdani",
                "Linkedin Url": ""
            },
            {
                "Name": "Edmund Loo",
                "Desgination": "edmundloo.com",
                "Hashtag_value": "#971504",
                "Followers_value": "27 followers",
                "Following_value": "15 following",
                "Twitter Url": "https://twitter.com/edmundsayshi",
                "Linkedin Url": ""
            },
            {
                "Name": "Darin Fisher",
                "Desgination": "browser builder @neeva",
                "Hashtag_value": "#3557018",
                "Followers_value": "29 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/darin-fisher-7059ab/"
            },
            {
                "Name": "Sridhar Ramaswamy",
                "Desgination": "@neeva Co-Founder Ex-@Google SVP Ads",
                "Hashtag_value": "#3522651",
                "Followers_value": "111 followers",
                "Following_value": "2 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/sridhar-ramaswamy/"
            },
            {
                "Name": "Rachel Cheng",
                "Desgination": "Product Designer",
                "Hashtag_value": "#819888",
                "Followers_value": "145 followers",
                "Following_value": "378 following",
                "Twitter Url": "https://twitter.com/ahraycho",
                "Linkedin Url": ""
            },
            {
                "Name": "Anton Borzov",
                "Desgination": "Product Design. Formerly @WhatsApp.",
                "Hashtag_value": "#167543",
                "Followers_value": "376 followers",
                "Following_value": "1,268 following",
                "Twitter Url": "https://twitter.com/tyggy",
                "Linkedin Url": ""
            },
            {
                "Name": "Seth Li",
                "Desgination": "Growth @ Neeva",
                "Hashtag_value": "#3553263",
                "Followers_value": "14 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Cooper LaRhette",
                "Desgination": "SWE @ Neeva",
                "Hashtag_value": "#3990531",
                "Followers_value": "2 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376466,
        "Name": "WritingMate.ai",
        "Tagline": "Free ChatGPT alternative that works as a Chrome extension",
        "Url": "https://www.producthunt.com/posts/writingmate-ai?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 739,
        "Makers": [
            {
                "Name": "Alexander Nevedovsky",
                "Desgination": "",
                "Hashtag_value": "#1105511",
                "Followers_value": "357 followers",
                "Following_value": "1,676 following",
                "Twitter Url": "https://twitter.com/ednevsky",
                "Linkedin Url": "https://www.linkedin.com/in/ednevsky/"
            },
            {
                "Name": "Artem Vysotsky",
                "Desgination": "",
                "Hashtag_value": "#1616664",
                "Followers_value": "23 followers",
                "Following_value": "8 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375784,
        "Name": "Conektto API-First Design Studio",
        "Tagline": "API design studio for product managers",
        "Url": "https://www.producthunt.com/posts/conektto-api-first-design-studio?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 541,
        "Makers": [
            {
                "Name": "Ram Sathia",
                "Desgination": "Automation obsessed technologist",
                "Hashtag_value": "#4344282",
                "Followers_value": "79 followers",
                "Following_value": "222 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Amol Dewhare",
                "Desgination": "Founder & CEO of Conektto",
                "Hashtag_value": "#4641853",
                "Followers_value": "18 followers",
                "Following_value": "43 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Madhu V Swamy",
                "Desgination": "Technopreneur building digital products",
                "Hashtag_value": "#4161146",
                "Followers_value": "43 followers",
                "Following_value": "83 following",
                "Twitter Url": "https://twitter.com/madhuworldwide",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 375864,
        "Name": "Figma to WordPress Beta",
        "Tagline": "Convert Figma to WordPress websites & themes automatically",
        "Url": "https://www.producthunt.com/posts/figma-to-wordpress-beta?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 462,
        "Makers": [
            {
                "Name": "Alfonso García Frey",
                "Desgination": "Building nextgen design technology",
                "Hashtag_value": "#877476",
                "Followers_value": "133 followers",
                "Following_value": "1,468 following",
                "Twitter Url": "https://twitter.com/garciafrey",
                "Linkedin Url": ""
            },
            {
                "Name": "Cédric Legendre",
                "Desgination": "",
                "Hashtag_value": "#1555388",
                "Followers_value": "15 followers",
                "Following_value": "35 following",
                "Twitter Url": "https://twitter.com/cackbone",
                "Linkedin Url": ""
            },
            {
                "Name": "Maurício",
                "Desgination": "Software Dev, gamer and guitar player",
                "Hashtag_value": "#4556405",
                "Followers_value": "10 followers",
                "Following_value": "51 following",
                "Twitter Url": "https://twitter.com/maublum",
                "Linkedin Url": ""
            },
            {
                "Name": "Ali mot",
                "Desgination": "Software engineer",
                "Hashtag_value": "#4553224",
                "Followers_value": "6 followers",
                "Following_value": "1 following",
                "Twitter Url": "",
                "Linkedin Url": "https://www.linkedin.com/in/ali-mottaghian-1b3a73102/"
            },
            {
                "Name": "Ilyes El ayeb",
                "Desgination": "software engineer",
                "Hashtag_value": "#4492146",
                "Followers_value": "7 followers",
                "Following_value": "6 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Sanine Moreira",
                "Desgination": "",
                "Hashtag_value": "#1197996",
                "Followers_value": "4 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    },
    {
        "Id": 376506,
        "Name": "Alt Sprints",
        "Tagline": "Idea to MVP in 2 weeks",
        "Url": "https://www.producthunt.com/posts/alt-sprints?utm_campaign=producthunt-api&utm_medium=api-v2&utm_source=Application%3A+test2+%28ID%3A+95747%29",
        "Votescount": 295,
        "Makers": [
            {
                "Name": "Ali Haider",
                "Desgination": "Building a venture studio",
                "Hashtag_value": "#4885174",
                "Followers_value": "26 followers",
                "Following_value": "13 following",
                "Twitter Url": "https://mobile.twitter.com/alihaideratiq",
                "Linkedin Url": "https://www.linkedin.com/in/ali-haider-atiq-khurshid-5b454892/?originalsubdomain=pk"
            },
            {
                "Name": "Ahsan Asghar",
                "Desgination": "Product Manager",
                "Hashtag_value": "#4688836",
                "Followers_value": "15 followers",
                "Following_value": "9 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Ahsan Sohail",
                "Desgination": "Venture Builder @ Alt Sprints",
                "Hashtag_value": "#4688852",
                "Followers_value": "24 followers",
                "Following_value": "53 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Yetunde Lopez",
                "Desgination": "Product designer",
                "Hashtag_value": "#4160460",
                "Followers_value": "6 followers",
                "Following_value": "6 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            },
            {
                "Name": "Umair Abdullah",
                "Desgination": "Founder, digital nomad and storyteller.",
                "Hashtag_value": "#4976712",
                "Followers_value": "5 followers",
                "Following_value": "0 following",
                "Twitter Url": "",
                "Linkedin Url": ""
            }
        ]
    }
]
# Write the combined data to a new file


fd = pd.read_excel("merged_file.xlsx",sheet_name="Sheet1")
fd_url = fd["Website"] 
print(fd_url)
fd_url_list =[ pro_info_url_all for pro_info_url_all in fd_url ] 
print("fd_url_list",len(fd_url_list))
with open('producthuntdatafile.json', 'r') as f:
    dataone = json.load(f)


# # load the Excel file into a pandas DataFrame
# df = pd.read_excel('filename.xlsx', header=None, names=['strings'])

# # load the JSON file into a list of dictionaries
# with open('filename.json', 'r') as f:
#     dict_list = json.load(f)
for i in range(0,100):
    print()
# add the new key to each dictionary in the list, with the list of strings as its value
for dictionary in dataone:
    dictionary['Website'] = fd_url_list[i]

# write the updated list of dictionaries back to the JSON file
with open('filenamehiiiii.json', 'w') as f:
    json.dump(dataone, f)

    # print("dataone",dataone) 
    # for i in range(0,100):
    #     # print(">>>>>>>>>>>>iiiii",i)
    #     for j in dataone:
    #         # print("???????jjjjj",j)
    #         j["Website"] = fd_url_list[i]
    # print("dataone*******",dataone) 
    # with open('producthuntdatafilechecking.json', 'w') as fout:
    #     json.dump(dataone, fout) 




































   




   


  
 
  
  
 
  
   
   
  
   
   
 
  
   
  
 
   

 
   
   
  
  
  
 
  




































































































































   