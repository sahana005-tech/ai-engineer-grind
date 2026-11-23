"""
Transpose a matrix (Medium)
Week 1 · Day 1 · Python: zip(*rows)

Problem:
    Return the transpose of a matrix (rows become columns) as a list of lists.
"""

def transpose(m):
    return [list(col) for col in zip(*m)]
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = transpose([[1,2,3],[4,5,6]])
    assert _got == [[1,4],[2,5],[3,6]], f"example 1: got {_got!r}"

    # example 2
    _got = transpose([[1]])
    assert _got == [[1]], f"example 2: got {_got!r}"

    # example 3
    _got = transpose([])
    assert _got == [], f"example 3: got {_got!r}"

    print("transpose.py: all 3 examples pass")
