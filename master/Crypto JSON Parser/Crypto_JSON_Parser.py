'''
This is a JSON Parser made to read CoinMarketCap API Information such as Cryptocurrency Prices and Volume.
'''

import urllib.request, json

USD = 'USD'
GBP = 'GBP'
JPY = 'JPY'
EUR = 'EUR'

def bitcoin_information():

    with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/1/") as url:
        information = json.loads(url.read().decode())
        name = (information['data']['name'])
        symbol = (information['data']['symbol'])
        price = (information['data']['quotes']['USD']['price'])
        market_cap = ((str(round(information['data']['quotes']['USD']['market_cap'])).rstrip('0').rstrip('.')) + ' ' + USD)
        print('=' * 20)
        print('Coin Name = ' + name + '\nSymbol =  ' + symbol + '\nPrice = ' + str(price) + '\nMarket Cap =  ' + str(market_cap))
        print('=' * 20)

def ethereum_information():
    with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/1027/") as url:
        information = json.loads(url.read().decode())
        name = (information['data']['name'])
        symbol = (information['data']['symbol'])
        price = (information['data']['quotes']['USD']['price'])
        market_cap = ((str(round(information['data']['quotes']['USD']['market_cap'])).rstrip('0').rstrip('.')) + ' ' + USD)
        print('=' * 20)
        print('Coin Name = ' + name + '\nSymbol =  ' + symbol + '\nPrice = ' + str(price) + '\nMarket Cap =  ' + str(market_cap))
        print('=' * 20)


def chainlink_information():
    with urllib.request.urlopen("https://api.coinmarketcap.com/v2/ticker/1975/") as url:
        information = json.loads(url.read().decode())
        name = (information['data']['name'])
        symbol = (information['data']['symbol'])
        price = (information['data']['quotes']['USD']['price'])
        market_cap = ((str(round(information['data']['quotes']['USD']['market_cap'])).rstrip('0').rstrip('.')) + ' ' + USD)
        print('=' * 20)
        print('Coin Name = ' + name + '\nSymbol =  ' + symbol + '\nPrice = ' + str(price) + '\nMarket Cap =  ' + str(market_cap))
        print('=' * 20)


def general_cryptocurrency_information():
    with urllib.request.urlopen("https://api.coinmarketcap.com/v2/global/") as url:
        information = json.loads(url.read().decode())
        active_cryptocurrencies = (information['data']['active_cryptocurrencies'])
        active_markets = (information['data']['active_markets'])
        bitcoin_dominance = (information['data']['bitcoin_percentage_of_market_cap'])
        total_market_cap = (str(round(information['data']['quotes']['USD']['total_market_cap'])).rstrip('0').rstrip('.'))
        print('=' * 20)
        print('Active Cryptocurrencies= ' + str(active_cryptocurrencies) + '\nActive Markets =  ' + str(active_markets) + '\nBitcoin Dominance = ' + str(bitcoin_dominance) +  '%' + '\nTotal Market Cap =  ' + str(total_market_cap) + ' USD')
        print('=' * 20)
        

bitcoin_information()
ethereum_information()
chainlink_information()
general_cryptocurrency_information()