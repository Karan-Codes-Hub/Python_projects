# Python code to display schematic weather details
import requests
#Sending requests to get the IP Location Information
res = requests.get('https://ipinfo.io/')
# Receiving the response in JSON format
data = res.json()
# Extracting the Location of the City from the response
citydata = data['city']
print("Enter the cityname")
city = input()
# Prints the Current Location

# Passing the City name to the url
url = 'https://wttr.in/{}'.format(city)
# Getting the Weather Data of the City
res = requests.get(url)
# Printing the results!
print(res.text)