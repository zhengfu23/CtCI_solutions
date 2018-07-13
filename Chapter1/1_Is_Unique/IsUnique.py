"""Implement an algorithm to determine if a string has all unique characters. """
import unittest


def unique(string):
    # The string can't be unique if it's longer than the amount of unique chars.
    # Assuming character set is ASCII (128 characters total)
    if len(string) > 128:
        return False

    # Make array of length 128 with Falses to indicate whether
    # the corresponding character has appeared.
    char_set = [False for _ in range(128)]
    for char in string:
        index = ord(char)
        if char_set[index]:
            return False
        char_set[index] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)

        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
