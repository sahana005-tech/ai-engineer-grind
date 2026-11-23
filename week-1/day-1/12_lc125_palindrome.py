"""
Valid palindrome (Easy)
Week 1 · Day 1 · DSA: Two pointers
LeetCode 125: https://leetcode.com/problems/valid-palindrome/

Problem:
    Return True if s reads the same forwards and backwards, considering only letters and digits and ignoring case.
"""

def is_palindrome(s):
    left=0
    right=len(s)-1
    
    
    while left<right:
        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1
        elif s[left].lower()!=s[right].lower():
            return False
            break
        else:
            left+=1
            right-=1
    return True
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = is_palindrome('A man, a plan, a canal: Panama')
    assert _got == True, f"example 1: got {_got!r}"

    # example 2
    _got = is_palindrome('race a car')
    assert _got == False, f"example 2: got {_got!r}"

    # example 3
    _got = is_palindrome('')
    assert _got == True, f"example 3: got {_got!r}"

    # example 4
    _got = is_palindrome('0P')
    assert _got == False, f"example 4: got {_got!r}"

    print("lc125_palindrome.py: all 4 examples pass")
