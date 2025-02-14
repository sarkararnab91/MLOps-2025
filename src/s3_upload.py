import os
from dotenv import load_dotenv
import subprocess
import boto3
import csv
import logging
from botocore.exceptions import NoCredentialsError
from datetime import datetime
from src.loggings.logging_config import setup_logging  # Import centralized logging

# CSV Log File
LOG_FILE_PATH = os.environ.get("LOG_FILE", "logs.csv")

# Set up logging from our centralized module
setup_logging()
logger = logging.getLogger(__name__)

# Load .env file
load_dotenv()

# AWS S3 Configuration
S3_BUCKET = os.environ.get("S3_BUCKET")
AWS_REGION = os.environ.get("AWS_REGION")
LOCAL_DATA_DIR = os.environ.get("LOCAL_DATA_DIR")

# Initialize S3 client
s3_client = boto3.client("s3")

def upload_to_s3():
    for root, _, files in os.walk(LOCAL_DATA_DIR):
        for file in files:
            file_path = os.path.join(root, file)  # Full local file path
            s3_key = os.path.relpath(file_path, LOCAL_DATA_DIR).replace("\\", "/")  # Relative path for S3
            
            logging.info(f"Uploading {file_path} to S3 as {s3_key}...")
            
            try: #trying randmomly
                s3_client.upload_file(file_path, S3_BUCKET, s3_key)
                logging.info(f"Successfully uploaded {file_path} to s3://{S3_BUCKET}/{s3_key}")
            except Exception as e:
                logging.error(f"Failed to upload {file_path}: {e}")



