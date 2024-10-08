FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y procps coreutils

COPY service1/service1.py /app/

RUN pip install requests

EXPOSE 8199

CMD ["python3", "/app/service1.py"]
