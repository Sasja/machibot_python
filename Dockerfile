FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip

RUN pip install \
    requests \
    jsonschema

ARG commit
RUN git pull && git checkout $commit

CMD python machibot.py
