import pytest
from unittest.mock import patch, MagicMock
from src.s3_upload import upload_to_s3

@patch("src.s3_upload.boto3.client")
def test_upload_to_s3(mock_boto_client):
    """Test if a file uploads successfully to S3."""
    mock_s3 = mock_boto_client.return_value
    mock_s3.upload_file.return_value = None  # Simulate successful upload

    file_path = "data/sample.pdf"
    bucket_name = "test-bucket"

    try:
        upload_to_s3(file_path, bucket_name)
        assert True  # If no exception, test passes
    except Exception:
        pytest.fail("S3 upload failed unexpectedly!")
