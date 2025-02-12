import unittest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover("tests", pattern="test_*.py")
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(tests)
