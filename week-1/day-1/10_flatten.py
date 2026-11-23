"""
Flatten nested lists (Hard)
Week 1 · Day 1 · Python: recursion

Problem:
    Flatten a list nested to any depth: [1,[2,[3,[4]]]] → [1,2,3,4].
"""

def flatten(nested):
    out = []
    for item in nested:
        if isinstance(item, list):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = flatten([1,[2,[3,[4]]]])
    assert _got == [1,2,3,4], f"example 1: got {_got!r}"

    # example 2
    _got = flatten([])
    assert _got == [], f"example 2: got {_got!r}"

    # example 3
    _got = flatten([[],[[]],5])
    assert _got == [5], f"example 3: got {_got!r}"

    # example 4
    _got = flatten(['ab',[1]])
    assert _got == ['ab',1], f"example 4: got {_got!r}"

    print("flatten.py: all 4 examples pass")
