"""
Best time to buy and sell stock (Easy)
Week 1 · Day 1 · DSA: Arrays · running minimum
LeetCode 121: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem:
    prices[i] is the price on day i. Buy one day, sell on a later day. Return the max profit, or 0 if you can't profit.
"""

def max_profit(prices):
    cheapest = float('inf')
    best = 0
    for p in prices:
        cheapest = min(cheapest, p)
        best = max(best, p - cheapest)
    return best
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = max_profit([7,1,5,3,6,4])
    assert _got == 5, f"example 1: got {_got!r}"

    # example 2
    _got = max_profit([7,6,4,3,1])
    assert _got == 0, f"example 2: got {_got!r}"

    # example 3
    _got = max_profit([2,4,1])
    assert _got == 2, f"example 3: got {_got!r}"

    # example 4
    _got = max_profit([1])
    assert _got == 0, f"example 4: got {_got!r}"

    print("lc121_best_time.py: all 4 examples pass")
