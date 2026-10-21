# IAM Permissions and Security

## Purpose

This document describes the permissions required by the serverless file-processing application and the security principles used to limit access.

## Lambda Execution Role

The Lambda function requires an IAM execution role trusted by the AWS Lambda service.

The role should include permissions for:

- Reading the intended input objects from Amazon S3.
- Publishing processing results to the designated Amazon SNS topic.
- Writing execution logs to Amazon CloudWatch Logs.

## Permission Mapping

| Action | Resource scope | Purpose |
|---|---|---|
| `s3:GetObject` | Intended input bucket objects | Read uploaded text files |
| `sns:Publish` | Intended SNS topic ARN | Publish word-count notifications |
| `logs:CreateLogGroup` | Relevant log group resources, as required | Create a log group when needed |
| `logs:CreateLogStream` | Relevant Lambda log group | Create log streams |
| `logs:PutLogEvents` | Relevant Lambda log streams | Write execution logs |

The exact resource ARNs and any additional permissions must be reviewed against the deployment configuration and AWS service requirements before use.

## Trust Relationship

The role's trust policy should allow the `lambda.amazonaws.com` service to assume the role. The role should not be trusted by unrelated services or users unless there is a documented need.

## Security Best Practices

- Follow least privilege and restrict S3 permissions to the required bucket and objects.
- Restrict `sns:Publish` to the designated SNS topic.
- Keep S3 Block Public Access enabled.
- Do not place AWS access keys or credentials in the Python source code.
- Protect email subscription and notification configuration.
- Review CloudWatch logs to ensure sensitive file contents are not recorded.
- Review permissions periodically and remove unnecessary actions.

## Important Implementation Note

This document is a permission design guide, not a deployed IAM policy. Confirm the resource ARNs and validate the policy against the actual environment before attaching it to an IAM role.

## Verification Status

The permission design has been documented in the repository. The actual IAM role, policies, and access behavior have not yet been confirmed through deployment and testing.
