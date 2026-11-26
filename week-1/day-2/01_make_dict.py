"""
Zip into a dict (Easy)
Week 1 · Day 2 · Python: dict(zip(...))

Problem:
    Build a dict from a list of keys and a list of values. If the lists differ in length, stop at the shorter one.
"""

def make_dict(keys, values):
    return dict(zip(keys,values))
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = make_dict(['a','b'],[1,2])
    assert _got == {'a':1,'b':2}, f"example 1: got {_got!r}"

    # example 2
    _got = make_dict(['a','b','c'],[1])
    assert _got == {'a':1}, f"example 2: got {_got!r}"

    # example 3
    _got = make_dict([],[])
    assert _got == {}, f"example 3: got {_got!r}"

    print("make_dict.py: all 3 examples pass")
