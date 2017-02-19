FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip

RUN pip install \
    requests \
    jsonschema

RUN mkdir /machibot && git clone https://github.com/sasja/machibot_python /machibot

RUN cd /machibot && git pull && git checkout 544ac21c1670cab96e27fc2aae7853be8e83da8c

CMD cd /machibot && python pythonmachibot.py
