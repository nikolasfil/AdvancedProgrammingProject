
FROM python:3.9

WORKDIR /app

COPY publisher.py . 
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","publisher.py"]