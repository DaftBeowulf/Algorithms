#!/usr/bin/python

import sys

"""
eating_cookies(n=3):
	possible options are 1,2, or 3 cookies at a time
	spawn a recursion tree based on how many options can work

							3 cookies
					|	      |          |
					eat1    eat2        eat3
               2 cookies   1 cookie     0 cookies
			   |       |         |       done
              eat1    eat2     eat1
		     1 left  0 left   0 left
			  |       done     done
			  eat1
			  0 left
			  done

	each possible path that ends in a base case increments the ways they can be eaten
	here, that number is 4

	base case:
	if n=0, increment ways by 1

	otherwise, call recursive method for each possible amount
	BUT
	store the results for a specific n in a cache, since if n=4, eat2 tree could pop up multiple times

"""

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=[]):
    if cache == []:
        cache = [0 for i in range(n+1)]
    if n < 0:
        return 0
    if 0 <= n <= 1:
        return 1
    if cache[n] > 0:
        return cache[n]
    else:
        for i in range(1, 4):
            if n-i > 0:
                cache[n] += eating_cookies(n-i, cache)
            elif n-i == 0:
                cache[n] += 1

    return cache[n]

# O(n) since each possible eating_cookies(n) only gets run once for each value of n
# possible ways to improve: an iterative solution, or a bottom-up iterative solution?


print("there are", eating_cookies(4), "ways of eating the cookies")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
