import unittest
from src.slow_processor import SlowProcessor

class TestSlowProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = SlowProcessor()

    def test_process_data(self):
        result = self.processor.process_data("hello")
        self.assertEqual(result, "HELLO")

    def test_process_data_empty(self):
        result = self.processor.process_data("")
        self.assertEqual(result, "")

    def test_complex_calculation(self):
        result = self.processor.complex_calculation(5)
        self.assertEqual(result, 30)  # 0² + 1² + 2² + 3² + 4² = 30

    def test_complex_calculation_zero(self):
        result = self.processor.complex_calculation(0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()