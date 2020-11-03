"""
At FactSet the first step of the portfolio lifecycle involves parsing 
clients' holdings into our portfolio databases. In this lab you are 
given an input file as comma separated values and calculating the 
portfolio's value. Each line has a symbol and number of shares.

portfolio.py contains documentation for the portfolio object
portfolio.csv is the input file that's being parsed
https://www.w3schools.com/python/ref_string_split.asp

"""

from portfolio import Portfolio, Holding, get_price
from datetime import date

filepath = 'portfolio.csv'
portfolio = Portfolio(date(2020,1,2))

def username():
  # Get started by registering a username
  return "username"

def parse_portfolio():
  with open(filepath) as fp:
    lines = fp.readlines()
    #for line in lines:
      # Split each lines
      
      # Place the values into a new Holding object

      # Add the holding to the portfolio.
  return portfolio

def portfolio_value(Portfolio: portfolio):
  total = 0
  # Loop through each holding in the portfolio

    # Calculate the value of the holding using the get_price helper method

    # Add the value to the total

  return total
