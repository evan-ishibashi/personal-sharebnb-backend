import logging
import boto3
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY = os.environ['ACCESS_KEY']
AWS_SECRET_KEY = os.environ['SECRET_KEY']

bucket = 'eb-sharebnb-listing-photos'


def upload_file(file_name, bucket, object_name=None):
    """Uploads file to AWS bucket."""
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    breakpoint()
    s3_client = boto3.client(
        's3',
        'us-west-1',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )
    try:
        response = s3_client.upload_fileobj(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Borrowed from https://saturncloud.io/blog/getting-the-file-url-after-uploading-to-amazon-s3-a-guide/


def get_file_url(bucket, object_name):
    """Get file URL after uploading to an S3 bucket

    :param bucket: Name of the S3 bucket
    :param object_name: Name of the S3 object
    :return: URL of the uploaded file
    """

    s3_client = boto3.client(
        's3',
        'us-west-1',
        aws_access_key_id=AWS_ACCESS_KEY,
        aws_secret_access_key=AWS_SECRET_KEY,
    )
    location = s3_client.get_bucket_location(
        Bucket=bucket)['LocationConstraint']
    url = f"https://{bucket}.s3.{location}.amazonaws.com/{object_name}"
    return url


# s3 = boto3.client('s3')
# with open("house.jpg", 'rb') as f:
#     s3.upload_fileobj(f, bucket, "house.jpg")


# AWSFILENAME = "TEST.jpg"
# upload_file("house.jpg", bucket, AWSFILENAME)


def upload_listing_photo(file, secure_file_name):
    print('file in upload listing', file)
    upload_file(file, bucket, secure_file_name)
    return get_file_url(bucket, secure_file_name)

# file getting added to our vscode
# fn to delete?
