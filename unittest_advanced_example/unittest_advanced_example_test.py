import unittest
from unittest_advanced_example import *


class LogicClassTest(unittest.TestCase):

    def test_bussiness_method(self):
        mail_service = SendMailClass()
        logic_object = LogicClass(mail_service)

        self.assertFalse(logic_object.is_business_done())

        logic_object.make_some_bussiness()

        self.assertTrue(logic_object.is_business_done())


if __name__ == '__main__':
    unittest.main()