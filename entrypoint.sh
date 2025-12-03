#!/bin/sh
set -e

echo "Starting OC Lettings application..."

if [ -z "$SECRET_KEY" ]; then
    echo "WARNING: SECRET_KEY not set, using default"
    export SECRET_KEY="temp-secret-key-for-docker-build-only"
fi

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Setup complete. Starting server..."
exec "$@"
