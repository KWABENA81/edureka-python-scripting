#    Q3: Create a script called weather that return the environmental parameters
#    (temperature (min, max), windspeed, humidity, cloud, pressure, sunrise and sunset)
#    of any location you want; after passing arguments (like user api and city id).
import argparse
import json

import requests
from geopy import Nominatim

parameters = ['temperature (min, max)', 'windspeed', 'humidity', 'cloud', 'pressure', 'sunrise' ,'sunset']
parameter_dict = {}
os_lst=['N', 'W', 'R']
weather_api_key = 'a006c9c582dde2994f646473fb0efcc5'

def weather_out(loc):
    lat = loc[0]
    lon = loc[1]
    print(lat, '  ', lon)
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=metric/'\
          % (lat, lon, weather_api_key)
    response = requests.get(url)
    print(url)
    if response.ok:
        data = json.loads(response.text)
        print(data)
    else:
        print('Backend weather service not available')



parser = argparse.ArgumentParser(prog='location',
                                 description='Provide the parameters of a given location')
parser.add_argument(dest='input', metavar='\"location item\"', nargs='+',
                    help='the location', type=str)
args = parser.parse_args()

if __name__ == '__main__':
    args = parser.parse_args()
    location_search(args.input)
    for key in parameter_dict:
        print(key, ':-->', parameter_dict[key])


#    curl "https://nominatim.openstreetmap.org/details?osmtype=R&osmid=175905&format=json"