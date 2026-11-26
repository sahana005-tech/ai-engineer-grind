"""
Merge inventories (Easy)
Week 1 · Day 2 · Python: Counter arithmetic

Problem:
    Add two inventories (dicts of item → count) together and return a plain dict.
"""

from collections import Counter
def merge(a, b):
    return dict(Counter(a)+Counter(b))
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = merge({'apple':2},{'apple':1,'pear':4})
    assert _got == {'apple':3,'pear':4}, f"example 1: got {_got!r}"

    # example 2
    _got = merge({},{})
    assert _got == {}, f"example 2: got {_got!r}"

    print("merge_counts.py: all 2 examples pass")
