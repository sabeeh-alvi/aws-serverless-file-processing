# Source Code

This directory contains the Python code for the serverless file-processing application.

## Files

- `lambda_function.py` — AWS Lambda handler. Reads text files from Amazon S3, counts words, publishes the result to Amazon SNS, and writes processing details to CloudWatch Logs.
- `word_count.py` — Reusable `count_words()` function shared by the Lambda handler and unit tests.

## Word-count behavior

The application counts whitespace-separated tokens using Python's `str.split()` method. Multiple spaces, tabs, and line breaks act as separators. Punctuation remains part of a token, so `Hello, AWS!` counts as two words.

## Packaging note

The Lambda deployment package must include the handler and the shared word-count module, with imports and the configured handler path matching the package layout. Verify the package and handler configuration before deployment.

This documentation describes the intended code structure; it does not claim that the application has been deployed or tested in AWS.
