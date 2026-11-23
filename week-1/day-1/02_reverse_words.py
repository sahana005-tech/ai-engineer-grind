"""
Reverse the words (Easy)
Week 1 · Day 1 · Python: split / join

Problem:
    Return the words of s in reverse order, separated by single spaces. Ignore extra spaces.
"""

def reverse_words(s):
    words=s.split()
    reversed_words=words[::-1]
    return " ".join(reversed_words)    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = reverse_words('hello world')
    assert _got == 'world hello', f"example 1: got {_got!r}"

    # example 2
    _got = reverse_words('  the sky   is blue ')
    assert _got == 'blue is sky the', f"example 2: got {_got!r}"

    # example 3
    _got = reverse_words('')
    assert _got == '', f"example 3: got {_got!r}"

    print("reverse_words.py: all 3 examples pass")
