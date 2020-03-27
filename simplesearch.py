import requests

api_key = "AIzaSyBAz46CIw4xbtbgx2aOw7RTu04D2tfVymM"

# url variable store url 
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
# The text string on which to search 
search = "veterinary"
place = "Durham, NC"
query = input("{} near {}".format(search, place)) 
  
# get method of requests module 
# return response object 
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
  
# json method of response object convert 
#  json format data into python format data 
x = r.json() 
  
# now x contains list of nested dictionaries 
# we know dictionary contain key value pair 
# store the value of result key in variable y 
y = x['results'] 
  
# keep looping upto length of y 
for i in range(10): 
      
    # Print value corresponding to the 
    # 'name' key at the ith index of y 
    print(y[i]['name']) 
