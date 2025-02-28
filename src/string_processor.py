import time

class StringProcessor:
    def concat_with_separator(self, strings, separator=" "):
        time.sleep(1)  # 処理時間をシミュレート
        return separator.join(strings)

    def reverse_words(self, text):
        time.sleep(1.5)  # 処理時間をシミュレート
        words = text.split()
        reversed_words = [word[::-1] for word in words]
        return " ".join(reversed_words)

    def count_characters(self, text):
        time.sleep(2)  # 処理時間をシミュレート
        alpha = sum(c.isalpha() for c in text)
        digit = sum(c.isdigit() for c in text)
        other = len(text) - alpha - digit
        return {
            "alphabets": alpha,
            "digits": digit,
            "others": other
        }