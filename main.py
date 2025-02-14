from src.s3_upload import *
import logging
from src.loggings.logging_config import setup_logging 
# Set up logging from our centralized module
setup_logging()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.info("Checking for changes in DVC...")
    result = subprocess.run(["dvc", "status"], capture_output=True, text=True)
    
    if "data.dvc" in result.stdout:
        logging.info(" Changes detected! Uploading to S3...")
        subprocess.run(["dvc", "add", "data/"], check=True)
        subprocess.run(["git", "add", "data.dvc"], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-updating data files"], check=True)
        subprocess.run(["dvc", "push"], check=True)
        upload_to_s3()
    else:
        logging.info("No changes detected. Exiting.")