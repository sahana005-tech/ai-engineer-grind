"""
Count the vowels (Easy)
Week 1 · Day 1 · Python: loop + membership test

Problem:
    Return how many vowels (a, e, i, o, u — any case) are in s.
"""

def count_vowels(s):
    count=0
    for c in s.lower():
        if c in 'aeiou':
            count+=1
    return count
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = count_vowels('Hello World')
    assert _got == 3, f"example 1: got {_got!r}"

    # example 2
    _got = count_vowels('rhythm')
    assert _got == 0, f"example 2: got {_got!r}"

    # example 3
    _got = count_vowels('AEIOU')
    assert _got == 5, f"example 3: got {_got!r}"

    # example 4
    _got = count_vowels('')
    assert _got == 0, f"example 4: got {_got!r}"

    print("count_vowels.py: all 4 examples pass")
