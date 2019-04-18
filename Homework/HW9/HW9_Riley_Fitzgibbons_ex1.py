'''
Homework 9 exercise 1
Riley Fitzgibbons 
04.14/19
An API call to OpenWeather at 7am. If rain is expected, send and email reminding user to bring umbrella.
'''


# Functions go here.
'''
Sends email to remind user to bring an umbrella for rain.
'''
def send_email():
	# Import libaries
	import smtplib
	myEm = smtplib.SMTP('smtp-mail.outlook.com', 587)

	print('Sending email..')
	
	email = input("email: ")
	password = input("password: ")

	# Check for response.
	if not (myEm.ehlo()[0] == 250):
		print('There was an error contacting the smtp server')
		import sys; sys.exit()	# Quit.
	
	# Login
	myEm.starttls()
	myEm.login(email, password)

	message = 'Subject: Bring an umbrella! \n\nPlease bring an umbrella'

	# Send email
	myEm.sendmail(email, email, message)
	myEm.quit()
	print('Email Sent..')



def obtain_weather(api_key, cityID):
	# Import necesary packages
	import requests
	import json

	# Set up and make API call.
	api_OpenWeather = 'http://api.openweathermap.org/data/2.5/forecast?id='
	url = api_OpenWeather + cityID + '&units=imperial&APPID=' + api_key
	response = requests.get(url)

	# If no response, quit.
	if response is None:
		print('Sorry reponse gathered. Exiting..')
		import sys; sys.exit()

	# Load Json to variable.
	data = json.loads(response.text)

	# Get main forecast
	current_weather = data['list'][0]['weather'][0]['main']
	return current_weather


# Main function.
def main():
	# Import the neded packages.
	import datetime as dt
	import time
	
	# Test if curent time is past 7am, if not, wait.
	now = dt.datetime.now()
	while (int(now.strftime("%H")) > 7):
		time.sleep(10)
		now = dt.datetime.now() # Refresh the time.

	# Set variables
	apiKey = open('Util/apiKey.txt', 'r') # need to set you own apiKey
	cityID = '5417598' # For Colorado Springs
	

	# If rain is expected, send email warning. 
	if (obtain_weather(api_key, cityID) == 'rain'):
		# Send email
		send_email()

	print("Done")

if __name__=="__main__":
	main()
