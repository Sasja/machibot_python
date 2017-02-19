FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip

RUN pip install \
    requests \
    jsonschema

RUN mkdir /machibot && git clone https://github.com/sasja/machibot_python /machibot

ARG commit
RUN cd /machibot && git pull && git checkout $commit

CMD cd /machibot && python pythonmachibot.py
