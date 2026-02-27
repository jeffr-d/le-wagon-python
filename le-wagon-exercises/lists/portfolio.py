# pylint: disable=missing-docstring

aapl = [ 10, 154.12 ]
goog = [  2, 812.56 ]
tsla = [ 12, 342.12 ]
fb   = [ 18, 209.0  ]

portfolio = [ aapl, goog, tsla, fb ]

#            AAPL     GOOG    TSLA      FB
market = [ 198.84, 1217.93, 267.66, 179.06 ]

total_pnl = 0

# We loop through your portfolio using enumerate to get the index
for i, stock_data in enumerate(portfolio):
    volume = stock_data[0]
    strike_price = stock_data[1]
    market_price = market[i] # Match the index to the market list
    
    # Calculate PNL for this specific stock
    stock_pnl = (market_price - strike_price) * volume
    total_pnl += stock_pnl

print(f"Overall Portfolio PNL: ${total_pnl:.2f}")