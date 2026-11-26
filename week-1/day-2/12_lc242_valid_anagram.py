"""
Valid anagram (Easy)
Week 1 · Day 2 · DSA: Hashing · counting
LeetCode 242: https://leetcode.com/problems/valid-anagram/

Problem:
    Return True if t uses exactly the same letters as s (same counts).
"""

from collections import Counter
def is_anagram(s, t):
    return Counter(s)==Counter(t)
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = is_anagram('anagram','nagaram')
    assert _got == True, f"example 1: got {_got!r}"

    # example 2
    _got = is_anagram('rat','car')
    assert _got == False, f"example 2: got {_got!r}"

    # example 3
    _got = is_anagram('aab','abb')
    assert _got == False, f"example 3: got {_got!r}"

    # example 4
    _got = is_anagram('','')
    assert _got == True, f"example 4: got {_got!r}"

    print("lc242_valid_anagram.py: all 4 examples pass")
