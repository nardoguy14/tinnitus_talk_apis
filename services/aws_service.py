import logging
import boto3
from botocore.exceptions import ClientError
from fastapi import UploadFile
import os
import base64



def upload_file(username: str, filename: str, file: UploadFile, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = f"{username}/{filename}"
    # Upload the file
    s3_client = boto3.client('s3')

    try:
        response = s3_client.upload_fileobj(file.file, bucket, object_name)
        print(response)
    except ClientError as e:
        logging.error(e)
        print(e)
        return False
    return True


def download_file(username: str, bucket, object_name=None):
    path = f"{username}/{object_name}"
    s3 = boto3.client('s3')
    temp_file_name = f"{username}{object_name}"
    with open(temp_file_name, 'wb') as f:
        s3.download_fileobj(bucket, path, f)
    in_file = open(temp_file_name, "rb")
    x = in_file.read()
    in_file.close()
    os.remove(temp_file_name)
    encoded_string = base64.b64encode(x)
    return encoded_string
