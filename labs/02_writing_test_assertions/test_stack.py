from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.assertEqual(True, self.stack.is_empty())
        self.stack.push(10)
        self.assertEqual(False, self.stack.is_empty())

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(10)
        self.assertEqual(10, self.stack.pop())
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(10)
        self.stack.push(33)
        self.assertEqual(33, self.stack.peek())

    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertFalse(self.stack.is_empty())
        self.stack.push(10)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())
