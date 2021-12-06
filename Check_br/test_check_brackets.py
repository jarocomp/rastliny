import unittest
import check_brackets

class TestCheck_brackets(unittest.TestCase):
    def test_check_brackets(self):
        res = check_brackets.check('{[]{()}}')
        assert res == 'Matched'

    def test_check_brackets2(self):
        res = check_brackets.check('[(){}([{}{}{}])]')
        assert res == 'Matched'

    def test_check_brackets3(self):
        res = check_brackets.check('[({{{)]')
        assert res == 'Unmatched'

