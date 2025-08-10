FROM python:3.10-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENV PORT=8000
ENV DEBUG=True
ENV ALLOWED_HOST=127.0.0.1,localhost

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]