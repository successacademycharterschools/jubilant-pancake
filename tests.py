"""Test for our Edit distance app."""
import json
from app import app
from unittest import main, TestCase

from wfdistance import distance


class AppTestCase(TestCase):
    """Test Suite for the Flask app."""

    def setUp(self):
        """Standard setup."""
        self.app = app.test_client()

    def test_invalid_api_call_get(self):
        """Test bad GET call to the 'API'."""
        response = self.app.get("/api/v1/distance")
        assert "Method Not Allowed" in response.data
        self.assertEqual(response.status_code, 405)

    def test_invalid_api_call_post(self):
        """Test bad POST call to the 'API'."""
        data = dict(
            first="abc",
            second="def",
        )
        response = self.app.post("/api/v1/distance", data=data)
        assert "your request must be in JSON" in response.data
        self.assertEqual(response.status_code, 400)

    def test_proper_api_call_post(self):
        """Test proper POST call to the 'API'."""
        data = dict(
            first="abc",
            second="def",
        )
        response = self.app.post("/api/v1/distance",
                                 headers={"content-type": "application/json"},
                                 content_type="application/json",
                                 data=json.dumps(data))
        res = json.loads(response.data)
        self.assertEqual(res["distance"], 3)


class EditDistanceTestCase(TestCase):
    """Unit tests for the edit distance."""

    def test_empty_strings(self):
        """Test various cases of empty strings."""
        self.assertEqual(distance("abc", ""), 3)
        self.assertEqual(distance("", "abc"), 3)
        self.assertEqual(distance("", "a"), 1)
        self.assertEqual(distance("a", ""), 1)
        self.assertEqual(distance("", ""), 0)

    def test_same_strings(self):
        """Test case of same strings."""
        self.assertEqual(distance("abc", "abc"), 0)

    def test_diff_strings(self):
        """Test various cases of strings of different lengths."""
        self.assertEqual(distance("abc", "abcd"), 1)
        self.assertEqual(distance("abc", "abd"), 1)
        self.assertEqual(distance("abc", "bc"), 1)
        self.assertEqual(distance("abc", "bcd"), 2)
        self.assertEqual(distance("bcd", "abc"), 2)
        self.assertEqual(distance("abc", "eabf"), 2)
        self.assertEqual(distance("abc", "a"), 2)
        self.assertEqual(distance("c", "abc"), 2)
        self.assertEqual(distance("abcde", "bcdze"), 2)
        self.assertEqual(distance("abcde", "axdfe"), 3)
        self.assertEqual(distance("axdfe", "abcde"), 3)

if __name__ == "__main__":
    main()
