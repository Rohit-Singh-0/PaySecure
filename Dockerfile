# Use official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy everything from your project folder into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for FastAPI and Streamlit apps
EXPOSE 8000
EXPOSE 8501
EXPOSE 8502

# Default command: run all services
CMD ["python", "run_all.py"]
