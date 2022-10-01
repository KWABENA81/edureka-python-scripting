import math


def distance_between(locA, locB):
    diffLon = locB[1] - locA[1]
    diffLat = locB[0] - locA[0]

    a = math.pow(math.sin(diffLat / 2), 2)
    b = math.cos(locB[0])
    c = math.cos(locA[0])
    d = math.pow(math.sin(diffLon / 2), 2)

    result1 = a + b * c * d
    print('distance_between result1 : ', result1)
    result2 = 6373.0 * (2 * math.atan2(math.sqrt(result1), math.sqrt(1 - result1)))
    print('distance_between result2 : ', result2)
    # print('distance_between 1: ', locB[1] - locA[1] )


# print('distance_between 2: ', lng[1]-lng[0])


vancouver = (49.2827, -123.1207)
montreal = (45.5019, -73.5674)
calgary = (51.0447, -114.0719)
toronto = (43.6532, -79.3832)
distance_between(toronto, vancouver)
