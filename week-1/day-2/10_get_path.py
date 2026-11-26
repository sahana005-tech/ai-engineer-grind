"""
Safe nested lookup (Medium)
Week 1 · Day 2 · Python: dict.get chain

Problem:
    Return the value at a dotted path like 'user.address.city', or default if any part is missing.
"""

def get_path(d, path, default=None):
    cur = d
    for key in path.split('.'):
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = get_path({'user':{'address':{'city':'Mysuru'}}}, 'user.address.city')
    assert _got == 'Mysuru', f"example 1: got {_got!r}"

    # example 2
    _got = get_path({'user':{}}, 'user.address.city', 'n/a')
    assert _got == 'n/a', f"example 2: got {_got!r}"

    # example 3
    _got = get_path({'a':1}, 'a.b')
    assert _got == None, f"example 3: got {_got!r}"

    # example 4
    _got = get_path({'a':0}, 'a', 5)
    assert _got == 0, f"example 4: got {_got!r}"

    print("get_path.py: all 4 examples pass")
