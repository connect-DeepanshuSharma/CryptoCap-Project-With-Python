
import os
import json
import time
import requests

import pyttsx3
from datetime import datetime

os.system('cls')
convert = 'USD'
engine = pyttsx3.init()
listings_url = 'https://api.coinmarketcap.com/v2/listings/?convert=' + convert
url_end = '?structure=array&convert=' + convert

request = requests.get(listings_url)
results = request.json()
data = results['data']

ticker_url_pairs = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url

print()
print('ALERTS TRACKING...')
print()

already_hit_symbols = []

while True:
    with open(input('Enter File you want to access\n')) as inp:
        for line in inp:
            ticker, amount = line.split()
            ticker = ticker.upper()
            ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[ticker]) + '/' + url_end

            request = requests.get(ticker_url)
            results = request.json()

            currency = results['data'][0]
            name = currency['name']
            last_updated = currency['last_updated']
            symbol = currency['symbol']
            quotes = currency['quotes'][convert]
            price = quotes['price']


            if float(price) >= float(amount) and symbol not in already_hit_symbols:
                last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')

                engine.say(name + ' hit ' + amount + 'on' + last_updated_string)
                engine.runAndWait()

                print(name + ' hit ' + amount + ' on ' + last_updated_string)
                already_hit_symbols.append(symbol)


    print()
    os.system('cls')
    os.system('python coincap_main.py')
    print()
    print('Alert Processing Running... Press CTRL+C to exit')
    time.sleep(5000)
