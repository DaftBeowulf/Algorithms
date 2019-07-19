#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batches = math.inf

    for item in recipe:
        if not item in ingredients:
            return 0
        if recipe[item] <= ingredients[item]:

            b = ingredients[item]//recipe[item]

            if b < batches:
                batches = b
    return batches

# first pass: O(n) right now, but can be optimized by reducing dict lookups and computations somehow?


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
