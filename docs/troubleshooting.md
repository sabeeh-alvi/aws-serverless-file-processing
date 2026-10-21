# Troubleshooting Guide

## Purpose

This guide describes common issues in the S3, Lambda, and SNS workflow and the checks that can help diagnose them.

## 1. Lambda Is Not Invoked After an Upload

**Possible causes**
- The S3 event notification is missing or incorrectly configured.
- The notification filter does not match the uploaded filename.
- S3 lacks permission to invoke the Lambda function.
- The upload went to a different bucket than expected.

**Checks**
1. Confirm the bucket and object key.
2. Review the bucket's event notification configuration.
3. Check the Lambda resource-based permissions for S3 invocation.
4. Review available Lambda metrics and CloudWatch logs.

## 2. Word Count Is Always Zero

**Possible causes**
- The uploaded file is empty.
- The function is reading a different object than expected.
- The wrong version of the code was deployed.
- The calculated value is not being included correctly in the notification.

**Checks**
1. Verify the input file contains text.
2. Check the bucket and key extracted from the S3 event.
3. Confirm the object was retrieved successfully.
4. Review the calculated count in CloudWatch logs.
5. Confirm the SNS message uses the calculated value.

The current implementation counts whitespace-separated tokens using Python's `split()` method.

## 3. Access Denied When Reading S3

**Possible causes**
- The Lambda execution role lacks `s3:GetObject`.
- The policy references the wrong bucket or object ARN.
- A bucket policy, permissions boundary, or organization policy blocks access.
- The object is encrypted and requires additional permissions.

**Checks**
1. Inspect the Lambda execution role.
2. Verify the S3 object ARN and policy scope.
3. Review applicable bucket policies and encryption settings.
4. Grant only the additional permissions that are actually required.

## 4. SNS Notification Is Not Received

**Possible causes**
- The function lacks permission to publish to the topic.
- The topic ARN in the Lambda environment variable is incorrect.
- The email subscription has not been confirmed.
- The function fails before publishing the message.

**Checks**
1. Verify the `SNS_TOPIC_ARN` environment variable.
2. Confirm the execution role has `sns:Publish` on the intended topic.
3. Check the SNS subscription status.
4. Inspect Lambda logs for publishing errors.
5. Confirm the function completed the expected processing path.

## 5. Duplicate Notifications

**Possible causes**
- An event was delivered or processed more than once.
- A file was uploaded multiple times.
- Multiple overlapping application paths publish notifications.

**Checks**
1. Compare timestamps, object keys, and request details in the logs.
2. Review S3 event notification configuration.
3. Consider idempotency if duplicate processing would cause a problem.

S3 event notifications are not guaranteed to be delivered exactly once or in a particular order.

## 6. S3 Notification Filter Conflict

**Possible cause**

Multiple notification rules for the same event type have overlapping prefix or suffix filters.

**Checks**
1. Review existing event notification rules.
2. Remove or adjust conflicting filters.
3. Confirm the revised configuration matches the intended input files.

## Diagnostic Information to Record

For each incident, document:
- The observed symptom
- The relevant AWS service
- The error message or log excerpt
- The root cause, if confirmed
- The corrective action
- The result after retesting

Do not include credentials, secrets, or sensitive file contents in the report.

## Verification Status

This guide documents diagnostic procedures. It does not claim that these failures have been reproduced or that the application has been deployed successfully.
