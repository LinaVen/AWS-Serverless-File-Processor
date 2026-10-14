# AWS Serverless File Processor

Cloud Computing Assignment completed at Atlantic Technological University (ATU).

## Project Overview

This project implements a serverless application using Amazon S3, AWS Lambda, DynamoDB, and CloudWatch.

The system automatically reacts to file uploads and deletions in an S3 bucket. AWS Lambda processes the event information and stores file details in a DynamoDB table.

## AWS Services Used

- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon CloudWatch
- AWS IAM

## Architecture

The application uses an event-driven, serverless architecture.

1. A file is uploaded to or deleted from an Amazon S3 bucket.
2. Amazon S3 triggers an AWS Lambda function.
3. The Lambda function processes the event using Python.
4. The function stores event information in Amazon DynamoDB.
5. AWS CloudWatch Logs captures Lambda execution logs for monitoring and troubleshooting.

### Architecture Flow

```text
Amazon S3 (Upload / Delete)
          |
          v
AWS Lambda (Python)
          |
          +----> Amazon DynamoDB (Event Records)
          |
          +----> Amazon CloudWatch Logs (Execution Logs)
```

## Features Implemented

### DynamoDB

- Table: DynamoDB-table-s00274687
- Partition Key: id
- Stores file event information, including uploads and deletions

### Amazon S3

- Bucket: assignment2-s00274687
- Stores files uploaded to the S3 bucket
- Triggers AWS Lambda when files are uploaded or deleted

### AWS Lambda

- Function: assignment2Processor
- Python runtime
- Processes Amazon S3 upload and deletion events
- Extracts file metadata, including filename, file size, file type, and event timestamp
- Stores event records in Amazon DynamoDB

### Lambda Environment Variables

The Lambda function uses an environment variable to identify the DynamoDB table.

Configure the following environment variable in the AWS Lambda console:

- **Variable name:** `DYNAMODB_TABLE`
- **Example value:** `DynamoDB-table-s00274687`

To configure it:

1. Open your Lambda function in the AWS Management Console.
2. Select **Configuration → Environment variables**.
3. Click **Edit**.
4. Add the variable `DYNAMODB_TABLE` with your DynamoDB table name as its value.
5. Save the changes.

The Lambda function reads this value using Python's `os.environ` instead of hardcoding the table name.

### IAM Permissions

The original university assignment used the `AmazonDynamoDBFullAccess` managed policy for DynamoDB access.

For a production environment, a more secure approach is to follow the **principle of least privilege**:

- Allow `dynamodb:PutItem` on the specific DynamoDB table.
- Allow CloudWatch Logs permissions for Lambda execution logging.
- Avoid granting unnecessary access to other DynamoDB tables.

The Lambda execution role must have the required permissions to write records to DynamoDB and send logs to CloudWatch.

### CloudWatch Monitoring

- Automatic logging
- Execution monitoring
- Error tracking

## Extensions Added

### Delete Event Processing

An additional Amazon S3 trigger was configured to detect file deletion events.

The AWS Lambda function records the following event types in Amazon DynamoDB:

- `ObjectCreated:Put` — when a file is uploaded.
- `ObjectRemoved:Delete` — when a file is deleted.

Each event record includes information about the file and the type of operation performed.

### S3 Versioning

Versioning was enabled to improve recovery and data protection.

### Lifecycle Rules

Lifecycle rule: DeleteOldFiles

- Applies to all objects
- Automatically deletes files after 30 days
- Reduces storage costs

## Python Technologies Used

- `boto3` — AWS SDK for Python, used to interact with DynamoDB.
- `datetime` — Generates timestamps for file events.
- `uuid` — Generates unique identifiers for DynamoDB records.
- `os` — Reads the DynamoDB table name from an environment variable.

## Learning Outcomes

This project demonstrates practical experience in:

- Developing serverless applications using AWS Lambda and Python.
- Implementing event-driven workflows with Amazon S3.
- Processing file events and storing metadata in Amazon DynamoDB.
- Monitoring application execution using Amazon CloudWatch Logs.
- Configuring AWS IAM permissions and understanding the principle of least privilege.
- Managing S3 versioning and lifecycle rules for data protection and cost optimisation.
- Using Python and Boto3 to integrate AWS services.

## Author

**Lina Venckus (Venckuviene)**

Computer Science Graduate
Atlantic Technological University (ATU)

## Project Screenshots

The following screenshots demonstrate the AWS configuration, testing, and successful execution of this serverless application.

### 1. DynamoDB Records
![DynamoDB Records](screenshots/dynamodb_records.png)

### 2. Successful S3 File Upload
![S3 Upload Success](screenshots/s3_upload_success.png)

### 3. AWS Lambda S3 Triggers
![Lambda S3 Triggers](screenshots/lambda_s3_triggers.png)

### 4. CloudWatch Execution Logs
![CloudWatch Logs](screenshots/cloudwatch_execution_logs.png)

### 5. S3 Bucket Versioning
![S3 Versioning](screenshots/s3_versioning.png)

### 6. S3 Lifecycle Rule
![S3 Lifecycle Rule](screenshots/s3_lifecycle_rule.png)
