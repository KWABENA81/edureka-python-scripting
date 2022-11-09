#    Q3: Create a script called weather that return the environmental parameters
#    (temperature (min, max), windspeed, humidity, cloud, pressure, sunrise and sunset)
#    of any location you want; after passing arguments (like user api and city id).
import argparse
import json
import re
from subprocess import run

import requests

parameter_dict = {'cloud': '', 'windspeed': '', 'sys': '', 'temperature (min, max) ,humidity, pressure': ''}
os_lst = ['N', 'W', 'R']
wfile = 'weather_out.txt'


def weather_out(loc, weather_api_key):
    lat = loc[0]
    lon = loc[1]
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=metric/' \
          % (lat, lon, weather_api_key)
    response = requests.get(url)
    if response.ok:
        data = json.loads(response.text)
        parameter_dict['temperature (min, max) ,humidity, pressure'] = data['main']
        parameter_dict['windspeed'] = data['wind']
        parameter_dict['cloud'] = data['clouds']
        parameter_dict['sys'] = data['sys']
    else:
        print('Backend weather service not available')


parser = argparse.ArgumentParser(
    prog='weather', description='Provide the parameters of a city')
parser.add_argument('-d', '--city_id', dest='cityid', required=True, help='the city OSM Id', type=str)
parser.add_argument('-k', '--api_key', dest='apikey', required=True, help='the api key', type=str)
args = parser.parse_args()


def read_weather_out(apkey):
    with open(wfile) as f:
        wlines = f.readlines()
        f.close()
        lat = 0
        lon = 0
        result_str = re.search(r'coordinates\":\[.*\]', ''.join(wlines))
        split_list = result_str.group(0).split('},')
        for v in split_list:
            if v.startswith('coordinates'):
                v1 = v.lstrip('coordinates":[')
                v2 = v1.rstrip(']')
                v3 = v2.split(',')

                for y in range(len(v3)):
                    lon = v3[0]
                    lat = v3[1]

    weather_out([lat, lon], apkey)


def locationsearch(cid, apkey):
    oosm_type = ['W', 'N', 'R']
    for typ in oosm_type:
        xy2 = run(
            'curl \"https://nominatim.openstreetmap.org/details?osmtype=' \
            + ''.join(typ) + '&osmid=' + ''.join(cid) + \
            '&format=json\" 2>/dev/null 1> ' + wfile, shell=True)

    read_weather_out(apkey)


if __name__ == '__main__':
    args = parser.parse_args()
    locationsearch(args.cityid, args.apikey)
    for key in parameter_dict:
        print(key.upper(), '\n\t-->', parameter_dict[key])
