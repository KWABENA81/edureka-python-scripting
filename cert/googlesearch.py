import re
import requests


def search_google(search_query):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    # search_query = ''.join(search_query)  # 'nollywood'
    url = 'https://www.google.com/search?q=' +  search_query
    response = requests.get(url, headers=headers).content
    with open("Output.txt", "w") as text_file:
        text_file.write(response.decode('utf-8'))
        text_file.close()

    p_list = re.split(r'<h3 class=', response.decode('utf-8'))

    p_list0 = []
    for x in p_list:
        if search_query.upper() in x.upper() and '</h3' in x:
            p_list0.append(x)

    p_list1 = []
    for sublink in p_list0:
        sub_list = re.split(r"</h3></div>", sublink)
        p_list1.append(sub_list)

    count = 0
    p_list2 = []
    max_hits = 15
    for lst in p_list1:
        if count < max_hits:
            #   convert list to str
            lst_str = ' '.join(lst)
            find_str = re.findall(r'(<div class=.*/div>)', lst_str)
            p_list2.append(find_str)
            count += 1
        else:
            break

    p_list3 = []
    for x in range(len(p_list2)):
        wd = ''.join(p_list2[x])

        nword = re.sub(r'^(<div class="BNeawe vvjwJb AP7Wnd UwRFLe" style="-webkit-line-clamp:2">)', '', wd, count=1)

        word = re.sub(r'(</div>.*)$', '', nword)
        if re.search(r'(<|>|#)', word):
            continue
        else:
            # p_list3.append(word)
            print(word)
    # return p_list3
