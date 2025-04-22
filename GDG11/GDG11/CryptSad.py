#Alan's mentor group task for data scientists , data parsing ,vizualization and etc.
#The panda lib is entirely new for me so I am just tryna learn :p
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    'vs_currency': 'usd',
    'days': '30'
}
response = requests.get(url, params=params)
data = response.json()

prices = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
prices['timestamp'] = pd.to_datetime(prices['timestamp'], unit='ms')

plt.figure(figsize=(10,5))
plt.plot(prices['timestamp'], prices['price'])
plt.title('Bitcoin Price - Last 30 Days')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()
plt.show()
