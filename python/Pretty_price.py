""" 3.21 => 3.99
have the flexibility to say 3.99 or 3.95 either way. or 3.00.

input 3.20 and variable .99 => 3.99
needs to remove the cents, and add the variable, and add it in the following way. 3.99.
"""
import math

def pretty_price(dollars, cents_wanted):
    whole_dollar = math.modf(dollars)
    if isinstance(cents_wanted, int):
        cents_wanted = cents_wanted * 0.01

    return(whole_dollar[1]) + (cents_wanted)

print(f"The price is : ${(pretty_price(2.20, 57))}")



    