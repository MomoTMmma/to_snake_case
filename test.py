import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('helpIWantToBeInCamelCase'), 'help_i_want_to_be_in_camel_case')

    def test_2(self):
        self.assertEqual(solution("codingTemple"), "coding_temple")

    def test_3(self):
        self.assertEqual(solution("thisIsATestCase"), "this_is_a_test_case")

    def test_4(self):
        self.assertEqual(solution("thisIsAnotherTest"), "this_is_another_test")


if __name__ == "__main__":
    unittest.main()