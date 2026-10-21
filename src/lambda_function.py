
import os
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
sns = boto3.client("sns")

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):
    """Count words in an S3 text file and publish the result to SNS."""

    records = event.get("Records", [])
    if not records:
        raise ValueError("No S3 event records found")

    results = []

    for record in records:
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]

        response = s3.get_object(Bucket=bucket, Key=key)
        content = response["Body"].read().decode("utf-8")

        word_count = len(content.split())

        message = (
            f"File processing completed.\n"
            f"Bucket: {bucket}\n"
            f"File: {key}\n"
            f"Word count: {word_count}"
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="S3 File Word Count",
            Message=message,
        )

        logger.info(
            "Processed s3://%s/%s; word_count=%d",
            bucket,
            key,
            word_count,
        )

        results.append({
            "bucket": bucket,
            "key": key,
            "word_count": word_count,
        })

    return {
        "statusCode": 200,
        "results": results,
    }
