FROM python:3.10-slim-bookworm

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
# Ensures output is sent straight to terminal without buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies needed for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    build-essential \
    libssl-dev \
    pkg-config \
    default-mysql-client \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables
ENV PORT=8000
ENV DEBUG=True
ENV ALLOWED_HOSTS=127.0.0.1,localhost

EXPOSE 8000

# Default command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



# FROM python:3.10-slim-bookworm

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# RUN adduser --disabled-password --gecos '' appuser

# WORKDIR /app

# COPY requirements.txt .

# RUN apt-get update && apt-get install -y \
#     gcc \
#     default-libmysqlclient-dev \
#     build-essential \
#     libssl-dev \
#     pkg-config \
#  && rm -rf /var/lib/apt/lists/*


# RUN pip install --no-cache-dir -r requirements.txt

# COPY . .

# # Change ownership of the app to the non-root user. Include -p to satify checker
# RUN chown -R appuser:appuser /app

# USER appuser

# ENV PORT=8000
# ENV DEBUG=True
# ENV ALLOWED_HOST=127.0.0.1,localhost

# EXPOSE 8000

# HEALTHCHECK CMD curl --fail http://127.0.0.1:8000/ || exit 1

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]