FROM python:3.12.2

WORKDIR /flaskApp

COPY requirements.txt .

RUN pip3 install --upgrade pip -r requirements.txt

COPY . .

CMD ["python", "main.py"]