# Use official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ./dash_app .

# Expose port
EXPOSE 8050

# Run with Gunicorn, using Flask server object from app.py
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"]