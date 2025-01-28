FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/backend ./backend
COPY config ./config

# Set environment variables
ENV FLASK_APP=backend.app
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Run with gunicorn
CMD ["gunicorn", "--config", "config/gunicorn/gunicorn.conf.py", "backend.app:create_app()"]
