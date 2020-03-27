from googleplaces import GooglePlaces
from opencage.geocoder import OpenCageGeocode
import requests
import geocoder

def get_ip():
    """  Function To Get GeoIP Latitude & Longitude """
    g = geocoder.ip('me')
    return g.latlng

def get_coord(place, key):
    geocoder = OpenCageGeocode(key)
    results = geocoder.geocode(place)
    lat = results[0]['geometry']['lat']
    long = results[0]['geometry']['lng']
    return "{},{}".format(lat,long)

if __name__ == '__main__':
    key = "e1871292624242709b817e84e497c0a2"
    api = GooglePlaces("AIzaSyBAz46CIw4xbtbgx2aOw7RTu04D2tfVymM")
    keyword = "veterinarian"
    place = "Durham, NC"
    query = "{} near {}".format(keyword, place)
    location = get_coord(place, key)
    fields = ['name','formatted_address', 'international_phone_number', 'opening_hours']
    radius = 50000
   # places = api.search_places_by_keyword(query, location, fields)
   # places2 = api.search_places_by_coordinate(location, radius, keyword)
    places3 = api.search_places_by_coordinate_rank(location, keyword)
    #print(places)
    for place in places3:
        details = api.get_place_details(place['place_id'], fields)
        try:
            name = details['result']['name']
        except KeyError:
            name = ""
        try:
            address = details['result']['formatted_address']
        except KeyError:
            address = ""
        try:
            phone = details['result']['international_phone_number']
        except KeyError:
            phone = ""
        '''
        try:
            hours = details['result']['opening_hours']
        except KeyError:
            hours = ""
        '''
        print("Name:", name)
        print("Address:", address)
        print("Phone:", phone)
        #print("Hours:", hours)
