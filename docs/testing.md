# Testing and Validation Plan

## Purpose

This document defines how to test the serverless file-processing application. Test results must be recorded only after the corresponding tests have actually been performed.

## Test Cases

| Test | Input or action | Expected result |
|---|---|---|
| Normal text file | Upload a file containing a known number of words | Lambda calculates the expected word count |
| Multiple lines | Upload text containing several lines | Words across all lines are counted |
| Empty file | Upload a zero-byte text file | Word count is zero |
| Multiple spaces | Upload text with repeated spaces and newlines | Whitespace-separated words are counted correctly |
| SNS delivery | Process a valid file with a confirmed SNS email subscription | Notification contains the correct word count |
| Missing object permissions | Test without the required S3 read permission in a controlled environment | Processing fails and logs identify the access error |
| Missing SNS permissions | Test without the required SNS publish permission in a controlled environment | Notification publishing fails and the error can be diagnosed |
| Invalid event | Invoke Lambda with an event that has no S3 records | Function raises an input-validation error |

## How to Verify the Word Count

1. Prepare a small text file with a manually calculated word count.
2. Upload it to the configured S3 input bucket.
3. Check the Lambda invocation in the AWS Console.
4. Inspect the function's CloudWatch logs.
5. Compare the reported count against the expected count.
6. Check the SNS notification, if the email subscription is confirmed.

For example, this input contains five whitespace-separated words:

`AWS serverless applications process files`

The expected word count is **5**.

## Troubleshooting a Word Count of Zero

If a notification reports zero unexpectedly:

- Confirm the uploaded file contains text and is not empty.
- Confirm Lambda is reading the correct bucket and object key.
- Verify that the object was retrieved successfully.
- Check the CloudWatch logs for the calculated count and any exceptions.
- Confirm the event points to the intended file and that the function's code was saved and deployed.
- Ensure the SNS message uses the calculated count rather than a hard-coded value.

## Event and Notification Checks

- Confirm that the S3 event notification targets the intended Lambda function.
- Verify the Lambda resource permission allows S3 to invoke it.
- Confirm that the Lambda execution role allows the required S3 and SNS actions.
- Confirm the SNS subscription has been accepted.
- Avoid overlapping S3 notification filters for the same event type.
- Consider duplicate event deliveries when interpreting repeated notifications.

## Test Results

**Status:** Test plan documented. Application execution and successful test results have not yet been confirmed.

Record the date, test input, expected result, actual result, and pass/fail status after each test is performed.

## Limitations

The current function counts whitespace-separated tokens using Python's `split()` method. This is a simple word-count definition; it does not attempt linguistic tokenization or special handling of punctuation.
