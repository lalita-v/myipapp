# Use an official lightweight Python image as the base
FROM python:3.13.2-slim

# Set the working directory in the container
WORKDIR /myipapp

# Copy only the necessary files to the container
COPY requirements.txt .
# requirements.txt is a dependency file that lists all the Python packages your application needs.

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# --no-cache-dir prevents pip from storing downloaded packages in a cache.
# -r Read dependencies from requirements.txt

# Copy the rest of the application files
COPY . .
# We use two separate COPY commands because of Docker's caching mechanism. This helps speed up builds and prevent unnecessary re-installation of dependencies.

# Expose the application port (Flask runs on port 8080)
EXPOSE 8080

# Run the application
CMD ["python", "myipapp.py"]
