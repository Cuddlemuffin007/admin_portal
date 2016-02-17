import unittest
from unittest import mock
from portal_db_reader import PortalDBReader, PortalDBReaderException
from user import User


class UserTestCase(unittest.TestCase):

    def test_can_init_with_username_and_password(self):
        user = User("bkr", "admin")
        self.assertEqual(user.username, "bkr")
        self.assertEqual(user.password, "admin")

    def test_user_can_login_with_username_and_password(self):
        user = User("bkr", "admin")
        file_input = ["bkr,admin,brennon rogers"]
        portal_db_reader = PortalDBReader(file_input)
        self.assertTrue(user.login(portal_db_reader))

    def test_login_fails_and_returns_false_with_invalid_username_or_password(self):
        user1 = User("br", "admin")
        user2 = User("tst", "wrongpass")
        file_input = ["bkr,admin,brennon rogers", "tst,admin2,test entry"]
        portal_db_reader = PortalDBReader(file_input)
        self.assertFalse(user1.login(portal_db_reader))
        self.assertFalse(user2.login(portal_db_reader))

    @mock.patch('builtins.input', lambda x: x.lower()[:-2])
    def test_user_may_define_a_new_user(self):
        user = User("bkr", "admin")
        self.assertEqual(user.create_new_user(), "username,password,full name")