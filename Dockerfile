# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (prevents some package errors)
RUN apt-get update && apt-get install -y gcc libpq-dev python3-dev libffi-dev libssl-dev

# Copy requirements.txt separately (improves caching)
COPY requirements.txt .

# Upgrade pip & install dependencies (debugging enabled)
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --verbose -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
RUN pip install flask pandas numpy
