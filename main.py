from portfolio import Portfolio
from portfolio import Holding
import yfinance as yf
from datetime import date, timedelta

filepath = 'portfolio.csv'
portfolio = Portfolio(date(2020,1,2))

def get_historical_price(symbol, priceDate):
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history["Close"][0],2)

def get_price(symbol):
  priceDate = date.today() - timedelta(days=10)
  ticker = yf.Ticker(symbol)
  history = ticker.history(start=priceDate)
  return round(history[-1:]["Close"][0],2)

# Parse a portfolio
with open(filepath) as fp:
   lines = fp.readlines()
   for line in lines:
    portfolio.add_holding(Holding(*line.split(',')))
    
   print(portfolio)

print("\n\n\n")

total = 0

# Parse market values as part of the portfolio load
for holding in portfolio.holdings:
  price = get_price(holding.security)
  value = int(holding.shares) * price
  total += value
print("Total: " + "{:.2f}".format(total))

historical_total = 0

# Calculate portfolio value
for holding in portfolio.holdings:
  price = get_historical_price(holding.security, portfolio.openDate)
  value = int(holding.shares) * price
  historical_total += value
print("Historical total: " + "{:.2f}".format(historical_total))
print("Gains: " + "{:.2f}".format(total-historical_total))

# Compare performance to SP50
historical_benchmark_price = get_historical_price("^GSPC", portfolio.openDate)
benchmark_shares = historical_total / historical_benchmark_price
benchmark_earnings = (get_price("^GSPC") - historical_benchmark_price) * benchmark_shares 
print("Benchmark Earnings: " + "{:.2f}".format(benchmark_earnings))

# Compare to treasury bonds


# Create a new portfolio 
# Calc new portfolio perfomance over 6mo vs sp50
# Leaderboard for top returns
# Come back to see how your portfolio does next week/month/year


# Build this as a service to hook into a leaderboard
#   does validation on their values returned
#   keeps track of who completes first
#   Gets holdings returns for the new portfolio and ranks users
