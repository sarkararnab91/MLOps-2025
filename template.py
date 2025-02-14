import os
from pathlib import Path 

# Define project structure
PROJECT_STRUCTURE = {
    "pdf-data-pipeline": [
        "src",
        "tests",
        ".github/workflows",
        "terraform",
        "logs",
        'data'
    ],
    "src": [
        "dvc_tracking.py",
        "s3_upload.py",
        "chunking.py",
        "embedding.py",
        "vector_store.py",
        "main.py",
        "utils.py",
    ],
    "tests": [
        "test_dvc_tracking.py",
        "test_s3_upload.py",
        "test_chunking.py",
        "test_embedding.py",
        "test_vector_store.py",
    ],
    ".github/workflows": [
        "ci.yml",
    ],
    "terraform": [
        "main.tf",
        "variables.tf",
        "outputs.tf",
    ],
}

# Files with content templates
TEMPLATE_FILES = {
    "README.md": "# PDF Data Pipeline\n\nThis repository contains a pipeline for processing unstructured PDFs.",
    "requirements.txt": "boto3\npytest\npgvector\ndvc[aws]\nblack\nflake8\n",
    "Dockerfile": """\
# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY src/ ./src/
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the pipeline
CMD ["python", "src/main.py"]
""",
    ".gitignore": """\
__pycache__/
*.log
.env
data/
.dvc/
terraform.tfstate*
""",
}

def create_project_structure():
    """Creates the directory structure and files for the project."""
    for folder, subitems in PROJECT_STRUCTURE.items():
        os.makedirs(folder, exist_ok=True)
        for item in subitems:
            path = Path(os.path.join(folder, item))
            if "." in item[1:]:  # If . present not in the beginning but in the middle 
                with open(path, "w") as f:
                    #f.write(f"# {item}\n")  # Add a comment as a placeholder
                    pass
            else:
                os.makedirs(path, exist_ok=True)

    for filename, content in TEMPLATE_FILES.items():
        #if file already exist then don't overwrite
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                f.write(content)

    print("✅ Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
