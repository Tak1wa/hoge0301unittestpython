import unittest
import pytest
from src.string_processor import StringProcessor

class TestStringReverse(unittest.TestCase):
    def setUp(self):
        self.processor = StringProcessor()

    def test_reverse_multiple_words(self):
        """複数単語の逆順化テスト"""
        result = self.processor.reverse_words("Hello World")
        self.assertEqual(result, "olleH dlroW")

    def test_reverse_single_word(self):
        """単一単語の逆順化テスト"""
        result = self.processor.reverse_words("Python")
        self.assertEqual(result, "nohtyP")

    def test_reverse_with_numbers(self):
        """数字を含む文字列の逆順化テスト"""
        result = self.processor.reverse_words("Hello123 World456")
        self.assertEqual(result, "321olleH 654dlroW")

    def test_reverse_empty_string(self):
        """空文字列の逆順化テスト"""
        result = self.processor.reverse_words("")
        self.assertEqual(result, "")