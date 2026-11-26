"""
Contains duplicate (Easy)
Week 1 · Day 2 · DSA: Hashing · set
LeetCode 217: https://leetcode.com/problems/contains-duplicate/

Problem:
    Return True if any value appears at least twice.
"""

def contains_duplicate(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = contains_duplicate([1,2,3,1])
    assert _got == True, f"example 1: got {_got!r}"

    # example 2
    _got = contains_duplicate([1,2,3,4])
    assert _got == False, f"example 2: got {_got!r}"

    # example 3
    _got = contains_duplicate([])
    assert _got == False, f"example 3: got {_got!r}"

    print("lc217_contains_dup.py: all 3 examples pass")
