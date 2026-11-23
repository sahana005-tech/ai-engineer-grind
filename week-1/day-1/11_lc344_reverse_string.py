"""
Reverse a string in place (Easy)
Week 1 · Day 1 · DSA: Two pointers
LeetCode 344: https://leetcode.com/problems/reverse-string/

Problem:
    s is a list of characters. Reverse it in place (change the list itself, return nothing). Don't use reverse() or slicing.
"""

def reverse_string(s):
    left=0
    right=len(s)-1
    
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1
    return s
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    s = list('hello')
    reverse_string(s)
    _got = s
    assert _got == list('olleh'), f"example 1: got {_got!r}"

    # example 2
    s = list('ab')
    reverse_string(s)
    _got = s
    assert _got == ['b','a'], f"example 2: got {_got!r}"

    # example 3
    s = []
    reverse_string(s)
    _got = s
    assert _got == [], f"example 3: got {_got!r}"

    print("lc344_reverse_string.py: all 3 examples pass")
