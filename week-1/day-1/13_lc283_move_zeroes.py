"""
Move zeroes to the end (Easy)
Week 1 · Day 1 · DSA: Two pointers
LeetCode 283: https://leetcode.com/problems/move-zeroes/

Problem:
    Return the list with all zeros moved to the end, keeping the order of the other numbers.
"""

def move_zeroes(nums):
    nums = nums[:]
    write = 0
    for x in nums:
        if x != 0:
            nums[write] = x
            write += 1
    for i in range(write, len(nums)):
        nums[i] = 0
    return nums
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = move_zeroes([0,1,0,3,12])
    assert _got == [1,3,12,0,0], f"example 1: got {_got!r}"

    # example 2
    _got = move_zeroes([0])
    assert _got == [0], f"example 2: got {_got!r}"

    # example 3
    _got = move_zeroes([])
    assert _got == [], f"example 3: got {_got!r}"

    print("lc283_move_zeroes.py: all 3 examples pass")
