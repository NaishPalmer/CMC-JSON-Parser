'''
This is a JSON Parser made to read CoinMarketCap API Information such as Cryptocurrency Prices and Volume.
'''

import urllib.request, json

with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/1/") as url:
    requestedinfo = json.loads(url.read().decode())
    print(requestedinfo['data']['id'],requestedinfo['data']['name'], requestedinfo['data']['symbol'], requestedinfo['data']['quotes']['USD']['price'])
     