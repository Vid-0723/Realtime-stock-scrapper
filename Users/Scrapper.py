
import requests
import httpx
import csv
import requests
from bs4 import BeautifulSoup
import yfinance as yf
class Stock:
    def __init__(self, company, price, change):
        self.company = company
        self.price = price
        self.change = change

def scrape_stock_data(ticker):
    stocks = []

    for t in ticker:


        ticker = yf.Ticker(t)
    
    # Get the live price
        live_price = ticker.history(period='1d')['Close'][-1]

        print("Live Price",live_price)
        url = f"https://finance.yahoo.com/quote/{t}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup)
        with open(f"{t}_page.html", "w", encoding="utf-8") as html_file:
            html_file.write(str(soup))
        stock_info_div = soup.find('div', {'id': 'quote-header-info'})
        if stock_info_div:
            fin_streamer = stock_info_div.select_one("div:nth-of-type(3) div:nth-of-type(1) div fin-streamer:nth-of-type(1)").get_text()
            print("fin",fin_streamer)
        stock = Stock(
            company=soup.select_one("h1").get_text(),
            price=soup.select_one("[data-field='regularMarketPrice']").get_text(),
            change=soup.select_one("[data-field='regularMarketChangePercent']").get_text()
        )

        stocks.append(stock)

    return stocks


def get_ticker_list():
    client = httpx.Client()
    page=0
    reqUrl = f"https://finance.yahoo.com/screener/unsaved/78b0c185-f2e9-49f2-8665-cb113f39c1b3?count=100&offset={page}"
    listofallname=[]
    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
    }

    payload = ""

    r = client.get(reqUrl, headers=headersList)
    soup=BeautifulSoup(r.text,'html.parser')
    total=int((soup.find('div', class_='Fw(b) Fz(36px)')).text)//100
    all_name=soup.find_all('a', class_="Fw(600) C($linkColor)")
    for element in all_name:
        listofallname.append(element.text)
    page=100

    for i in range(total):
        reqUrl = f"https://finance.yahoo.com/screener/unsaved/78b0c185-f2e9-49f2-8665-cb113f39c1b3?count=100&offset={page}"
        r = client.get(reqUrl, headers=headersList)
        soup=BeautifulSoup(r.text,'html.parser')
        all_name=soup.find_all('a', class_="Fw(600) C($linkColor)")
        for element in all_name:
            listofallname.append(element.text)
        page+=100
    client.close()
    return listofallname

def save_to_csv(stocks, filename='stocks.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        headers = ["company", "price", "change"]
        writer.writerow(headers)

        for stock in stocks:
            row = [stock.company, stock.price, stock.change]
            writer.writerow(row)

if __name__ == "__main__":
    pass
    # stocks = scrape_stock_data(ticker)
    # print(stocks[0].price)
    # save_to_csv(stocks)

    # get_ticker_list()
    # print("Data scraped and saved to stocks.csv")