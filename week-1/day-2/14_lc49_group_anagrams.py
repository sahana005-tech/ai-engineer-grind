"""
Group anagrams (Medium)
Week 1 · Day 2 · DSA: Hashing · grouping
LeetCode 49: https://leetcode.com/problems/group-anagrams/

Problem:
    Group words that are anagrams of each other. Sort each group, and return the groups sorted.
"""

from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups[''.join(sorted(w))].append(w)
    return sorted(sorted(g) for g in groups.values())
    
    pass


if __name__ == "__main__":
    import os, tempfile
    os.chdir(tempfile.mkdtemp())  # examples that write files do it in a temp folder

    # example 1
    _got = group_anagrams(['eat','tea','tan','ate','nat','bat'])
    assert _got == [['ate','eat','tea'],['bat'],['nat','tan']], f"example 1: got {_got!r}"

    # example 2
    _got = group_anagrams([''])
    assert _got == [['']], f"example 2: got {_got!r}"

    # example 3
    _got = group_anagrams([])
    assert _got == [], f"example 3: got {_got!r}"

    print("lc49_group_anagrams.py: all 3 examples pass")
