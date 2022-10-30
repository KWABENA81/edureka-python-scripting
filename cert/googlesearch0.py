import re
from urllib.request import urlopen
import json

import requests

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

search_query='Nollywood'

url='https://www.google.com/search?q='+search_query
response = requests.get(url, headers=headers).content
with open("Output.txt", "w") as text_file:
  text_file.write(response.decode('utf-8'))
  text_file.close()

regex1='<h3 class=.*</h3'    # '<h3 class=.*</h3$'
ptn=r'<h3 class=\".*\">.+</h3>'
ptn0=r'<div class=".*</div></h3>'
ptn1=r'<div class=".*><div class=".*</div></h3></div>'
ptn2=r'(<div class=".*>){1}<h3 class=".*</div></h3></div>'
ptn3=r'(<div class=".+><h3 class=".+><div class=").+(</div></h3></div>)'
p_list = re.findall(ptn3, response.decode('utf-8'))

plist0=[]
plist1=[]

for x in p_list:
  ptn=r'<a href=".*</a>'
  ystr = re.findall(ptn,x)
  #if search_query in ystr:
  plist0.append(ystr)
  print(ystr)

# for y in plist0:
#     ys=re.split(r"</h3></div>",y) 
#     plist1.append(ys)
      
#     count=0ptn,x)
# for yy in plist1:
#   count+=1
#   print(count,'\n',yy,'\n\n')
#   if count >=10:
#     break

#print(p_list0)
  
#print(p.findall(response.decode('utf-8')))


#p = re.match(regex1)
#response_nl = response.decode('utf-8').splitlines(regex1,1)
# print(response.decode('utf-8'))

# regex0='^<h2 class=.*</h$'
# #regex1='value=.*' #'^<h2 class=.*/h2'
# p = re.match(regex1)
# print(p.findall(response.decode('utf-8')))


#with open("Output1.txt", "w") as text_file:
#text_file.write(response_nl)
# text_file.close()
# with open("Output1.txt", "w") as text_file:
#     text_file.write(p_list)

# url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'
# response = urlopen(url)

# # Convert bytes to string type and string type to dict
# string = response.read().decode('utf-8')
# json_obj = json.loads(string)

# print(json_obj['source_name'])