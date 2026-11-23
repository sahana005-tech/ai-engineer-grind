"""
Capitalise each word (Easy)
Week 1 · Day 1 · Python: split, transform, join

Problem:
    Capitalise the first letter of every word and lowercase the rest: 'hELLO wORLD' → 'Hello World'. Words are separated by single spaces.
"""

def title_case(s):
    words=s.split(" ")
    cap_word=[]
    
    for word in words:
        cap_word.append(word.capitalize())
        
    return " ".join(cap_word)
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = title_case('hELLO wORLD')
    assert _got == 'Hello World', f"example 1: got {_got!r}"

    # example 2
    _got = title_case('python')
    assert _got == 'Python', f"example 2: got {_got!r}"

    # example 3
    _got = title_case('')
    assert _got == '', f"example 3: got {_got!r}"

    # example 4
    _got = title_case('a b c')
    assert _got == 'A B C', f"example 4: got {_got!r}"

    print("title_case.py: all 4 examples pass")
