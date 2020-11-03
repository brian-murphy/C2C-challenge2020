"""
This module was tested on python3, but I think it should be easily convertible
to python2.x if necessary. You'll need to install the 'requests' module through
pip.
"""

import requests
from portfolio import Portfolio, Holding, get_price
from datetime import date, timedelta

URL = "https://hmresj58ib.execute-api.us-east-1.amazonaws.com/production/trials"

def submit_leaderboard(name, stage, completion):
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
  if not isinstance(name, str):
    raise TypeError("'name' parameter should be a string")
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
  if portfolio.openDate != date(2020,1,2):
    raise Exception("Invalid open date, leave it as date(2020,1,2)")
  if any(holding.symbol == "goog" and holding.shares == 10 for holding in portfolio.holdings) \
    and any(holding.symbol == "fds" and holding.shares == 32 for holding in portfolio.holdings) \
    and any(holding.symbol == "tsla" and holding.shares == 5 for holding in portfolio.holdings) \
    and any(holding.symbol == "aapl" and holding.shares == 12 for holding in portfolio.holdings):
    print("That's a good portfolio!")
    print(portfolio)
    print()
    return True
  
  print(portfolio)
  print()
  raise Exception("It's definitely missing something. Either that, or it has too much of something else.")
  # Mr. Peabody - Pinkalicious and the Pink Drink

def submit_portfolio_value(value):
  filepath = 'portfolio.csv'
  total=0
  portfolio = Portfolio(date(2020,1,2))
  with open(filepath) as fp:
    lines = fp.readlines()
    for line in lines:
      portfolio.add_holding(Holding(*line.split(',')))
  for holding in portfolio.holdings:
    total += int(holding.shares) * get_price(holding.symbol)
  if(round(value,2) != 29525.85):
    raise Exception("The value of " + "{:2f}".format(value) + " doesn't add up")

  print("${:,.2f} is a good start! How does it compare?".format(value))
  return True


if __name__ == "__main__":
  """A simple test of the api"""
  print(submitLeaderboard("Brian", 1, "bbbbbbb"))

