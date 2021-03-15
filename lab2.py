"""
LAB 2

In this lab, you'll write some analytical functions to run on the
portfolio that we parsed in lab 1. We want to calculate the returns
(profit or loss) on a portfolio over a specified period of time.

Step 1: Implement the `portfolio_value()` function. This function accepts
a portfolio and a date as arguments. You'll need to calculate the total
value of the portfolio at that date and return it.

HINT: You'll need to use the `get_historical_price()` function. 
* What arguments does `get_historical_price()` accept?
* Take a look at the `Portfolio` class in Lab 1. What methods will we
need to call in order to calculate the portfolio's total value?

Step 2: Implement the `portfolio_returns()` function. This function accepts
a portfolio, a start date, and an end date as arguments. You'll need to
calculate the amount that the portfolio's value grew or shrunk from the
start date to the end date, expressed as a percentage of the portfolio's
value at the start date.

Examples:
  Portfolio start date value: $1000
  Portfolio end date value: $1500
  Returns: 50%

  Portfolio start date value: $1000
  Portfolio end date value: $800
  Returns: -20%

"""

from lab1 import Portfolio
from datetime import date, timedelta
import yfinance as yf

"""
Warning: NO NEED TO TOUCH
This function will return the price of a stock on a date. If today's price
is requested, it will return the most recent closing price.
  `symbol` -- the ticker symbol of the requested stock
  `priceDate` -- the date at which the price is read
"""
def get_historical_price(symbol, priceDate):
  ticker = yf.Ticker(symbol)
  if priceDate == date.today():
    # today might not be a market day
    history = ticker.history(startDate=priceDate - timedelta(days=10))
    # return the most recent closing price
    return round(history[-1:]["Close"][0], 2)
  history = ticker.history(start=priceDate)
  return round(history["Close"][0], 2)


"""
STEP 1: implement portfolio_value() (see comments above)
"""
def portfolio_value(portfolio: Portfolio, date: date):
  total = 0
  # for ...
  return total

"""
STEP 2: implement portfolio_returns() (see comments above)
"""
def portfolio_returns(portfolio: Portfolio, startDate: date, endDate: date):
  # Calculate the value for the potfolio at its open date
  # opening_value = ...

  # Calculate the value for the portfolio today
  # close_value = ...

  # Calculate the percentage change since opening
  return 0
