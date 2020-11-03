from datetime import date, timedelta
import yfinance as yf

class Holding:
  def __init__(self, symbol: str, shares: str):
    self.symbol:str = symbol
    self.shares:int = int(str(shares).strip())
  
  def __str__(self):
    return self.symbol.ljust(8, " ")  + str(self.shares) + "\n"


class Portfolio:
  holdings: list
  openDate: date

  def __init__(self, openDate: date = date.today()):
    self.holdings = list()
    self.openDate = openDate

  def add_holding(self, holding: Holding):
    self.holdings.append(holding)

  def __str__(self):
    string = "Portfolio:\n"
    string += "Opened: " + self.openDate.strftime("%d-%b-%Y") + "\n"
    for holding in self.holdings:
      string += str(holding)
    return string


def get_price(symbol):
  priceDate = date.today() - timedelta(days=10)
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history[-1:]["Close"][0],2)

def get_historical_price(symbol, priceDate):
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history["Close"][0],2)