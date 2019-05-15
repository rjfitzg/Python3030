'''
Almost completed but couldn't get the file to load as a json object in time after completing the other scripts.
'''
def get_city_image_url(city):
	import requests
	import json
	
	# Normalize request and make call to api
	city = city.lower()
	city = city.replace(" ", "-") # turn spaces into '-' as is wanted by the api

	# Load and filter json file
	# Filter out json
	city_url_file = open("data.txt", "w+")

	# Load json to a variable from the file name
	file_json = ...
	for i in range(0,file_json['_links']['ua:item'][i]):
		if file_json['_links']['ua:item'][i]['name'] == city:
			# Load url from href and remove the url that you want
			req = requests.get(file_json['_links']['ua:item'][i]['href'])
			text = json.loads(req.text)
			photo_url = text['photos'][0]['attribution']['source']

	return photo_url



###
cities = ['Barcelona', 'London', 'berlin', 
			'paris', 'seattle', 'dubai',
			'new york', 'shanghai', 'Rome', 'Toronto']

for city in cities:
	city_url = get_city_image_url(city)