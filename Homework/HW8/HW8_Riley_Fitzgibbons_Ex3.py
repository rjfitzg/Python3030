'''
Homework8 Exercixe 3
Riley Fitzgibbons

Use openweathermap API to get forecast
'''

# Import necesary packages
import requests
import json

# Set variables
apiKey = open('Util/apiKey.txt', 'r') # need to set you own apiKey
cityID = '5417598' # For Colorado Springs
api_OpenWeather = 'http://api.openweathermap.org/data/2.5/forecast?id='
url = api_OpenWeather + cityID + '&units=imperial&APPID=' + apiKey

# Make API call
response = requests.get(url)

# If no response, quit
if response is None:
	import sys; sys.exit()

# Extract data from json format.
data = json.loads(response.text)
temps = ['temp', 'temp_min', 'temp_max']
OW_Forecast = []
for day in range(0,3):
	for temp in temps:
		OW_Forecast.append(data['list'][day]['main'][temp])

print('Today:\navg: %s \nmin: %s \nmax: %s' % (OW_Forecast[0], OW_Forecast[1],OW_Forecast[2]))
print('Tomorrow:\navg: %s \nmin: %s \nmax: %s' % (OW_Forecast[3], OW_Forecast[4],OW_Forecast[5]))
print('Tomorrow\'s Tomorrow:\navg: %s \nmin: %s \nmax: %s' % (OW_Forecast[6], OW_Forecast[7],OW_Forecast[8]))
