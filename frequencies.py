"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        item = str(i)
        if (item in frequencies.keys()):
            frequencies[item] += 1
        else:
            frequencies[item] = 1
    return frequencies
