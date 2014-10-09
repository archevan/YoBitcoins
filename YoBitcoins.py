#
#
# Author: Evan Seils
#
# Version: 3.0
#
#

import time
import apikey
import requests

initial = 0
x = True

#Get initial market value in United States Dollars
def getvalue(): 
	global initial
	t = requests.get('https://blockchain.info/stats?format=json') 
	jdatathen = t.json()
	initial = jdatathen['market_price_usd']
	print "First value request server response:"
	print t # Print HTTP status code
	print "Market Value in U.S. dollars" + initial

getvalue()
global initial

def yo_all():
	requests.post('http://api.justyo.co/yoall', data={'api_token': apikey.api_token,'link': 'https://blockchain.info/charts/market-price'}) # Send Yo to all
	print "YO Sent"

# Do while in Python
while x == True:
	time.sleep(3600) # One Hour
	n = requests.get('https://blockchain.info/stats?format=json')
	jdatanow = n.json()
	now = jdatanow['market_price_usd']
	if initial - now <= -100 or initial - now >= 100:
		yo_all()
		getvalue()
	
