
import unittest

from src.word_count import count_words


class TestWordCount(unittest.TestCase):

    def test_normal_text(self):
        self.assertEqual(
            count_words("AWS serverless applications process files"),
            5,
        )

    def test_empty_text(self):
        self.assertEqual(count_words(""), 0)

    def test_multiple_spaces(self):
        self.assertEqual(count_words("AWS   Lambda    S3"), 3)

    def test_multiple_lines(self):
        self.assertEqual(count_words("AWS Lambda\nS3 SNS"), 4)

    def test_whitespace_only(self):
        self.assertEqual(count_words(" \n\t  "), 0)

    def test_punctuation(self):
        self.assertEqual(count_words("Hello, AWS!"), 2)


if __name__ == "__main__":
    unittest.main()
