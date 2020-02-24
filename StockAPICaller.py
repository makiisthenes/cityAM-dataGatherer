# https://www.alphavantage.co/support/#api-key - API Source
import requests
import json
vantageapikey = '0OL6B1YZZABY32OD'
datatype = 'json'
outputsize = 'full'
interval = '1min'
symbol = 'MSFT'  # tick of company
function = 'TIME_SERIES_INTRADAY'
url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&interval="+interval+"&apikey="+vantageapikey
call =requests.get(url).json()
print(call)
# Now we need to parse this data to be more useful for me, but also look for an trading strategy to use...
# Look at different trading strategies on youtube and look at paper trading, before trading any money...

wtdapikey = 'KaoSKSITuap5ZX2ZgctLPBNNOecyAMz4i2rpaU31oASLJvssn5m3NxnAjThz'
# https://www.worldtradingdata.com/members/home
# Free 25 Intraday Daily Requests...
# https://www.worldtradingdata.com/documentation#stock-and-index-real-time
# This API looks very useful, have a look at it...


# COMPLETELY FREE, UNLIMITED REQ QUANDL
# https://www.quandl.com/tools/python
