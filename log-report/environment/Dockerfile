FROM python:3.11-slim-bookworm@sha256:74012ddba2bc217440b5dc8ea21012baa9ef20eab68bccfd98f269e0b1da581f

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log
