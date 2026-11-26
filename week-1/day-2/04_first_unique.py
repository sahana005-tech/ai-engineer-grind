"""
First unique character (Easy)
Week 1 · Day 2 · Python: count first, then scan

Problem:
    Return the index of the first character that appears exactly once, or -1.
"""

from collections import Counter

def first_unique(s):
    count=Counter(s)
    for i,ch in enumerate(s):
        if count[ch]==1:
            return i
    return -1
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = first_unique('leetcode')
    assert _got == 0, f"example 1: got {_got!r}"

    # example 2
    _got = first_unique('loveleetcode')
    assert _got == 2, f"example 2: got {_got!r}"

    # example 3
    _got = first_unique('aabb')
    assert _got == -1, f"example 3: got {_got!r}"

    print("first_unique.py: all 3 examples pass")
