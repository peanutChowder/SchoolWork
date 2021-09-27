# Modified by Paul Lu, 2021
# Copyright By Ali Gharari, Paul Lu, 2020
# Assumes unfairDice.py is in current working directory.

import unfairDice
import sys


if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test11", file=sys.stderr)
    rolls = [3, 2, 3, 2, 3, 3, 4, 6, 2, 6, 3, 2, 6, 2, 5, 5, 3, 4, 4, 2]
    unfairDice.draw_histogram(6, rolls, 50)
