def parse_location(location):
    if location is None or location == 0:
        return 0, 0
    location_values = location.split(",")
    latitude = location_values[0]
    longitude = location_values[1]
    return latitude, longitude
