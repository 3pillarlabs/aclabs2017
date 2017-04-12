import unittest

def flatten(seq, levels=1):
    if levels == 0:
        return seq

    acc = []
    for elem in seq:
        if isinstance(elem, list):
            acc += elem
        else:
            acc += [elem]

    return flatten(acc, levels -1)

class TestFlatten(unittest.TestCase):
    def test_empty(self):
        self.assertItemsEqual(flatten([]), [])

    def test_simple(self):
        self.assertItemsEqual(flatten([1]), [1])

    def test_two_layers(self):
        self.assertItemsEqual(flatten([1, [2]]), [1, 2])
