import unittest

class TestFirstTest(unittest.TestCase):
    """
    I am making first contacts with unittest and testing generally after a long time
    """
    def test_upper(self):
        """ test if the upper string method works as expected """
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        """ test if string is in uppercase """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """ test if string split works as expected """
        s = "hello world"
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()