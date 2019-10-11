FROM python:2.7.16-alpine3.9

WORKDIR /root

RUN pip install pymongo

COPY winner.py winner.py

ENTRYPOINT ["python", "winner.py"]
