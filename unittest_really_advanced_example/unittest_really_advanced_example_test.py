import unittest
from unittest.mock import patch
from unittest_really_advanced_example import *


class AnotherMoreComplexServiceTest(unittest.TestCase):

    @patch("unittest_really_advanced_example.SendMailClass")
    @patch("unittest_really_advanced_example.OneService")
    def test_make_magic_method(self, mail_service_mock, first_service_mock):
        first_service_mock.make_things_and_get_result.return_value = 6
        complex_service = AnotherMoreComplexService(mail_service_mock, first_service_mock)

        complex_service.make_complex_bussiness()

        self.assertEqual(1, mail_service_mock.send_mail.call_count)
        self.assertIsNotNone(complex_service.get_magical_number())
        self.assertEqual(4, complex_service.get_magical_number())

if __name__ == '__main__':
    unittest.main()