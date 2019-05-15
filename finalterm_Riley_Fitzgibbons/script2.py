'''
Does nothing but get a list of all cities and their json results. This works correctly.
'''
def main():
	# Import packages that are needed.
	import json
	import requests

	# Load file to be written to.
	city_url_file = open("data.txt", "w+")

	# Load json for all cities
	citys_json = requests.get('https://api.teleport.org/api/urban_areas/')
	city_url_file.write(json.dumps(citys_json.text))

	# Close file.
	city_url_file.close()

if __name__=="__main__":
	main()