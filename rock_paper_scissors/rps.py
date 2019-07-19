#!/usr/bin/python

import sys

"""
recursion function is key now

expect recursion_rps([['rock'], ['paper'], ['scissors']]) 
:= [['rock', 'rock'], 
	['rock', 'paper'], 
	['rock', 'scissors'], 
	['paper', 'rock'], 
	['paper', 'paper'], 
	['paper', 'scissors'], 
	['scissors', 'rock'], 
	['scissors', 'paper'], 
	['scissors', 'scissors']]

each recursive result goes up by three -- for each of the original rps,
return an array filled with 
"""


def recursion_rps(moves):

    updated_moves = []
    for start in [['rock'], ['paper'], ['scissors']]:
        for rest in moves:
            updated_moves.append(start+rest)
    return updated_moves


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    moves = [['rock'], ['paper'], ['scissors']]
    while n > 1:
        moves = recursion_rps(moves)
        n -= 1
    return moves

# current complexity of O(n^2): reduce by using a cache system? or go iterative


print(rock_paper_scissors(3))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
