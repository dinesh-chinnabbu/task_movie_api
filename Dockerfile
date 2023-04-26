# Use an official Python runtime as a parent image
FROM python:3.7.4

# Set the working directory to /app
WORKDIR /task_movie_api

# Copy the current directory contents into the container at /app
COPY . /task_movie_api

RUN apt-get update -y
RUN apt-get install -y libpq-dev python3-dev
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install importlib-metadata==4.13.0

