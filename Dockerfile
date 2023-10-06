FROM python:3.8

WORKDIR /app

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

COPY consumer.py .

CMD ["python", "consumer.py"]
