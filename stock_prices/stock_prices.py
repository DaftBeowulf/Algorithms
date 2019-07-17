#!/usr/bin/python

import argparse
import math
"""
find_max_profit([10, 7, 5, 8, 11, 9]) = 6
return 11-5 =6

for each possible buy number(each except the last),
find highest profit difference in array items AFTER it (sell) 
[10, 7, 5, 8, 11, 9]
  b            s
p=1

[10, 7, 5, 8, 11, 9]
     b         s
p=4

[10, 7, 5, 8, 11, 9]
        b      s
p=6

[10, 7, 5, 8, 11, 9]
           b  s
p is still 6

[10, 7, 5, 8, 11, 9]
               b  s
p is still 6

loop ends, return 6  
"""


def find_max_profit(prices):

    # declare lowest number possible to catch inputs with only negative profits
    profit = -math.inf

    for i, buy in enumerate(prices[:-1]):
        for sell in prices[i+1:]:
            if sell-buy > profit:
                profit = sell-buy

    return profit


print(find_max_profit([10, 7, 5, 8, 11, 9]))

if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
