import unittest
from app import check_dns, check_https


class TestReadinessChecker(unittest.TestCase):

    def test_dns_success(self):
        success, ip_address = check_dns("example.com")
        self.assertTrue(success)
        self.assertIsNotNone(ip_address)

    def test_dns_failure(self):
        success, ip_address = check_dns("this-domain-should-not-exist.invalid")
        self.assertFalse(success)
        self.assertIsNone(ip_address)

    def test_https_success(self):
        success, status = check_https("https://example.com")
        self.assertTrue(success)
        self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()
