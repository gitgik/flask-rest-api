import unittest


class BaseTestCase(unittest.TestCase):
    """This base class creates setup and teardown methods."""

    def setUp(self):
        """Define test variables and initialize app."""
        pass

    def tearDown(self):
        """teardown all initialized variables."""
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
