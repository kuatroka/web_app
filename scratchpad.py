import requests

url = 'https://min-api.cryptocompare.com/data/histominute?fsym=BTC&tsym=USD&limit=\
    10&aggregate=0&e=Kraken'
url_output = requests.get(url).json()['Data']

print(url_output[0])
