# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1
# ENV DJANGO_SETTINGS_MODULE your_project_name.settings

# Create and set the working directory
RUN mkdir /code
WORKDIR /code

# Copy the current directory contents into the container at /code
ADD . /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose a port for your Django application (e.g., 8000)
EXPOSE 8000

# Start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]