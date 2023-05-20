# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY main.py .

# Set the entry point command to run the application
CMD ["python", "main.py"]
