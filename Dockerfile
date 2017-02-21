FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip

RUN pip install \
    requests \
    jsonschema

COPY ./ .

CMD python machibot.py
