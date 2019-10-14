FROM python:2.7.16-alpine3.9

WORKDIR /app

COPY winner.py .
COPY requirements.txt .

RUN pip install --upgrade pip && pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP winner.py

ENTRYPOINT ["python", "winner.py"]
