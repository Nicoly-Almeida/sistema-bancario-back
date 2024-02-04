#!/bin/sh
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
uvicorn project.asgi:application --host 0.0.0.0 --port 8000
