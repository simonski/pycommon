import os
from unittest import TestCase
from common import utils


TEST_FILENAME = "test-data/token_switching/token_switching_file.txt"


class TestUtils(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(TEST_FILENAME))

    def test_get_free_port(self):
        pass

    def test_is_port_available(self):
        pass

    def test_resolve_file(self):
        pass

    def test_token_switch(self):
        pass

    """
    def test_list_tokens(self):
        content = utils.read_file(TEST_FILENAME)
        actual = sorted(utils.list_tokens(content))
        expected = ["TOKEN_1", "KIND_OF_THING", "TBBC"]
        self.assertListEqual(actual, expected)
    """

    def test_split_file(self):
        pass
