import CoinBaseExchangeAuth
import MarketSocket
import requests
from threading import Timer


class AuthenticatedClient:
  
      def __init__(self, CoinBaseExchangeAuth):
        self.auth = CoinBaseExchangeAuth
       
     #size and price may be given as ints or strings, product_id must be a string
     def buy(size, price, product_id):
      size = str(size)
      price = str(price)
      api_url = 'https://api.gdax.com/'
			r = requests.get(api_url + 'accounts', auth=auth)

			order = {
			      'size': size,
			      'price': price,
			      'side': 'buy',
			      'product_id': product_id,
			   	}

			r = requests.post(api_url + 'orders', json=order, auth=auth)
			print(r.status_code)
			print("------------------BOUGHT-------------")
			print(order)

  
