import unittest
from unittest.mock import patch

from unittest_advanced_example import *


class LogicClassTest(unittest.TestCase):

    @patch( "unittest_advanced_example.SendMailClass", autospec=True)
    def test_bussiness_method(self, mail_service_mock):
        logic_object = LogicClass(mail_service_mock)

        self.assertFalse(logic_object.is_business_done())
        logic_object.make_some_bussiness()
        self.assertTrue(logic_object.is_business_done())

        self.assertEqual(1, mail_service_mock.send_mail.call_count)
        mail_service_mock.send_mail.assert_called_once_with('Negocio hecho el día 2018-09-12')


if __name__ == '__main__':
    unittest.main()