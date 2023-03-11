from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables as regular variables
token = os.getenv("ACCESS_TOKEN")
print(token)

# import requests

# # Replace YOUR_API_KEY with your actual API key
# headers = {'Authorization': 'Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s'}

# # Replace product_id with the ID of the product you want to retrieve
# endpoint = 'https://api.producthunt.com/v2/products'
# params = {'search[featured]': True}
# response = requests.get(endpoint, headers=headers, params=params)
# res = requests.get('https://api.producthunt.com/v2/products')
# print("tiiiiiii>>>")
# if res.status_code == 200:
#     data = response.json()
#     product_id = response.json()['id']
#     print(product_id)
# else:
#     # Handle the error here
#     print(f"Error: API returned status code {res.status_code}")

# # Extract the product data from the response

# import requests

# # Set the API endpoint URL
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the GraphQL query string to retrieve the ID of a product by its name
# query = """
# query {
#   product(name: "neeva") {
#     id
#   }
# }
# """

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": "Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s",
#     "Content-Type": "application/json",
# }

# # Send the POST request with the GraphQL query
# response = requests.post(url, headers=headers, json={"query": query})

# # Check if the request was successful
# if response.status_code == 200:
#     # Print the product ID from the response
#     data = response.json()["data"]["product"]
#     print(f"Product ID: {data['id']}")
# else:
#     # Print the error message if the request failed
#     print(f"Request failed with status code {response.status_code}: {response.text}")

# import json
# import requests

# API_URL = "https://api.producthunt.com/v2/api/graphql"

# # Specify your API token
# MY_API_TOKEN = "0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s"

# # Specify your query

# query = {"query":
#         """
#         query todayPosts {
#             posts {
#                 edges {
#                     node {
#                         id
#                         name
#                         tagline
#                         votesCount
#                     }
#                 }
#             }
#         }
#         """}

# query = {"query":
#         """
#        query topProducts(10: Int!) {
#      posts(first: 10, order: VOTES_COUNT_DESC) {
#     edges {
#       node {
#         id
#         name
#         tagline
#         votesCount
#       }
#     }
#   }
# }
#         """}




# headers = {
# 'Accept': 'application/json',
# 'Content-Type': 'application/json',
# 'Authorization': 'Bearer ' + MY_API_TOKEN,
# 'Host': 'api.producthunt.com'
# }

# today_posts = requests.post(API_URL,
# 							headers=headers,
# 							data=json.dumps(query))

# today_posts = today_posts.json()
# print(today_posts)



# import requests

# # Set the API endpoint URL
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the GraphQL query string
# query = """
# query topProductsByMonth($createdAtGte: DateTime!, $createdAtLt: DateTime!) {
#   posts(filter: { createdAtGte: $createdAtGte, createdAtLt: $createdAtLt }, order: RANKINGS_SCORE_DESC) {
#     edges {
#       node {
#         id
#         name
#         tagline
#         votesCount
#         rankingsScore
#       }
#     }
#   }
# }
# """

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": "Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s",
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }

# # Set the query variables
# from datetime import datetime

# start_of_year = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
# print("start_of_year",start_of_year)
# end_of_month = start_of_year.replace(month=2)
# print("end_of_month",end_of_month)
# variables = {
#     "createdAtGte": start_of_year.isoformat(),
#     "createdAtLt": end_of_month.isoformat(),
# }
# print(variables["createdAtGte"],"ISO fORMAT",variables["createdAtLt"])
# # Send the POST request with the GraphQL query and variables
# response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
# print("solllllllllll",response)
# # Check if the request was successful
# if response.status_code == 200:
#     # Get the JSON body of the response
#     response_json = response.json()
#     print("jsonresponse200",response_json)
# #     # Print the product information from the response
# #     for product in response_json["data"]["posts"]["edges"]:
# #         print(f"ID: {product['node']['id']}")
# #         print(f"Name: {product['node']['name']}")
# #         print(f"Tagline: {product['node']['tagline']}")
# #         print(f"Votes Count: {product['node']['votesCount']}")
# #         print(f"Rankings Score: {product['node']['rankingsScore']}")
# #         print()
# # else:
# #     # Print the error message if the request failed
# #     print(f"Request failed with status code {response.status_code}: {response.text}")


# import requests
# from datetime import datetime

# # Set the API endpoint URL
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the GraphQL query string
# query = """
# query topProductsByMonth($createdAtGte: DateTime!, $createdAtLt: DateTime!) {
#   posts(
#     where: {
#       createdAt_gte: $createdAtGte,
#       createdAt_lt: $createdAtLt
#     },
#     orderBy: RANKING
#   ) {
#     edges {
#       node {
#         id
#         name
#         tagline
#         votesCount
#         rankings {
#           daily
#           weekly
#           monthly
#         }
#       }
#     }
#   }
# }
# """

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": "Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s",
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }


# # Set the query variables
# start_of_year = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
# end_of_month = start_of_year.replace(month=2)
# variables = {
#     "createdAtGte": start_of_year.isoformat(),
#     "createdAtLt": end_of_month.isoformat(),
# }

# # Send the POST request with the GraphQL query and variables
# response = requests.post(url, headers=headers, json={"query": query, "variables": variables})

# # Check if the request was successful
# if response.status_code == 200:
#     # Get the JSON body of the response
#     response_json = response.json()
#     print("response_json",response_json)
#     # Print the product information from the response
#     for product in response_json["data"]["posts"]["edges"]:
#         print(f"ID: {product['node']['id']}")
#         print(f"Name: {product['node']['name']}")
#         print(f"Tagline: {product['node']['tagline']}")
#         print(f"Votes Count: {product['node']['votesCount']}")
#         print(f"Rankings: {product['node']['rankings']}")
#         print()
# else:
#     # Print the error message if the request failed
#     print(f"Request failed with status code {response.status_code}: {response.json}")



# # reference code geeks
# # we have imported the requests module
# import requests
# # defined a URL variable that we will be
# # using to send GET or POST requests to the API
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": "Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s",
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }


# body = """
# query getProduct {
#   post(id: "277326") {    
#     id
#     name
#     tagline
#     votesCount
#     website
#   }
# }
# """

# response = requests.post(url=url, headers=headers, json={"query": body})
# print("response status code: ", response.status_code,)
# if response.status_code == 200:
# 	print("response : ", response.json())

# working code
# import requests
# from datetime import datetime

# # Set the API endpoint URL
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the GraphQL query string
# query = """
# query getProduct($id: ID!) {
#   post(id: $id) {
#     id
#     name
#     tagline
#     votesCount
#     website
#     thumbnail {
#       url
#     }
#     commentsCount
   
#     createdAt
#   }
# }
# """

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": "Bearer 0W9LnNaJUnuMZ9a6c4YgLPHVfreEDQFEh1IbltSAQ-s",
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }

# # Set the query variables
# start_of_year = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
# end_of_month = start_of_year.replace(month=2)
# print(start_of_year )
# print(end_of_month )
# start_of_year_epoch = int(start_of_year.timestamp())
# end_of_month_epoch = int(end_of_month.timestamp())
# print("Start of year epoch:", start_of_year_epoch)
# print("End of month epoch:", end_of_month_epoch)

# # Send the POST request with the GraphQL query and variables
# response = requests.post(url, headers=headers, json={
#     "query": query,
#     "variables": {"id": 277328}
# })

# # Check if the request was successful
# if response.status_code == 200:
#     print("200 enter")
#     # Get the JSON body of the response
#     response_json = response.json()
#     print(response_json)
#     # Print the product information from the response
#     # product = response_json["data"]["post"]
#     # print(f"ID: {product['id']}")
#     # print(f"Name: {product['name']}")
#     # print(f"Tagline: {product['tagline']}")
#     # print(f"Votes Count: {product['votesCount']}")
#     # print(f"Product State: {product['productState']}")
#     # print(f"Website: {product['website']}")
#     # print(f"Thumbnail URL: {product['thumbnail']['url']}")
#     # print(f"Comments Count: {product['commentsCount']}")
#     # print(f"Maker Name: {product['maker']['name']}")
#     # print(f"Maker Profile Link: {product['maker']['profileLink']}")
#     # print(f"Created At: {product['createdAt']}")
# else:
#     # Print the error message if the request failed
#     print(f"Request failed with status code {response.status_code}: {response.text}")



# working
# we have imported the requests module
# import requests
# # defined a URL variable that we will be
# # using to send GET or POST requests to the API
# url = "https://api.producthunt.com/v2/api/graphql"

# # Set the authorization header with your API access token
# headers = {
#     "Authorization": f'Bearer {token}',
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }


  


# body = """
# query {
#   collections(first: 10) {
#     edges {
#       node {
#         name
#         description
#       }
#     }
#   }
# }



# """
# body = """
# query { 
#     posts(first: 5) { edges { node { id, name, tagline,votesCount,we
#     bsite  } } }    user {name
#       username} 
   
#       }
# """
# body2 = """
# query getProduct {
#   post(id: "14717") {    
#     id
#     name
#     tagline
#     votesCount
#     website
#         user {
#             id
#             username
#          }
#   }
# }
# """
# body3 = """
#         query myVariable {
#             posts {
#                 totalCount
#                 edges {
#                     node {
#                         id
#                         name
#                         tagline
#                         votesCount
#                         featuredAt
#                          user {
#                             name
#                             username
#                         }
#                         makers {
#                             name
#                             followers {
#                                 totalCount
#                             }
#                             following {
#                                 totalCount
#                             }
#                             madePosts {
#                                 totalCount
#                             }
#                             twitterUsername
#                         }
#                     }
#                 }
#             }
#         }
#         """

# response = requests.post(url=url, headers=headers, json={"query": body2,})
# response2 = requests.post(url=url, headers=headers, json={"query": body2,})
# response3 = requests.post(url=url, headers=headers, json={"query": body3,})
# print("response status code: ", response.status_code)
# if response.status_code == 200:
	# print("response_collect : ", response.json())
	# print("response2 : ", response2.json())
	# print("response3 : ", response3.json())



























# import requests
# from datetime import datetime

# url = 'https://api.producthunt.com/v2/api/graphql'
# query = """
#     query ($createdAtGt: String!, $createdAtLt: String!, $first: Int!) {
#       products(filter: { createdAt: { gt: $createdAtGt, lt: $createdAtLt } }, first: $first) {
#         edges {
#           node {
#             name
#             tagline
#           }
#         }
#       }
#     }
# """

# headers = {
#     "Authorization": f'Bearer {token}',
#     "Content-Type": "application/json",
#     "Accept": "application/json",
#     "Host": "api.producthunt.com"

# }

# current_year = datetime.now().year
# first_month_of_year = datetime(current_year, 1, 1).strftime('%Y-%m-%d')
# print(type(first_month_of_year),first_month_of_year)
# second_month_of_year = datetime(current_year, 2, 1).strftime('%Y-%m-%d')
# print(type(second_month_of_year),second_month_of_year)
# variables = {
#     'createdAtGt': first_month_of_year,
#     'createdAtLt': second_month_of_year,
#     'first': 20
# }

# response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)
# print(response.json())

# if response.status_code == 200:
#     data = response.json()['data']['products']['edges']
#     for product in data:
#         print(product['node']['name'], "-", product['node']['tagline'])
# else:
#     print(f"Error: {response.status_code}")



import requests
from datetime import datetime
import pandas as pd
import json
start_of_year = datetime.today().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
print("start_of_year",start_of_year)
iso_format=start_of_year.isoformat()
print("iso to use",type(iso_format),iso_format)
# Define the GraphQL query
query = """
  {
  posts(order: VOTES, featured_at: "2022-02-01T00:00:00Z") {
    edges {
      node {
        name
        tagline
        featuredAt
      }
    }
  }
}
"""
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
          createdAt
          slug
          makers {
          coverImage
          id 
          name
          websiteUrl
          username
          isMaker
          isViewer
          profileImage
          twitterUsername
          url
          }
          productLinks{
          type
          url
          }
          userId
          name
          tagline
          url
          votesCount
          website
          commentsCount
          description
          user {
          id
          name 
          username
          websiteUrl
          coverImage
          createdAt 
          headline
          isMaker
          isViewer
          profileImage 
          twitterUsername
          url
          }
          featuredAt 
          isCollected
          isVoted
          media {
          videoUrl
          url
          }
          reviewsCount
          reviewsRating
          thumbnail {
          videoUrl
          url
          }
        }
       }
     pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
"""


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
# list  = [["id", "name","tagline", "url", "votesCount"],]
# list1 = []
# list2 = []
# list3 = []
# list4 = []
# list5 = []

# for post in data:
#     print(post)
#     a = {  
#          "id":post["id"],  
#          "name":post["name"],  
#          "tagline":post["tagline"],  
#          "url":post["url"],  
#          "votesCount":post["votesCount"]
#         }
    
#     b = [[a["id"],a["name"],a["tagline"],a["url"],a["votesCount"]]]
#     list.append(b)
#     id_1 = post['node']["id"]
#     name_2=post['node']["name"] 
#     tagline_3=post['node']["tagline"]
#     url_4=post['node']["url"]
#     votesCount_5=post['node']["votesCount"]
#     list1.append(id_1)
#     list2.append(name_2)
#     list3.append(tagline_3)
#     list4.append(url_4)
#     list5.append(votesCount_5)

# df = pd.DataFrame({
#         "Id":list1,
#          "Name":list2,
#        "Tagline":list3,
#          "Url":list4,
#         "Votescount":list5,
       

#                                        })
# df_old = pd.read_excel('ProducthuntProduct.xlsx')
# df_new = pd.concat([df_old,df], ignore_index=True)

# print(df)
# # df.to_excel("ProducthuntProduct.xlsx", index=False)
# df_new.to_excel('ProducthuntProduct.xlsx', index=False)

# print("file written now")



# Process the API response
# if response.status_code == 200:
#     data = response.json()['data']
#     posts = data['posts']['edges']
#     for post in posts:
#         node = post['node']
#         print(f"{node['name']} ({node['tagline']}) - {node['url']} ({node['votesCount']} votes)")
# else:
#     print("Error retrieving data from API")





import requests

# Define the GraphQL query
query = """
  query {
  
      makerGroups(order:NEWEST) {
        edges {
          node {
            id
            name
            description
            url 
            tagline
            membersCount
          }
        }
      }
    
  }
"""



# query = """ 
# query GetMakerGroupAndPost($makerGroupId: ID!) {
#   makerGroup(id: $makerGroupId) {
#     name
    
#   }
# }

# """
# query  = """
# query GetCollectionDetailsWithMakerGroups {
#   collection(id: "376802") {
#     name
#     url
#     posts {
#       edges {
#         node {
#           maker {
#             makerGroups {
#               edges {
#                 node {
#                   name
#                   url
#                 }
#               }
#             }
#           }
#         }
#       }
#     }
#   }
# }
# """










# 376802
# variables  = {
#     "userIds":4339504
# }
# Define the API endpoint
endpoint = "https://api.producthunt.com/v2/api/graphql"

# Define the API headers
headers = {
    "Authorization": f'Bearer {token}',
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Host": "api.producthunt.com"

}

# Make the API request
response = requests.post(endpoint, json={"query": query}, headers=headers)

# Extract the data from the response
data = response.json()
print("***********",data)
# # ["data"]["viewer"]["makerGroups"]["edges"]
# # Print the results
# for edge in data:
#     node = edge["node"]
#     # print(f"MakerGroup ID: {node['id']}")
#     # print(f"MakerGroup Name: {node['name']}")
#     print()


