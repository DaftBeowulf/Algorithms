#!/usr/bin/python

import sys

denominations = [1, 5, 10, 25, 50]


def making_change(amount, denominations, cache=[]):
    if cache == []:
        cache = [0 for i in range(amount+1)]
        denominations.reverse()
    if amount < 0:
        return 0
    if 0 <= amount <= 1:
        return 1
    if cache[amount] > 0:
        return cache[amount]
    else:
        for coin in denominations:
            if amount-coin > 0:
                cache[amount] += making_change(amount -
                                               coin, denominations, cache)
            elif amount-coin == 0:
                cache[amount] += 1

    return cache[amount]


print(making_change(10, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
