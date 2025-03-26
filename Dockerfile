# Use official Python runtime as a base image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Copy only requirements.txt first (for better caching)
COPY requirements.txt .

# Upgrade pip & install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["gunicorn", "app.py"]
