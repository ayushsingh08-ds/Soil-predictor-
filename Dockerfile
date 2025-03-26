# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any dependencies listed in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "app.py"]
