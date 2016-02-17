import unittest
from unittest import mock
from A_db import DBReader, DBReaderException


# Read contents from a file (csv)
# Find something in-memory "file"
# Show it to the user

class DBTestCase(unittest.TestCase):

    def test_db_reader_can_format_expected_file_structure(self):
        expected_input = ["joel taddei,32,205", "peanut,77,18"]
        expected_output = [["joel taddei", "32", "205"], ["peanut", "77", "18"]]
        db_reader = DBReader()
        self.assertEqual(db_reader.clean_file(expected_input), expected_output)

    def test_db_reader_can_format_expected_file_structure_in_init(self):
        expected_input = ["joel taddei,32,205", "peanut,77,18"]
        expected_output = [["joel taddei", "32", "205"], ["peanut", "77", "18"]]
        db_reader = DBReader(expected_input)
        self.assertEqual(db_reader.cleaned_data, expected_output)

    def test_db_reader_can_get_record_by_name_as_a_list(self):
        file_input = ["joel taddei,32,205", "peanut,77,18"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_name("joel taddei"), ["joel taddei", "32", "205"])
        self.assertEqual(db_reader.get_by_name("peanut"), ["peanut", "77", "18"])

    def test_db_reader_get_record_by_name_raises_error_if_multiple_people_with_same_name(self):
        file_input = ["joel taddei,32,205", "joel taddei,77,18"]
        db_reader = DBReader(file_input)
        with self.assertRaises(DBReaderException):
            db_reader.get_by_name("joel taddei")

    def test_db_reader_can_get_record_by_name_as_a_list_in_any_case(self):
        file_input = ["joel taddei,32,205", "peanut,77,18"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.get_by_name("JoEl TaDdEi"), ["joel taddei", "32", "205"])

    def test_db_reader_will_return_empty_list_if_record_by_name_not_found(self):
        db_reader = DBReader(["joel taddei,32,205", "joel taddei,77,18"])
        with self.assertRaises(DBReaderException):
            db_reader.get_by_name("joel taddei")

    def test_db_reader_can_filter_many_records_by_name_as_a_list_of_lists(self):
        file_input = ["joel taddei,32,205", "peanut,77,18", "joel taddei,2,35"]
        db_reader = DBReader(file_input)
        self.assertEqual(db_reader.filter_by_name("joel taddei"),
                         [["joel taddei", "32", "205"], ["joel taddei", "2", "35"]])

    @mock.patch("A_db.DBReader.read_file")
    def test_db_reader_will_read_from_database_if_no_contents_provided(self, read_file):
        read_file_return_value = ["joel taddei,32,205", "peanut,77,18"]
        db_reader = DBReader()
        read_file.assert_called_once_with()
