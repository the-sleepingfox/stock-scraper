import requests
from bs4 import BeautifulSoup

try:
    source= requests.get("https://groww.in/stocks/filter?closePriceHigh=100000&closePriceLow=0&marketCapHigh=2000000&marketCapLow=0&page=0&size=15&sortType=ASC")
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    stocks = soup.find('tbody').find_all('tr')
    print("\n\nTop 15 stocks according to there Market Cap\n\n")

    for stock in stocks:
        stockName = stock.find('td', class_="fs14 clrText").a.text

        marketPrice = stock.find('div', class_="fw500 st76CurrVal").text

        dayChange = stock.find('span', class_ ="st76PercentChange").text

        closingPrice = stock.find('td', class_="fs14 clrText st76Pad16").text

        print(stockName,":\n    Current Price:- ", marketPrice,"\n    Prev. Price  :- ", closingPrice, "\n    Day Change   :- ", dayChange, "\n")

except Exception as e:
    print(e)
print("\n")