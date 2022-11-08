# Q1:   Create a python script called googlesearch that provides a command line utility
#       to perform google search. It gives you the top links (search results) of whatever
#       you want to search on google.

import re
import requests


def search(search_query):
    search_string = ''
    for res in search_query:
        res = ''.join(res)
        search_string += res + ' '
    search_string.rstrip()

    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    url = 'https://www.google.com/search?q=' + search_string
    response = requests.get(url, headers=headers).content
    with open("temp.txt", "w") as text_file:
        text_file.write(response.decode('utf-8'))
        text_file.close()

    results_list0 = re.split(r'<h3 class=', response.decode('utf-8'))

    results_list1 = []
    for x in results_list0:
        if '</h3' in x:
            results_list1.append(x)

    results_list2 = []
    for res in results_list1:
        sub_list = re.split(r"</h3></div>", res)
        results_list2.append(sub_list)

    count = 0
    results_list3 = []
    max_hits = 15
    for res in results_list2:
        if count < max_hits:
            #   convert list to str
            res_str = ' '.join(res)
            find_str = re.findall(r'(<div class=.*/div>)', res_str)
            results_list3.append(find_str)
            count += 1
        else:
            break

    results_list4 = []
    rpattern = r'^(<div class="BNeawe vvjwJb AP7Wnd UwRFLe" style="-webkit-line-clamp:2">)'
    for x in range(len(results_list3)):
        wd = ''.join(results_list3[x])
        nword = re.sub(rpattern, '', wd, count=1)

        word = re.sub(r'(</div>.*)$', '', nword)
        if re.search(r'(<|>|#)', word):
            continue
        else:
            results_list4.append(word)
    return results_list4
