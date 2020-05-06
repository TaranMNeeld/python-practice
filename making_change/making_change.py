#!/usr/bin/python

import sys


def making_change(amount, denominations):
    ways_to_make_change = []
    change = {}

    for denomination in denominations:
        change[denomination] = 0

    # def calculate_remainder(remainder):
    for denomination in denominations:
        remainder = amount % denomination
        if remainder == 0:
            current_change = change.copy()
            current_change[denomination] = amount / denomination
            ways_to_make_change.append(current_change)
            print(ways_to_make_change)

    return ways_to_make_change


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
