"""
Common elements (Easy)
Week 1 · Day 2 · Python: set intersection

Problem:
    Return a sorted list of the unique values that appear in both lists.
"""

def common(a, b):
    return sorted(set(a)&set(b))
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = common([1,2,2,3],[2,3,4])
    assert _got == [2,3], f"example 1: got {_got!r}"

    # example 2
    _got = common([1],[2])
    assert _got == [], f"example 2: got {_got!r}"

    # example 3
    _got = common([],[1])
    assert _got == [], f"example 3: got {_got!r}"

    print("common.py: all 3 examples pass")
