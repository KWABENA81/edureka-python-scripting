import re
import requests

headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

search_query = 'canada'
url = 'https://www.google.com/search?q=' + search_query
response = requests.get(url, headers=headers).content
with open("Output.txt", "w") as text_file:
    text_file.write(response.decode('utf-8'))
    text_file.close()

max_hits = 15
regex0 = r'<h3 class='
regex1 = r'<h3 class=.*</h3'
regex2 = r'<h3 class=\".*\">.+</h3>'
regex3 = r'<div class=".*</div></h3>'
regex4 = r'<div class=".*><div class=".*</div></h3></div>'
pattern5 = r'<div class=.*</div>'
regex6 = r'(<div class=".+><h3 class=".+><div class=").+(</div></h3></div>)'
regex7 = r'</div><div class='
regex8 = r'</div>'
regex9 = r'<a href=\".*</a>'
p_list = re.split(r'<h3 class=', response.decode('utf-8'))

plist0 = []
plist1 = []
plist2 = []
plist3 = []

for x in p_list:
    if search_query.upper() in x.upper() and '</h3' in x:
        plist0.append(x)
1
for sublink in plist0:
    sub_list = re.split(r"</h3></div>", sublink)
    plist1.append(sub_list)

count = 0
for lst in plist1:
    if count < max_hits:
        #   convert list to str
        lst_str = ' '.join(lst)
        find_str = re.findall(r'(<div class=.*/div>)', lst_str)
        plist2.append(find_str)
        count += 1
    else:
        break
#<div class=".">
############################################################
for x in range(len(plist2)):
    wd=''.join(plist2[x])

    nword = re.sub(r'^(<div class="BNeawe vvjwJb AP7Wnd UwRFLe" style="-webkit-line-clamp:2">)', '', wd, count=1)
    print(x, '\t', nword)

   #nword=re.sub(r'(<div class=\".*\">)^','||',wd)
    # rr = wd.lstrip('<div class=.*>')
    #print('wd--\t',wd)
    #nword = re.sub('<div class=.*>', '||', wd, count=1)
    #nword = re.sub(r'^(<div class=.*\">)', '|88|', wd, count=1)
# ltr='<div class="BNeawe vvjwJb AP7Wnd UwRFLe" style="-webkit-line-clamp:2">Nollywood - Wikipedia</div></h3>kljljljljl'
# print( '\nltr\t', re.sub(r'^(<div class="BNeawe vvjwJb AP7Wnd UwRFLe" style="-webkit-line-clamp:2">)', '|===|', ltr, count=1))




# str = ''.join(map(str,plist3))              #(<div class=){1}\.*(/div>){1}
# strn=re.findall(r'(<div class=.*/div>){1}', str)
# #strn=re.findall(r'<div class=*/div>',str)
# print('\njfjdlsdls\n\n',len(strn))


# ppp = response.decode('utf-8').split(regex7)

# plist0=[]
#
# for x in ppp:
#   ystr = re.findall(ptn5,x)
#   if len( ystr) > 0:
#     plist0.append(ystr)
#     print('\n',plist0,'\n')
# #print(indeces)
#
# # p_list = re.findall(ptn2, response.decode('utf-8').split(p2))
# print('\n',len(plist0))

# print('\n\n\n\n', response)

# p = re.match(regex1)
# response_nl = response.decode('utf-8').splitlines(regex1,1)
# print(response.decode('utf-8'))

# regex0='^<h2 class=.*</h$'
# #regex1='value=.*' #'^<h2 class=.*/h2'
# p = re.match(regex1)
# print(p.findall(response.decode('utf-8')))


# with open("Output1.txt", "w") as text_file:
# text_file.write(response_nl)
# text_file.close()
# with open("Output1.txt", "w") as text_file:
#     text_file.write(p_list)

# url = 'http://www.quandl.com/api/v1/datasets/FRED/GDP.json'
# response = urlopen(url)

# # Convert bytes to string type and string type to dict
# string = response.read().decode('utf-8')
# json_obj = json.loads(string)

# print(json_obj['source_name'])
