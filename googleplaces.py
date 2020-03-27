import requests
import json
import time
 
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
 