# from channels.consumer import SyncConsumer,AsyncConsumer,StopConsumer
import asyncio
import json
import datetime
from .models import Stock_List 
# class MySyncConsumer(SyncConsumer):
#     async def websocket_connect(self,event):

#         print("Websocket Connected...",event)
#         await self.send(
#             {
#             'type':'websocket.accept'
#             }
#         )
#     def websocket_receive(self,event):
#         print("Message...",event)

#     def websocket_disconnect(self,event):
#         print("Websocket Disconnected...",event)


from channels.generic.websocket import AsyncWebsocketConsumer
from traceback import print_exc
import yfinance as yf

import csv
import requests
from bs4 import BeautifulSoup
from StockProject.settings import SCRAPPING_URL




def scrape_stock_data(ticker):
    stocks = []

    for t in ticker:
        url = f"{SCRAPPING_URL}{t}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        stock_info_div = soup.find('div', {'id': 'quote-header-info'})
        ticker = yf.Ticker(t)
        all_tickers = yf.Tickers('')

        ticker_list = all_tickers.tickers
        print(ticker_list)
        live_price = ticker.history(period='1d')['Close'][-1]

        print(live_price)
        try:
            stocks.append({
                "company" :stock_info_div.find('h1').get_text(),
                "price" : live_price,
                "change" : stock_info_div.select_one("[data-field='regularMarketChangePercent']").get_text()    ,
            })

        except:
            stocks.append({
                "company" :t,
                "price" : live_price,
                # "change" : stock_info_div.select_one("[data-field='regularMarketChangePercent']").get_text()    ,
            })

    return stocks

def save_to_csv(stocks, filename='stocks.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ["company", "price", "change"]
        writer.writerow(headers)

        for stock in stocks:
            row = [stock.company, stock.price, stock.change]
            writer.writerow(row)

ticker = [i.symbol for i in Stock_List.objects.filter(is_active = True)]

    # stocks = scrape_stock_data(ticker)
    # save_to_csv(stocks)
    # print("Data scraped and saved to stocks.csv")

class MySyncConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Channel Layer...",self.channel_layer)
        print("Channel Name..",self.channel_name)
        while True:
            try:
                print("Reading Stocks")
                stocks = scrape_stock_data(ticker)
                for stock in stocks:
                    print(stock["company"])
                    print(stock["price"])
                    current_time = datetime.datetime.now().strftime('%H:%M:%S')
                await self.send(text_data=json.dumps(stocks))
            except:
                print_exc()
            await asyncio.sleep(1)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        print("Receive from client",text_data)
        # await self.send(text_data=text_data)