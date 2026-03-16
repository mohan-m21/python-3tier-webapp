FROM python:3.9

WORKDIR /app

RUN pip install -r requirements.txt

RUN python3 -m pytest

COPY . .

CMD ["python", "app.py"]
