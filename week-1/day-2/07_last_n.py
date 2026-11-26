"""
Keep the last n lines (Easy)
Week 1 · Day 2 · Python: deque(maxlen=n)

Problem:
    Return the last n items of an iterable as a list — like tail -n. Assume you can only loop over it once.
"""

from collections import deque

def last_n(items, n):
    return list(deque(items, maxlen=n))
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = last_n([1,2,3,4,5], 2)
    assert _got == [4,5], f"example 1: got {_got!r}"

    # example 2
    _got = last_n(iter('abc'), 5)
    assert _got == ['a','b','c'], f"example 2: got {_got!r}"

    # example 3
    _got = last_n([], 3)
    assert _got == [], f"example 3: got {_got!r}"

    print("last_n.py: all 3 examples pass")
