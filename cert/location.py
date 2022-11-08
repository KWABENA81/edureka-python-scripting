# Q2: Create a script called location that return the location parameters of any location you want.
import argparse

from geopy import Nominatim

parameters = ['lat', 'lon', 'display_name', 'osm_id', 'place_id']
parameter_dict = {}


def location_search(loc):
    app = Nominatim(user_agent="kwabena81@yahoo.com")
    try:
        location_dict = app.geocode(loc).raw
        for ky in location_dict:
            if ky in parameters:
                parameter_dict[ky] = location_dict[ky]

    except:
        print('ERROR:  Input may be invalid')


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
