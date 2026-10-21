from src.word_count import count_words
import logging
import os
from urllib.parse import unquote_plus

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
sns = boto3.client("sns")


def lambda_handler(event, context):
    """Count words in S3 text files and publish results to SNS."""

    topic_arn = os.environ.get("SNS_TOPIC_ARN")
    if not topic_arn:
        raise ValueError("Missing SNS_TOPIC_ARN environment variable")

    records = event.get("Records", [])
    if not records:
        raise ValueError("No S3 event records found")

    results = []

    for record in records:
        try:
            bucket = record["s3"]["bucket"]["name"]
            encoded_key = record["s3"]["object"]["key"]
        except (KeyError, TypeError) as exc:
            raise ValueError("Invalid S3 event record") from exc

        key = unquote_plus(encoded_key)

        logger.info("Processing s3://%s/%s", bucket, key)

        response = s3.get_object(Bucket=bucket, Key=key)
        body = response["Body"]

        try:
            content = body.read().decode("utf-8")
        finally:
            body.close()

        word_count = count_words(content)

        message = (
            "File processing completed.\n"
            f"Bucket: {bucket}\n"
            f"File: {key}\n"
            f"Word count: {word_count}"
        )

        sns.publish(
            TopicArn=topic_arn,
            Subject="S3 File Word Count",
            Message=message,
        )

        logger.info(
            "Word count completed for s3://%s/%s: %d",
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
