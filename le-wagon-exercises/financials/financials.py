# pylint: disable=missing-docstring

# TODO: 1st exercise: Define the `forward_price` function
import math
def forward_price(spot, interest_rate, time):
    
# calculating the exponent part
    exponent = math.exp(interest_rate * time)

# multiply by the spot price
    price = spot * exponent

# return the result rounded to 2 decimal spaces
    return round(price, 2)

# TODO: 2nd exercise: Define the `short_pnl` function
def short_pnl(positions, mtm):
    total_pnl = 0
    for i in range(len(positions)):
        # for a short, P&L = strike - market
        total_pnl += (positions[i] - mtm[i])
        
    return float(total_pnl)


