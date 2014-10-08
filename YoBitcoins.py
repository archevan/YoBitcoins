#
#Author: Evan Seils
#
#Version: 1.0
#
#Please excuse any bugs that you find!
#

import requests
import time
import apikey

while True:
	t = requests.get('http://blockchain.info/stats?format=json') #First request for blockchain data
	jdatathen = t.json() #Read the returned data and assign it to a variable
	then = jdatathen['market_price_usd'] #Grab market price at the time
	time.sleep(1800) #30 Minute Delay
	n = requests.get('http://blockchain.info/stats?format=json') #Make a second request for current information
	jdatanow = n.json() 
	now = jdatanow['market_price_usd'] #Grab current market price
	if then-now >=100 or then-now <= -100: #Check for price difference
		print "Difference Greater Than $100 Detected.... Yoing all Subscribers!"
		yoall()

def yoall(): #Send YO!
	request.post('https://api.justyo.co/yoall/', data={'api_token': apikey.api_token,'link': 'http://blockchain.info/charts/market-price'})
	
