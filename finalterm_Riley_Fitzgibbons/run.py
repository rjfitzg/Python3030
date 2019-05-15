def get_city_image_url(city):
	import requests
	import json
	
	# Normalize request and make call to api
	city = city.lower()
	city = city.replace(" ", "-") # turn spaces into '-' as is wanted by the api
	api_url = 'https://api.teleport.org/api/urban_areas/slug:'
	req_url = api_url + city + '/images'
	req = requests.get(req_url)

	# If the api call was unsuccessful, return empty.
	if not (req.status_code == requests.codes.ok):
		return ""

	# Seperate the url that is wanted out of the rest of the json.
	text = json.loads(req.text)
	photo_url = text['photos'][0]['attribution']['source']

	return photo_url