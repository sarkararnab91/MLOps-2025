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
