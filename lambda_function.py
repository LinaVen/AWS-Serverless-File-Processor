import boto3
from datetime import datetime
import uuid

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('DynamoDB-table-s00274687')

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        file_size = record['s3']['object'].get('size', 0)
        timestamp = datetime.utcnow().isoformat()
        item_id = str(uuid.uuid4())

        if "." in key:
            file_type = key.split(".")[-1]
        else:
            file_type = "unknown"

        event_name = record['eventName']

        table.put_item(
            Item={
                "id": item_id,
                "bucket": bucket,
                "filename": key,
                "filesize": file_size,
                "eventType": event_name,
                "uploadTime": timestamp,
                "fileType": file_type
            }
        )

    return {"status": "ok", "files_logged": len(event['Records'])}