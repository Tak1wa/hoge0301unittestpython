import unittest
import pytest
from src.string_processor import StringProcessor

class TestStringConcat(unittest.TestCase):
    def setUp(self):
        self.processor = StringProcessor()

    def test_concat_with_space(self):
        """スペース区切りの結合テスト"""
        result = self.processor.concat_with_separator(["Hello", "World"])
        self.assertEqual(result, "Hello World")

    def test_concat_with_comma(self):
        """カンマ区切りの結合テスト"""
        result = self.processor.concat_with_separator(["Apple", "Banana", "Orange"], ",")
        self.assertEqual(result, "Apple,Banana,Orange")

    def test_concat_empty_separator(self):
        """空文字列での結合テスト"""
        result = self.processor.concat_with_separator(["A", "B", "C"], "")
        self.assertEqual(result, "ABC")

    def test_concat_single_string(self):
        """単一文字列の結合テスト"""
        result = self.processor.concat_with_separator(["Hello"])
        self.assertEqual(result, "Hello")