FROM python:3.12-slim@sha256:7f053e1fbe54c5e884e1b4dbff365775f0a3e316a704f0525287c8cb1cf84c2a

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
