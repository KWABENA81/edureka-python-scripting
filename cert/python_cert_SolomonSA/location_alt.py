# Q2: Create a script called location that return the location parameters of any location you want.
#       Providing this alternate solution, since question did not clarify how to solve this.
import argparse
import re
import requests


def loc_search(search_str):
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
            " Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    #sch_str=''.join(search_str)
    url = 'https://maps.google.com?q=' + ''.join(search_str)
    response = requests.get(url, headers=headers).content

    results_list0 = response.decode('utf-8')
    result_str = re.search('staticmap\?center=.*&amp;', results_list0)
    split_list = result_str.group(0).split('=')

    results_list3 = []
    for res in split_list:
        #   convert list to str
        if 'amp;zoom' in res:
            str0 = res.rstrip('&amp;zoom')
            if str0 not in results_list3:
                results_list3.append(str0)

    loc_array = ''.join(results_list3).split('%2C')
    return loc_array


parser = argparse.ArgumentParser(prog='location_alt',
                                 description='Provide the Long & Lat of a given location')
parser.add_argument(dest='input', metavar='\"location item\"', nargs='+',
                    help='the location', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()
    arr_value = loc_search(args.input)

    location_parameter = {'latitude': arr_value[0], 'longitude': arr_value[1]}
    print(arr_value, '\t', location_parameter)




