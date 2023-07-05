"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app, COUNTERS

class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()
        COUNTERS.clear()

    def test_create_a_counter(self):
        """It should create a counter"""
        counter = 'foo'
        result = self.client.post(f"/counters/{counter}")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn(counter, data)
        self.assertEqual(data[counter], 0)

    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)

    def test_get_counter(self):
        """It should return a counter and its value"""
        counter = 'foo'
        result = self.client.post(f"/counters/{counter}")
        result = self.client.get(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertIn(counter, data)
        self.assertEqual(data[counter], 0)
    def test_get_nonexisting_counter(self):
        """It should return an error counter does not exist"""
        counter = 'foo'
        result = self.client.get(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('message', data)
        self.assertEqual(data['message'], f"Counter {counter} does not exists")

    def test_update_counter(self):
        """It should increment the counter by one"""
        counter = 'foo'
        result = self.client.post(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(data[counter], 0)
        result = self.client.put(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertIn(counter, data)
        self.assertEqual(data[counter], 1)

    def test_update_nonexistent_counter(self):
        """It should return an error counter does not exist"""
        counter = 'foo'
        result = self.client.put(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('message', data)
        self.assertEqual(data['message'], f"Counter {counter} does not exists")

    def test_delete_counter(self):
        """It should return a counter deleted message"""
        counter = 'foo'
        result = self.client.post(f"/counters/{counter}")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.delete(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)
    def test_delete_nonexisting_counter(self):
        """It should return a counter deleted message"""
        counter = 'foo'
        result = self.client.delete(f"/counters/{counter}")
        data = result.get_json()
        self.assertEqual(result.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn('message', data)
        self.assertEqual(data['message'], f"Counter {counter} does not exist")