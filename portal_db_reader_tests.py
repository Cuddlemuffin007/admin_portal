import unittest
from A_db import DBReader, DBReaderException
from A_db_tests import DBTestCase
from portal_db_reader import PortalDBReader, PortalDBReaderException

class PortalDBReaderTestCase(DBTestCase):

    def test_can_get_by_username(self):
        file_input = ["bkr,admin,brennon rogers", "tst,admin2,test entry"]
        portal_db_reader = PortalDBReader(file_input)
        self.assertEqual(portal_db_reader.get_by_username("bkr"), ["bkr", "admin", "brennon rogers"])

    def test_raises_exception_if_username_not_found(self):
        file_input = ["bkr,admin,brennon rogers"]
        portal_db_reader = PortalDBReader(file_input)
        with self.assertRaises(PortalDBReaderException):
            portal_db_reader.get_by_username("br")

    def test_can_validate_username_and_password(self):
        file_input = ["bkr,admin,brennon rogers", "tst,admin2,test entry"]
        portal_db_reader = PortalDBReader(file_input)
        self.assertTrue(portal_db_reader.validate_user("tst", "admin2"))

    def test_returns_false_while_validating_user_if_username_not_found(self):
        file_input = ["bkr,admin,brennon rogers"]
        portal_db_reader = PortalDBReader(file_input)
        self.assertFalse(portal_db_reader.validate_user("br", "admin"))