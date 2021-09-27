# Modified by Paul Lu, 2021
# Originally By Ali Gharari, 2020
# Assumes unfairDice.py is in current working directory

import unfairDice
import sys

if __name__ == "__main__":
    print("*************************************************", file=sys.stderr)
    print("test9", file=sys.stderr)
    prob_list = [1/4, 1/16, 3/16, 1/8, 1/8, 1/16, 2/16, 1/32, 1/32]
    seed = 42
    n = 10000
    print(unfairDice.biased_rolls(prob_list, seed, n))
