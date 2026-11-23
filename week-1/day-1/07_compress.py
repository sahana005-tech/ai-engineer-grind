"""
Run-length encoding (Medium)
Week 1 · Day 1 · Python: scan with a 'previous' value

Problem:
    Compress runs of the same character: 'aaabcc' → 'a3b1c2'.
"""

def compress(s):
    if not s:                                       # Line 1: Handle empty string '' immediately
        return ""
    
    parts = []                                      # Line 2: List to collect chunks like 'a3', 'b1' (O(1) append)
    curr_char = s[0]                                # Line 3: Start tracking the very first character
    count = 1                                       # Line 4: Its streak starts at 1
    
    for ch in s[1:]:                                # Line 5: Walk through every character from index 1 onward
        if ch == curr_char:                         # Line 6: Same character as previous?
            count += 1                              # Line 7: Yes -> extend the current streak!
        else:                                       # Line 8: Streak broke! A different character appeared
            parts.append(f"{curr_char}{count}")     # Line 9: Save the finished streak (e.g., 'a3')
            curr_char = ch                          # Line 10: Switch tracker to the new character
            count = 1                               # Line 11: Reset streak count to 1
            
    parts.append(f"{curr_char}{count}")             # Line 12: Flush the final streak left over after the loop
    return "".join(parts)
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = compress('aaabcc')
    assert _got == 'a3b1c2', f"example 1: got {_got!r}"

    # example 2
    _got = compress('a')
    assert _got == 'a1', f"example 2: got {_got!r}"

    # example 3
    _got = compress('')
    assert _got == '', f"example 3: got {_got!r}"

    # example 4
    _got = compress('aabbaa')
    assert _got == 'a2b2a2', f"example 4: got {_got!r}"

    print("compress.py: all 4 examples pass")
