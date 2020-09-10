# CAW
# Section 1, Task 1
import pandas as pd
import requests
import datetime
url = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USDT&e=binance&limit=2000&toTs=1585699200'
f = requests.get(url)
ipdata = f.json()
df = pd.DataFrame(ipdata['Data']['Data'])
df = df.iloc[:, 0:-2]
fmt = "%Y-%m-%d %H:%M:%S"
df['datetime'] = df['time']
#for i in range(len(df)):
#    df['datetime'][i] = datetime.datetime.fromtimestamp(df['time'][i]/1000.).strftime(fmt)
df['datetime'] = pd.to_datetime(df['time'],unit='s')
df = df.rename(columns={'volumefrom': 'volume'})
df = df.rename(columns={'volumeto': 'baseVolume'})
df = df.sort_values(by = ['datetime'])
df.to_csv("s1t1.csv")

# Questions:
# 1. At the end of the URL, when specifying the '&toTs{1585699200}', it should be '&toTs={1585699200}' according to the API documentation, but when I include the '='
# it gives me an error message.
# 2. Although the toTs is included in the url, the data is still retrieved from the current time, how to fix it..?
