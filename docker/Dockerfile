FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.backend
ENV FLASK_ENV=production

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.backend:app"]
