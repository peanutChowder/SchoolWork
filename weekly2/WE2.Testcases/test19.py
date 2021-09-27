# Modified by Paul Lu, 2021
# Copyright By Ali Gharari, Paul Lu, 2020
# Assumes unfairDice.py is in current working directory.

import unfairDice
import sys


if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test19", file=sys.stderr)
    rolls = [1,1,1,1,1]
    unfairDice.draw_histogram(1, rolls, 5)
