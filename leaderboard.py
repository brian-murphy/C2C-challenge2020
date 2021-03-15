"""
WARNING: You shouldn't need to touch this file for the sake of the labs

This module was tested on python3, but I think it should be easily convertible
to python2.x if necessary. You'll need to install the 'requests' module through
pip.
"""

import requests
from lab1 import Portfolio
from lab2 import portfolio_value
from datetime import date
import yfinance as yf
import os

filepath = 'portfolio.csv'
validation_portfolio = Portfolio()
validation_returns = 0.0
validation_benchmark_returns = 0.0
with open(filepath) as fp:
  lines = fp.readlines()
  for line in lines:
    validation_portfolio.add_stock_position(*line.split(','))

URL = "https://hmresj58ib.execute-api.us-east-1.amazonaws.com/production/trials"

def submit_leaderboard(stage, completion):
  """Submits the results of a trial to the leaderboard api for recording.

      :param name: The name of the user submitting the trial. This will be used
        to display the user's results on the website.
      :param stage: an integer representing the stage of the challenge this
        submission pertains to.
      :param completion: a string summarizing the trial's results. It can be a
        a date, (if the goal of the stage is to complete it in the least amount
        of time) or it can be a string-encoded number (if the goal of the stage
        is to have the best-optimized result).

      :returns: a dict with two properties: "statusCode" and "body". "body" is a
        user-friendly string representing the result of the submission.
        Potential "statusCodes" are:
        * 200 -- This is the user's first submission, or new best result.
        * 403 -- The stage isn't open for submissions yet
        * 409 -- This submission is equal to or worse than one of the user's
                previous submissions for this stage.
        * 400 -- Invalid input. This shouldn't appear in general.
  """
  name = os.environ["REPL_OWNER"]
  if not isinstance(stage, int):
    raise TypeError("'stage' parameter should be an integer")
  if not isinstance(completion, str):
    raise TypeError("'completion' parameter should be a string")

  response = requests.put(URL, json = {
    'name': name,
    'stage': stage,
    'completion': completion
  })

  return response.json()


def submit_portfolio(portfolio):
  if "goog" in portfolio.holdings and portfolio.holdings["goog"] == 1 \
    and "fds" in portfolio.holdings and portfolio.holdings["fds"] == 3 \
    and "tsla" in portfolio.holdings and portfolio.holdings["tsla"] == 5 \
    and "aapl" in portfolio.holdings and portfolio.holdings["aapl"] == 1:
    print("That's a good portfolio!")
    print(portfolio)
    return True
  
  print("It's definitely missing something. Either that, or it has too much of something else.")
  print(portfolio)
  return False

def get_historical_price(symbol, priceDate):
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history["Close"][0],2)

def test_get_portfolio_value(portfolio, date):
  total = 0
  for ticker in portfolio.holdings.keys():
    total += get_historical_price(ticker, date) * portfolio.holdings[ticker]
  return total

def submit_portfolio_value(testValue, portfolio, date):
  validationValue = test_get_portfolio_value(portfolio, date)
  return round(validationValue, 2) == round(testValue, 2)

def test_portfolio_returns(portfolio, startDate, endDate):
  return round((portfolio_value(portfolio, endDate) / portfolio_value(portfolio, startDate) - 1) * 100,2)

def submit_portfolio_returns(testReturns, portfolio: Portfolio, startDate: date, endDate: date):
  validationReturns = test_portfolio_returns(portfolio, startDate, endDate)
  if validationReturns == round(testReturns, 2):
    return True

  print("The percent returns don't match for the portfolio")
  if testReturns > validationReturns:
    print("percent returns are too high.")

  if testReturns < validationReturns:
    print("percent returns are too low")

  return False
    

def submit_adjusted_returns(adjusted_returns):
  validation_adjusted_returns = round(((100 + validation_returns) / (100 + validation_benchmark_returns) - 1) * 100,2)
  if round(adjusted_returns, 2) != validation_adjusted_returns:
    raise Exception("Adjusted returns don't line up.")
  print("{:.2f}% adjusted returns is still great!")

