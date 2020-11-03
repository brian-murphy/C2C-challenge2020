from lab1 import username, parse_portfolio, portfolio_value
from leaderboard import submit_leaderboard, submit_portfolio, submit_portfolio_value
from datetime import datetime

if username() == "username":
  raise Exception("Fill in a username for our leaderboard.")

portfolio = parse_portfolio()
submit_portfolio(portfolio)

value = portfolio_value(portfolio)
submit_portfolio_value(value)

print("Congratulations, you have completed the first lab.")
submit_leaderboard(username(),1,str(datetime.now()))
print("Visit http://leaderboard to view the leaderboard")
