"""
Second largest (Medium)
Week 1 · Day 1 · Python: single pass, track two values

Problem:
    Return the second largest distinct number, or None if there isn't one. Don't sort.
"""

def second_largest(nums):
    first = None                                    # Line 1: Tracks the largest number seen so far
    second = None                                   # Line 2: Tracks the 2nd largest distinct number so far
    
    for x in nums:                                  # Line 3: Visit every number in one O(n) pass
        if x == first or x == second:               # Line 4: Duplicate of a number already on our podium?
            continue                                # Line 5: Skip it so both podium spots stay distinct
            
        if first is None or x > first:              # Line 6: New 1st place champion!
            second = first                          # Line 7: Demote the old 1st place down to 2nd place
            first = x                               # Line 8: Crown x as the new 1st place
        elif second is None or x > second:          # Line 9: Didn't beat 1st, so check if it beats 2nd place
            second = x                              # Line 10: Update 2nd place (1st place stays untouched)
            
    return second
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = second_largest([3,1,4,4,2])
    assert _got == 3, f"example 1: got {_got!r}"

    # example 2
    _got = second_largest([5,5])
    assert _got == None, f"example 2: got {_got!r}"

    # example 3
    _got = second_largest([1])
    assert _got == None, f"example 3: got {_got!r}"

    # example 4
    _got = second_largest([-2,-1])
    assert _got == -2, f"example 4: got {_got!r}"

    print("second_largest.py: all 4 examples pass")
