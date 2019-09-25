from module_testing.FooBar import foobarqix
import unittest

class TestFooBar(unittest.TestCase):
    def test_foobar(self):
        assert foobarqix(3) == "FooFoo"
        assert foobarqix(11) == 12
        assert foobarqix(35) == "BarFooBar"
        assert not foobarqix(12) == 11


if __name__ == '__main__':
    unittest.main()