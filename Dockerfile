# Use Python 3.13 slim image as base
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Create a non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create entrypoint script directly in Dockerfile to avoid line ending issues
RUN echo '#!/bin/sh' > /entrypoint.sh && \
    echo 'set -e' >> /entrypoint.sh && \
    echo 'echo "Starting OC Lettings application..."' >> /entrypoint.sh && \
    echo 'if [ -z "$SECRET_KEY" ]; then' >> /entrypoint.sh && \
    echo '  echo "WARNING: SECRET_KEY not set, using default"' >> /entrypoint.sh && \
    echo '  export SECRET_KEY="temp-secret-key-for-docker-build-only"' >> /entrypoint.sh && \
    echo 'fi' >> /entrypoint.sh && \
    echo 'echo "Collecting static files..."' >> /entrypoint.sh && \
    echo 'python manage.py collectstatic --noinput --clear' >> /entrypoint.sh && \
    echo 'echo "Setup complete. Starting server..."' >> /entrypoint.sh && \
    echo 'exec "$@"' >> /entrypoint.sh && \
    chmod +x /entrypoint.sh

# Create necessary directories and set permissions
RUN mkdir -p staticfiles && \
    chown -R appuser:appuser /app && \
    chown appuser:appuser /entrypoint.sh

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000')" || exit 1

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Run the application with Gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "60", "oc_lettings_site.wsgi:application"]
