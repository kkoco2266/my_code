import requests
import sys

file_with_price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

try:
    rate = file_with_price['bpi']['USD']['rate_float']
    price = float(sys.argv[1]) * rate
    print(f'${price:,.4f}')
except IndexError:
    sys.exit('Missing command-line argument')
except ValueError:
    sys.exit('Command-line argument is not a number')

print(requests.exceptions.RequestException)
