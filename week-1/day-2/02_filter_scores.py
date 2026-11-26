"""
Filter with a dict comprehension (Easy)
Week 1 · Day 2 · Python: dict comprehension

Problem:
    Return only the students who scored at least cutoff.
"""

def passed(scores, cutoff):
    return {k:v for k,v in scores.items() if v>=cutoff}
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = passed({'asha':72,'ravi':40,'bina':90}, 50)
    assert _got == {'asha':72,'bina':90}, f"example 1: got {_got!r}"

    # example 2
    _got = passed({}, 10)
    assert _got == {}, f"example 2: got {_got!r}"

    # example 3
    _got = passed({'x':50}, 50)
    assert _got == {'x':50}, f"example 3: got {_got!r}"

    print("filter_scores.py: all 3 examples pass")
