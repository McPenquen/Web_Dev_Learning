import unittest
import myapp.py as myapp

class TestingTest(unittest.TestCase):
    def test_welcome(self):
        self.app = myapp.app.test.client()
        out = self.app.get('/welcome')
        assert '200 OK' in out.status
        assert 'charset=utf-8' in out.content_type
        assert 'text/html' in out.content_type

if __name__ == "__main__":
    unittest.main()