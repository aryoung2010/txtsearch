import requests
import json
import requests
from opencage.geocoder import OpenCageGeocode

#import time
 
class GooglePlaces(object):
    def __init__(self, apiKey):
        super(GooglePlaces, self).__init__()
        self.apiKey = apiKey

    def search_places_by_coordinate_rank(self, location, keyword):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'rankby': 'distance',
            'keyword': keyword,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        return places

    def search_places_by_coordinate(self, location, radius, keyword):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        places = []
        params = {
            'location': location,
            'radius': radius,
            'keyword': keyword,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        '''
        time.sleep(2)
        while "next_page_token" in results:
            params['pagetoken'] = results['next_page_token'],
            res = requests.get(endpoint_url, params = params)
            results = json.loads(res.content)
            places.extend(results['results'])
            time.sleep(2)
        '''
        return places

    def search_places_by_keyword(self, query, location, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        places = []
        params = {
            'input': query,
            'inputtype': 'textquery',
            'locationbias': location,
            'fields': fields,
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params=params)
        print(res)
        results = json.loads(res.content)
        print(results)
        places.extend(results['candidates'])
        return places

    def get_place_details(self, place_id, fields):
        endpoint_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'placeid': place_id,
            'fields': ",".join(fields),
            'key': self.apiKey
        }
        res = requests.get(endpoint_url, params = params)
        place_details = json.loads(res.content)
        return place_details


def get_coord(place, key):
    #print(f"place {place} key {key}")
    geocoder = OpenCageGeocode(key)
    results = geocoder.geocode(place)
    latc = results[0]['geometry']['lat']
    longc = results[0]['geometry']['lng']
    locale = "{},{}".format(latc,longc)
    #print(f"locale {locale}")
    return locale


def thingnearplace(request,KEY):
    """Takes JSON Payload {"thing": "veterinarian" , "place": "Durham, NC"}
    """
    request_json = request.get_json()
    #print(f"request_json {request_json}")
    thing = request_json['thing']
    place = request_json['place']
    #print(f"my key {KEY}")
    location = get_coord(place, KEY)
    return location

def getinfolist(request):
    request_json = request.get_json()
    thing = request_json['thing']
    place = request_json['place']
    KEY = 'e1871292624242709b817e84e497c0a2'
    api = GooglePlaces("AIzaSyBAz46CIw4xbtbgx2aOw7RTu04D2tfVymM")
    query = "{} near {}".format(thing, place)
    location = get_coord(place,KEY)
    fields = ['name','formatted_address', 'international_phone_number', 'opening_hours']
    radius = 50000
   # places = api.search_places_by_keyword(query, location, fields)
   # places2 = api.search_places_by_coordinate(location, radius, keyword)
    places3 = api.search_places_by_coordinate_rank(location, thing)
    #print(places)
    i=0
    closest ={} 
    for place in places3:
        i += 1
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
        closest[i] = {"name" : name , "address" : address , "phone" : phone}

        #print("Name:", name)
        #print("Address:", address)
        #print("Phone:", phone)
        #print("Hours:", hours)
    return closest
