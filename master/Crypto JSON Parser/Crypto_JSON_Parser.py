'''
This is a JSON Parser made to read CoinMarketCap API Information such as Cryptocurrency Prices and Volume.
'''

import urllib.request, json

def bitcoin():

    with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/1/") as url:
        information = json.loads(url.read().decode())
        name = (information['data']['name'])
        symbol = (information['data']['symbol'])
        price = (information['data']['quotes']['USD']['price'])
        market_cap = (str(information['data']['quotes']['USD']['market_cap']))
        print('Name = ' + name + '\nSymbol =  ' + symbol + '\nPrice = ' + str(price) + '\nMarket Cap =  ' + str(market_cap))


bitcoin()
