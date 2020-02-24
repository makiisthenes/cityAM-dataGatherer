# https://www.alphavantage.co/support/#api-key - API Source
import requests
import json
apikey = '0OL6B1YZZABY32OD'
datatype = 'json'
outputsize = 'full'
interval = '1min'
symbol = 'MSFT'  # tick of company
function = 'TIME_SERIES_INTRADAY'
url = "https://www.alphavantage.co/query?function="+function+"&symbol="+symbol+"&interval="+interval+"&apikey="+apikey
call =requests.get(url).json()
print(call)