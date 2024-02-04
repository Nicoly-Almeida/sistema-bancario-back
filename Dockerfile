FROM python:3.11-alpine
RUN apk add --no-cache build-base

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE project.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for Uvicorn
EXPOSE 8000

RUN ["chmod", "+x", "docker-entrypoint.sh"]
