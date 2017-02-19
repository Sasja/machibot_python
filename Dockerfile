FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    git \
    python \
    python-pip

RUN pip install \
    requests \
    jsonschema

ARG repo_url 
RUN mkdir /machibot && git clone $repo_url /machibot

ARG commit
RUN cd /machibot && git pull && git checkout $commit

CMD cd /machibot && python machibot.py
