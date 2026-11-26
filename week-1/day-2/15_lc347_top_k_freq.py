"""
Top k frequent elements (Medium)
Week 1 · Day 2 · DSA: Hashing · bucket sort
LeetCode 347: https://leetcode.com/problems/top-k-frequent-elements/

Problem:
    Return the k most frequent numbers, most frequent first (ties: smaller number first).
"""

from collections import Counter
def top_k_frequent(nums, k):
    counts=Counter(nums)
    return sorted(counts, key=lambda x: (-counts[x], x))[:k]
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = top_k_frequent([1,1,1,2,2,3], 2)
    assert _got == [1,2], f"example 1: got {_got!r}"

    # example 2
    _got = top_k_frequent([1], 1)
    assert _got == [1], f"example 2: got {_got!r}"

    # example 3
    _got = top_k_frequent([4,4,5,5,6], 2)
    assert _got == [4,5], f"example 3: got {_got!r}"

    print("lc347_top_k_freq.py: all 3 examples pass")
