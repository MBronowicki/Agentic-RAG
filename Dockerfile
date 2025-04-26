# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the 'src' folder contents into the container at /app/src
COPY src /app/src
# Copy the requirements.txt into the container
COPY requirements.txt /app/

# Install bash and other system dependencies if needed
RUN apt-get update && apt-get install -y bash && apt-get clean

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache -r /app/requirements.txt


# Set the working directory to 'src' where app.py is located
WORKDIR /app/src

# Run the application
CMD ["streamlit", "run", "app.py"]
