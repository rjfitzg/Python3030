'''
Homework 9 exercise 1
Riley Fitzgibbons 
04.14/19
An API call to OpenWeather at 0730. If rain is expected, send and email reminding user to bring umbrella.
'''
# Functions go here.


# Main function.
def main():
	# Import the neded packages.
	import datetime as dt
	import time
	
	# Test if curent time is past 7am, if not, wait.
	# Commented out to undergo testing.
	now = dt.datetime.now()
	'''
	while (int(now.strftime("%H")) > 7):
		time.sleep(10)
		now = dt.datetime.now() # Refresh the time.
	'''


# Import necesary packages
import requests
import json

# Set variables
#apiKey = open('Util/apiKey.txt', 'r') # need to set you own apiKey
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
	
	print("Done")

if __name__=="__main__":
	main()
