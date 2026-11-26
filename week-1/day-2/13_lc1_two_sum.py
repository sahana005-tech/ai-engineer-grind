"""
Two sum (Medium)
Week 1 · Day 2 · DSA: Hashing · hash map
LeetCode 1: https://leetcode.com/problems/two-sum/

Problem:
    Return indices [i, j] (i < j) of the two numbers that add up to target. Exactly one answer exists.
"""

def two_sum(nums, target):
    seen = {}  # value -> index
    for j, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], j]
        seen[x] = j
      
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = two_sum([2,7,11,15], 9)
    assert _got == [0,1], f"example 1: got {_got!r}"

    # example 2
    _got = two_sum([3,2,4], 6)
    assert _got == [1,2], f"example 2: got {_got!r}"

    # example 3
    _got = two_sum([3,3], 6)
    assert _got == [0,1], f"example 3: got {_got!r}"

    print("lc1_two_sum.py: all 3 examples pass")
