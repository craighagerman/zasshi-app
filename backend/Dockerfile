# syntax=docker/dockerfile:1
# Do nothing FROM python:latest
# Do nothing FROM python:3.11-slim-bookworm
FROM python:3.11-alpine
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY test.py ./
CMD [ "python", "./test.py"]
