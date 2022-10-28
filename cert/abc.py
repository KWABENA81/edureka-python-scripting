from urllib.request import urlopen
import json

# from serpapi import GoogleSearch

# api_key='389a0ed3ce3cc7a86045ef9fb82fc83d65c6da86692bfc1bb32043cdfc8bd53e'

# params = {
#     "q" : "Coffee",
#     "location" : "Austin, Texas, United States",
#     "hl" : "en",
#     "gl" : "us",
#     "google_domain" : "google.com",
#     "api_key" : "demo",
# }

# query = GoogleSearch(params)
# dictionary_results = query.get_dict()
#######################################
# import os, urllib
# from SerpApi import GoogleSearch

# params = {
#   "engine": "google",
#   "q": "Coffee",
#   "api_key": "389a0ed3ce3cc7a86045ef9fb82fc83d65c6da86692bfc1bb32043cdfc8bd53e"
# }

# search = GoogleSearch(params)
# results = search.get_dict()
# organic_results = results["organic_results"]

############################################
# import os, urllib
# from serpapi import GoogleSearch

# params = {
#     "engine": "google",
#     "q": "london",
#     "api_key": os.getenv("API_KEY"),
# }

# search = GoogleSearch(params)
# results = search.get_dict()

# html = results['search_metadata']['raw_html_file']
# print(urllib.request.urlopen(html).read())
################################################################
import requests

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

search_query='Nollywood growing world'

url='https://www.google.com/search?q='+search_query
response = requests.get(url, headers=headers).content
with open("Output.txt", "w") as text_file:
  text_file.write(response.decode('utf-8'))
  text_file.close()



response_nl = response.decode('utf-8').splitlines()
print(response_nl)

#with open("Output1.txt", "w") as text_file:
#text_file.write(response_nl)
# text_file.close()

# with open("Output1.txt", "w") as text_file:
#     text_file.write(response_nl)

# url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'
# response = urlopen(url)

# # Convert bytes to string type and string type to dict
# string = response.read().decode('utf-8')
# json_obj = json.loads(string)

# print(json_obj['source_name'])