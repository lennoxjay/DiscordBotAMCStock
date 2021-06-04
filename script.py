import discord
import os
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #get the share price
# as shown in https://towardsdatascience.com/python-how-to-get-live-market-data-less-than-0-1-second-lag-c85ee280ed93
#Interval required 5 minutes
data = yf.download(tickers='AMC', period='5d', interval='5m')
#Print data
data

#stockprice = data.iat[,4]
stockprice = data['Close'].iloc[-1]
stockprice = round(stockprice, 2)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$amc'):
        await message.channel.send('The current AMC stock price in USD is ' + str(stockprice))

client.run(os.getenv('TOKEN'))

