#!/usr/bin/python

import sys


"""
loop that starts big, ends small
d=[50,25,10,5,1]
a=amount
ex: m_c(6)
    6-50 < 0 #loops ends, next coin
        6-25 < 0 #same
            6-10 < 0 #same
                6-5>0 #keep going, but with sliced denominations: [5,1]. also add 5 to the array of transactions
                    1-5 > 0 # try again, but without the 5
                        1-1==0 #stop, and add 1 to the array of transactions: [5,1]
                also run 6-1 > 0
                            5-5 ==0 #stop: [1,5]
                            5-1 == 4
                                4-1==3
                                    3-1==2
                                        2-1==1
                                            1-1==0 #stop: [1,1,1,1,1,1]

iteratively:
    cache[amount]=[]
    while amount>0:
    cache[-1]=[]
        for i in range([1, 5, 10, 25, 50]) (backwards)
            if amount-d[i] <0:
                pass
            elif amount-d[i] == 0:
                cache[-1] += [d[i]]
                amount-=d[i] #0
            else:
                cache[-1] += [d[i]]
                amount-=d[i]

"""


def making_change(amount, denominations, cache=[]):
    # first value a 0 index needs to be 1, won't be hit in for loops
    cache = [1]+[0 for i in range(amount)]
    for coin in denominations:
        for higher_amount in range(coin, amount+1):
            cache[higher_amount] += cache[higher_amount-coin]
    return cache[amount]


denominations = [1, 5, 10, 25, 50]
print(making_change(10, [1, 5, 10, 25, 50]))

# attempt at recursive solution
# if amount < 0:
#     return 0
# if amount in [0, 1]:
#     return [1]
# if amount in cache:
#     return cache[amount]
# for i, coin in enumerate(denominations):
#     if amount-coin < 0:
#         pass
#     elif amount-coin == 0:
#         return [coin]
#     else:
#         if not -1 in cache:
#             cache[-1] = []
#         cache[-1] += [coin] + \
#             making_change(amount-coin, denominations[i:], cache)
# cache[amount] = cache[-1]
# cache[-1] = []
# return cache[amount]


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
