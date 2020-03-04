import os
from unittest import TestCase
from common.ini import IniFile

TEST_INI_FILE_1_FILENAME = "test-data/ini_files/test_ini_file_1.cfg"


class TestIniFile(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_file_exists1(self):
        self.assertTrue(os.path.isfile(TEST_INI_FILE_1_FILENAME))

    def test_load(self):
        ini = IniFile(TEST_INI_FILE_1_FILENAME)
        headers = ini.get_headers()
        self.assertTrue("test-header" in headers)
        self.assertTrue("test-missing-header" not in headers)
        expected = "hello"
        actual = ini.get("test-header", "message")
        self.assertEqual(expected, actual)

    def test_set(self):
        ini = IniFile(TEST_INI_FILE_1_FILENAME)
        expected = "hello"
        actual = ini.get("test-header", "message")
        self.assertEqual(expected, actual)
        ini.set("test-header", "message", "goodbye")
        actual = ini.get("test-header", "message")
        self.assertEqual("goodbye", actual)
