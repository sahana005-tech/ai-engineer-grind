"""
The shared-row trap (Medium)
Week 1 · Day 1 · Python: mutability & aliasing

Problem:
    This builds a grid, but changing one cell changes a whole column. Fix it so each row is its own list.
    def make_grid(rows, cols):
        return [[0] * cols] * rows
"""

def make_grid(rows, cols):
    
        
    
    return [[0] * cols for _ in range(rows)]


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    g = make_grid(3, 2)
    g[0][0] = 9
    _got = g
    assert _got == [[9,0],[0,0],[0,0]], f"example 1: got {_got!r}"

    # example 2
    _got = make_grid(2, 3)
    assert _got == [[0,0,0],[0,0,0]], f"example 2: got {_got!r}"

    # example 3
    _got = make_grid(0, 3)
    assert _got == [], f"example 3: got {_got!r}"

    print("make_grid.py: all 3 examples pass")
