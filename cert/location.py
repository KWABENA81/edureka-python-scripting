# Q2: Create a script called location that return the location parameters of any location you want.

from geopy import Nominatim


def location_search(loc):
    app = Nominatim(user_agent="python_coding")
    try:
        location = app.geocode(loc).raw
        print(location)
    except:
        print('ERROR')


if __name__ == '__main__':
    loc_search = 'accra,ghana'
    location_search(loc_search)
