FROM python:3.9

WORKDIR /app

COPY . .

RUN yum install -y python3-pip

RUN pip install -r backend/requirements.txt

CMD ["python", "app.py"]
