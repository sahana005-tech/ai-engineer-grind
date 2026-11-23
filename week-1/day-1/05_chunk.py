"""
Split into chunks (Easy)
Week 1 · Day 1 · Python: range with a step

Problem:
    Split lst into lists of size n. The last chunk may be shorter.
"""

def chunk(lst, n):
    result=[]
    
    for i in range(0,len(lst),n):
        result.append(lst[i : i+n])
    return result
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = chunk([1,2,3,4,5], 2)
    assert _got == [[1,2],[3,4],[5]], f"example 1: got {_got!r}"

    # example 2
    _got = chunk([1,2,3], 3)
    assert _got == [[1,2,3]], f"example 2: got {_got!r}"

    # example 3
    _got = chunk([], 4)
    assert _got == [], f"example 3: got {_got!r}"

    print("chunk.py: all 3 examples pass")
