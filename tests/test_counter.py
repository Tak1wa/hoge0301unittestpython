import unittest
import pytest
from src.string_processor import StringProcessor

class TestCharacterCounter(unittest.TestCase):
    def setUp(self):
        self.processor = StringProcessor()

    def test_mixed_string(self):
        """英数字混合文字列のカウントテスト"""
        result = self.processor.count_characters("Hello123!")
        self.assertEqual(result["alphabets"], 5)
        self.assertEqual(result["digits"], 3)
        self.assertEqual(result["others"], 1)

    def test_only_alphabets(self):
        """アルファベットのみのカウントテスト"""
        result = self.processor.count_characters("HelloWorld")
        self.assertEqual(result["alphabets"], 10)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["others"], 0)

    def test_only_numbers(self):
        """数字のみのカウントテスト"""
        result = self.processor.count_characters("12345")
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["digits"], 5)
        self.assertEqual(result["others"], 0)

    def test_special_characters(self):
        """特殊文字のカウントテスト"""
        result = self.processor.count_characters("@#$%^")
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["digits"], 0)
        self.assertEqual(result["others"], 5)