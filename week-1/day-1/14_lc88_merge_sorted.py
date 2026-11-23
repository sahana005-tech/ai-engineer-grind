"""
Merge two sorted lists (Easy)
Week 1 · Day 1 · DSA: Two pointers
LeetCode 88: https://leetcode.com/problems/merge-sorted-array/

Problem:
    Merge two sorted lists into one sorted list without calling sorted().
"""

def merge_sorted(a, b):
    p1=0
    p2=0
    result=[]
    
    while p1 < len(a) and p2<len(b):
        if a[p1] < b[p2]:
            result.append(a[p1])
            p1+=1
        else:
            result.append(b[p2])
            p2+=1
    result.extend(a[p1:])
    result.extend(b[p2:])
    return result
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = merge_sorted([1,2,3],[2,5,6])
    assert _got == [1,2,2,3,5,6], f"example 1: got {_got!r}"

    # example 2
    _got = merge_sorted([],[1])
    assert _got == [1], f"example 2: got {_got!r}"

    # example 3
    _got = merge_sorted([4,5],[1,2,3])
    assert _got == [1,2,3,4,5], f"example 3: got {_got!r}"

    print("lc88_merge_sorted.py: all 3 examples pass")
