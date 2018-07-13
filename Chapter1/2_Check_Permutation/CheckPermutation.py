""" Given two strings, check if one is the permutation of the other.
    input: two strings
    output: boolean

    ex: "abcd" and "cbad" ==> True
        "abcd" and "bcde" ==> False
"""


from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
