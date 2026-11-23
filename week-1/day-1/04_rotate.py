"""
Rotate a list (Easy)
Week 1 · Day 1 · Python: slicing + modulo

Problem:
    Return a new list with nums rotated right by k steps. k can be bigger than the length.
"""

def rotate(nums, k):
    if not nums:                        # Line 1: Handle empty list [] immediately (avoids divide-by-zero)
        return []
    
    k = k % len(nums)                   # Line 2: Shrink huge k down to effective steps (e.g., 4 % 3 -> 1)
    if k == 0:                          # Line 3: If 0 effective steps, return a shallow copy as-is
        return nums[:]
        
    return nums[-k:] + nums[:-k]
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = rotate([1,2,3,4,5], 2)
    assert _got == [4,5,1,2,3], f"example 1: got {_got!r}"

    # example 2
    _got = rotate([1,2,3], 4)
    assert _got == [3,1,2], f"example 2: got {_got!r}"

    # example 3
    _got = rotate([], 3)
    assert _got == [], f"example 3: got {_got!r}"

    # example 4
    _got = rotate([7], 0)
    assert _got == [7], f"example 4: got {_got!r}"

    print("rotate.py: all 4 examples pass")
