import unittest
import warnings
from Api import app

class MyAppTest(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "<p>Hello, World!</p>")

    def test_getlicense(self):
        response = self.app.get("/licenses")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("John Doe" in response.data.decode())

    def test_getlicense_by_id(self):
        response = self.app.get("/licenses/4")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("Bob Brown" in response.data.decode())

if __name__ == "__main__":
    unittest.main()
