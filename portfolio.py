from datetime import date

class Holding:
  def __init__(self, security: str, shares: int):
    self.security = security
    self.shares = shares
  
  def __str__(self):
    return self.security.ljust(8, " ")  + self.shares


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

