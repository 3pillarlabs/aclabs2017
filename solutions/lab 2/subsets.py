import unittest


def subsets(seq, sol=None):
    sol = sol or [set()]
    if not seq:
        return sol
    else:
        new_solutions = [{seq[0]}] + [s | {seq[0]} for s in sol]
        unique = []
        for s in sol + new_solutions:
            if s not in unique:
                unique += [s]
        return subsets(seq[1:], unique)


class TestSubset(unittest.TestCase):
    def test_void(self):
        self.assertListEqual(subsets([]), [set()])

    def test_simple(self):
        self.assertItemsEqual(subsets([1, 2, 3]),
                             [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}])
