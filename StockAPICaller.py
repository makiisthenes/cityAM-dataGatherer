# https://www.alphavantage.co/support/#api-key - API Source
import requests
import json
# ----------------------------------------------------------------------------------------------------------------------
vantageapikey = '0OL6B1YZZABY32OD'
datatype = 'json'
outputsize = 'full'
interval = '1min'
symbol = 'MSFT'  # tick of company 'symbol'
function = 'TIME_SERIES_INTRADAY'
url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&interval="+interval+"&apikey="+vantageapikey
call = requests.get(url).json()
print(call)
# ----------------------------------------------------------------------------------------------------------------------
wtdapikey = 'KaoSKSITuap5ZX2ZgctLPBNNOecyAMz4i2rpaU31oASLJvssn5m3NxnAjThz'
requests.get('https://www.worldtradingdata.com/members/home')
# Free 25 Intraday Daily Requests...
requests.get('https://www.worldtradingdata.com/documentation#stock-and-index-real-time')
# This API looks very useful, have a look at it...
# ----------------------------------------------------------------------------------------------------------------------
# COMPLETELY FREE, UNLIMITED REQ QUANDL
requests.get('https://www.quandl.com/tools/python')
# Look at API Documentation.
