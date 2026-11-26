"""
Letter frequencies (Easy)
Week 1 · Day 2 · Python: Counter

Problem:
    Return a dict counting each letter in s, lowercased. Ignore everything that isn't a letter.
"""

from collections import Counter
def char_freq(s):
    
    return dict(Counter(c.lower() for c in s if c.isalpha()))

    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = char_freq('Hello!')
    assert _got == {'h':1,'e':1,'l':2,'o':1}, f"example 1: got {_got!r}"

    # example 2
    _got = char_freq('123')
    assert _got == {}, f"example 2: got {_got!r}"

    # example 3
    _got = char_freq('AaA')
    assert _got == {'a':3}, f"example 3: got {_got!r}"

    print("char_freq.py: all 3 examples pass")
