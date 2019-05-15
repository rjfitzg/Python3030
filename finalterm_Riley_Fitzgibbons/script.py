'''
Send run.py a city name and get returned a url of an image of the requested city.
This script then writes that url to a json file

I started this wrong and completed it before being told my mistake.
It may not be the intended way but it still worked and did it in less than 1 second for 10 cities.
'''

def main():
	# Import packages that are needed.
	import json
	import run

	# Load a list of cities
	citys = ['Barcelona', 'London', 'berlin', 
			'paris', 'seattle', 'dubai',
			'new york', 'shanghai', 'Rome', 'Toronto']

	# Load file to be written to.
	city_url_file = open("data.txt", "w+")

	# Set data
	data = {}

	# Get image url for every city and write to file.
	for city in citys:
		city_url = run.get_city_image_url(city)
		data[city] = city_url


	# Generate json and write to file
	city_json = json.dumps(data)
	city_url_file.write(city_json)


	# Close file.
	city_url_file.close()

if __name__=="__main__":
	main()