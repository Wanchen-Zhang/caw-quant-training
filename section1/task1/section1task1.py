#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:11:20 2020

@author: wanchenzhang
"""


# Questions:
# 1. The basic structure is the same as the s1t1.py but has an additional while loop 
# to constantly retrieve data. It seems didn't work as desired... 
import pandas as pd
import requests
import datetime
import time
# Section 1, Task 1
# Write a function to download histohour data, parameters:
# fsym: BTC, tsym: USDT, start_time="2017-04-01", end_time="2020-04-01", e='binance'
# time-zone: UTC

def get_data(fsym, tsym, start_time, end_time, e):
    """ returns pandas DataFrame 
    """
    url = 'https://min-api.cryptocompare.com/data/v2/histohour?'
    fmt = "%Y-%m-%d %H:%M:%S"
    start_time = str(datetime.datetime.strptime(start_time, '%Y-%m-%d'))
    start_time = int(time.mktime(time.strptime(start_time, fmt)))
    end_time = str(datetime.datetime.strptime(end_time, '%Y-%m-%d'))
    end_time = int(time.mktime(time.strptime(end_time, fmt)))
    date = end_time
    holder = []
    # Retrieve the data backwards
    while date>start_time:
        # Modify the URL using the given parameters
        url = url+"fsym="+fsym+"&tsym="+tsym+"&e="+e+'&limit=2000'+'toTs='+str(date)
        f = requests.get(url)
        ipdata = f.json()
        df = pd.DataFrame(ipdata['Data']['Data'])
        df = df.iloc[:, 0:-2]
        df['datetime'] = df['time']
        df = df.rename(columns={'volumefrom': 'volume'})
        df = df.rename(columns={'volumeto': 'baseVolume'})
        #for i in range(len(df)):
            #df['datetime'][i] = datetime.datetime.utcfromtimestamp(df['datetime'][i]).strftime(fmt)
        df['datetime'] = pd.to_datetime(df['time'],unit='s')
        print(df)
        holder.append(df)
        # Update the date
        date = df['datetime'][0]
    
    # sort the holder by date ascendingly
    holder = holder.sort_values(by = ['datetime'])
    return holder


    
    











# Use the __main__ section for all of your test cases. 
# This section will automatically be executed when the file is run in Python
if __name__ == '__main__':
    print(get_data('BTC','USDT', "2017-04-01","2020-04-01",'binance'))
