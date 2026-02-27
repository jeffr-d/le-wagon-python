# pylint: disable=missing-docstring

# TODO: start by defining a `portfolio` using a dict!

portfolio = {
  "AAPL": {
    "volume": 10,
    "strike": 154.12
  },
  "GOOG": {
    "volume": 2,
    "strike": 812.56
  },
  "TSLA": {
    "volume": 12,
    "strike": 342.12
  },
  "META": {
    "volume": 18,
    "strike": 209.0
  }
}
# print the volume of TSLA stocks in the portfolio
print(portfolio['TSLA']['volume'])

# print the strike of GOOG in the portfolio
print(portfolio['GOOG']['strike'])

market = {
  "AAPL": 198.84,
  "GOOG": 1217.93,
  "TSLA": 267.66,
  "META": 179.06
}