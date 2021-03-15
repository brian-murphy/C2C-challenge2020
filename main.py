"""
WARNING: you shouldn't have to touch this file for the sake of the labs
"""

from lab1 import parse_portfolio
from lab2 import portfolio_returns, portfolio_value
from lab3 import portfolio_name
from leaderboard import submit_portfolio, submit_leaderboard, submit_portfolio_returns, submit_portfolio_value
from replit import db
from datetime import datetime, date

def clearDb():
  for key in db.keys():
    del db[key]

YEAR_START_2020 = date(2020, 1, 2)

def get_from_db(key):
  try:
    return db[key]
  except Exception:
    return None

def get_lab_success(labFile):
  labSuccess = get_from_db(labFile + "-success")
  if labSuccess == None:
    return False
  return labSuccess

def set_lab_success(labFile, success):
  db[labFile + "-success"] = success

def has_file_changed(filePath):
  contentKey = filePath + "-content"
  with open(filePath) as fp:
    content = fp.read()
    prevContent = get_from_db(contentKey)
    db[contentKey] = content
    return content != prevContent

"""
Checks if the file has changed since the last run.
"""
def should_run_lab(labFile):
  labSuccess = get_lab_success(labFile)
  fileChanged = has_file_changed(labFile)
  # print(labFile + " labSuccess: " + str(labSuccess) + " fileChanged: " + str(fileChanged))
  return (not labSuccess) or fileChanged

def run_labs():
  # clearDb()
  # if True == True:
  #   return
  portfolio = parse_portfolio(portfolio_name())

  if should_run_lab("lab1.py"):
    print("Checking lab 1 results...")
    lab1Success = submit_portfolio(portfolio)
    if lab1Success:
      print("Congratulations, you have completed the first lab!")
      submit_leaderboard(1, datetime.now().strftime("%H:%M:%S"))
    else:
      print("Lab 1 failed")
      return
    set_lab_success("lab1.py", lab1Success)
  else:
    print("Lab 1 complete")

  print()

  openingValue = portfolio_value(portfolio, YEAR_START_2020)
  returns = portfolio_returns(portfolio, YEAR_START_2020, date.today())

  if should_run_lab("lab2.py"):
    print("Checking lab 2 results...")
    lab2Part1Success = submit_portfolio_value(openingValue, portfolio, YEAR_START_2020)
    if not lab2Part1Success:
      print("Lab 2 failed")
      print("There's something wrong with the 'portfolio_value' function")
      set_lab_success("lab2.py", False)
      return 
    
    lab2Part2Success = submit_portfolio_returns(returns, portfolio, YEAR_START_2020, date.today())

    if not lab2Part2Success:
      print("Lab 2 failed")
      print("There's something wrong with the 'portfolio_returns' function")
      set_lab_success("lab2.py", False)
      return

    print("Congratulations, you have completed the second lab!")
    submit_leaderboard(2, datetime.now().strftime("%H:%M:%S"))
    set_lab_success("lab2.py", lab2Part2Success)
  else:
    print("Lab 2 complete")

  print()
  print("Your portfolio made {:.2f}% returns from ".format(returns) + YEAR_START_2020.strftime("%m/%d/%Y") + " to " + date.today().strftime("%m/%d/%Y"))

  hasLabChanged = has_file_changed("lab3.py")
  hasPortfolioChanged = has_file_changed(portfolio_name())
  if hasLabChanged or hasPortfolioChanged:
    print("Submitting portfolio to leaderboard...")
    if openingValue < 10000:
      bestResult = get_from_db("best-result")
      if bestResult == None or returns > bestResult:
        print("This is your new highest return!")
        db["best-result"] = returns
      elif returns < bestResult:
        print("This portfolio has a lower return than your best: ({:.2f}%)".format(bestResult))
      submit_leaderboard(3, "{:.2f}%".format(returns))
    else:
      print("Opening value should be no more than $10,000. Yours: ${:.2f}".format(openingValue))
  else:
    print("Results were already submitted")

run_labs()