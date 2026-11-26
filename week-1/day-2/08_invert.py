"""
Invert a dict (Medium)
Week 1 · Day 2 · Python: defaultdict(list)

Problem:
    Turn {key: value} into {value: [keys...]} with each list sorted.
"""

from collections import defaultdict
def invert(d):
    out = defaultdict(list)
    for k, v in d.items():
        out[v].append(k)
    return {v: sorted(ks) for v, ks in out.items()}
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = invert({'a':1,'b':2,'c':1})
    assert _got == {1:['a','c'],2:['b']}, f"example 1: got {_got!r}"

    # example 2
    _got = invert({})
    assert _got == {}, f"example 2: got {_got!r}"

    print("invert.py: all 2 examples pass")
