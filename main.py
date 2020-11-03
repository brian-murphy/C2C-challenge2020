from lab1 import parse_portfolio, portfolio_value
from lab2 import username, portfolio_returns, benchmark_returns, adjusted_returns
from leaderboard import submit_leaderboard, submit_portfolio_returns, submit_benchmark_returns
from datetime import datetime

if username() == "username":
  raise Exception("Fill in a username for our leaderboard.")

portfolio = parse_portfolio()
value = portfolio_value(portfolio)

returns = portfolio_returns(portfolio)
submit_portfolio_returns(returns)

benchmark_returns = benchmark_returns(portfolio.openDate)
submit_benchmark_returns(benchmark_returns)

adjusted_returns = adjusted_returns(returns, benchmark_returns)
print("{:.2f}% adjusted returns".format(adjusted_returns))


print("Congratulations, you have completed the second lab.")
submit_leaderboard(username(),2,str(datetime.now()))
print("Visit http://leaderboard to view the leaderboard")
