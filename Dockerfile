FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV WORKDIR=/src
WORKDIR $WORKDIR

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src $WORKDIR

CMD python main.py
