
import unittest
from app import app

class TestLMS(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Learning Management System", response.data)

    def test_course_list(self):
        response = self.client.get("/courses")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Python Programming", response.data)

    def test_courses_api(self):
        response = self.client.get("/api/courses")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 3)

if __name__ == "__main__":
    unittest.main()
