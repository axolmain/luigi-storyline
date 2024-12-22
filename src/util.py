import math


def haversine(location1, location2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)

    note: I know using an object here is gross
    """
    R = 6371  # Radius of the earth in km

    dlat = math.radians(location2.latitude - location1.latitude)
    dlon = math.radians(location2.longitude - location1.longitude)
    a = math.sin(dlat / 2) ** 2 + math.cos(math.radians(location1.latitude)) * math.cos(math.radians(location2.latitude)) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return abs(distance)


class location():
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
