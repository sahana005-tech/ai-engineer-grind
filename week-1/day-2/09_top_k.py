"""
Top k words (Medium)
Week 1 · Day 2 · Python: sort with a tuple key

Problem:
    Return the k most common words (lowercase). Break ties alphabetically.
"""

from collections import Counter 
def top_k(text, k):
    counts=Counter(text.lower().split())
    return sorted(counts, key=lambda w: (-counts[w], w))[:k]
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = top_k('the cat the dog the cat', 2)
    assert _got == ['the','cat'], f"example 1: got {_got!r}"

    # example 2
    _got = top_k('b a c', 2)
    assert _got == ['a','b'], f"example 2: got {_got!r}"

    # example 3
    _got = top_k('A a b', 1)
    assert _got == ['a'], f"example 3: got {_got!r}"

    print("top_k.py: all 3 examples pass")
