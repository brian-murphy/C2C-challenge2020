"""
LAB 1

At FactSet, the first step of the portfolio lifecycle involves parsing 
clients' holdings into our portfolio databases. In this lab you are 
given an input ".csv" file that represents a portfolio, and must parse
it into an instance of the `Portfolio` class, seen below.

HINT:
* portfolio.csv is the input file that's being parsed
* split a string: https://www.w3schools.com/python/ref_string_split.asp
"""


"""
Warning: NO NEED TO CHANGE THIS CLASS
The `Portfolio` class represents a portfolio by storing the ticker
symbols and number of shares held for the stocks that the investor owns.

Use the `add_stock_position()` method to add a stock position to the
portfolio.

Use the `get_all_stocknames()` method to list the ticker symbols of the
stocks held in the portfolio.

Use the `get_share_count()` method to determine how many shares of a
stock are held in the portfolio.
"""
class Portfolio:
  holdings: dict
  def __init__(self):
    self.holdings = dict()
  """
  Use this method to add a position in a stock to this Portfolio
    `stockName` -- The ticker symbol of the stock to open a position in (BUY)
    `shares` -- The number of shares of the stock to purchase
  """
  def add_stock_position(self, stockName:str, shares):
    if stockName in self.holdings:
      print("Warning! This portfolio already has a position in " + stockName)
    self.holdings[stockName] = int(shares) if isinstance(shares, str) else shares
  """
  Use this method to get a list of the ticker symbols of all the stocks
  held in this portfolio.
  """
  def get_all_stocknames(self):
    return self.holdings.keys()
  """
  Use this method to get the number of shares this portfolio holds of a
  particular stock.
    `stockName` -- The ticker symbol of the stock
    returns -- the number of shares held
  """
  def get_share_count(self, stockName:str):
    if not stockName in self.holdings:
      raise Exception("Error! Portfolio doesn't have a position in " + stockName)
    return self.holdings[stockName]
  """
  Converts this portfolio to string format
  """
  def __str__(self):
    string = "Portfolio: \n"
    for holding in self.holdings.keys():
      string += holding + " " + str(self.holdings[holding]) + "\n"
    return string

"""
Implement this function! (see instructions above)
"""
def parse_portfolio(filepath):
  portfolio = Portfolio()
  with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
      print(line)
      # TO DO: parse the file lines and add holdings to the portfolio
      row = line.split(",")
      portfolio.add_stock_position(row[0], row[1])
  return portfolio


