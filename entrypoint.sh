#!/bin/bash
# Entrypoint script for Docker container

set -e

echo "🚀 Starting OC Lettings application..."

# Check if required environment variables are set
if [ -z "$SECRET_KEY" ]; then
    echo "⚠️  WARNING: SECRET_KEY not set, using default (not for production!)"
    export SECRET_KEY="temp-secret-key-for-docker-build-only"
fi

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Run migrations (optional, uncomment if needed)
# echo "🔄 Running database migrations..."
# python manage.py migrate --noinput

echo "✅ Setup complete!"
echo "🌐 Starting Gunicorn server..."

# Execute the main command (passed as arguments to this script)
exec "$@"
