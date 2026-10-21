# Unit Testing Guide

## Purpose

The unit tests document the expected behavior of the project's whitespace-separated word-count logic.

They use Python's built-in `unittest` framework and do not require AWS credentials or deployed AWS resources.

## Test Coverage

| Test | Expected behavior |
|---|---|
| Normal text | Counts five whitespace-separated words |
| Empty text | Returns zero |
| Multiple spaces | Counts words correctly despite repeated spaces |
| Multiple lines | Counts words across line breaks |
| Whitespace-only input | Returns zero |
| Punctuation | Counts whitespace-separated tokens without removing punctuation |

## Running the Tests

With Python 3 installed, open a terminal in the repository's root directory and run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

On some systems, the command may be `python3` instead of `python`.

A successful run should report that all six tests passed.

## Current Scope and Limitations

The tests currently exercise a standalone `count_words()` helper in `test_word_count.py`.

They do not import or invoke the AWS Lambda handler, and they do not test S3 event parsing, S3 object retrieval, SNS publishing, IAM permissions, or CloudWatch logging.

The helper currently duplicates the word-count expression used by the Lambda function. A future improvement would be to move the shared counting logic into a reusable module and test that same function directly.

## Verification Status

The test file and this guide have been committed to GitHub. The tests have not yet been executed, so a passing test result has not been confirmed.
