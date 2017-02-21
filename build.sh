#!/usr/bin/env bash

#FIXME this is temporary
#commit=$(git log --format="%H" -n 1)
#docker build -t machitest github.com/sasja/machibot_python --build-arg commit=$commit
docker build -t machitest github.com/sasja/machibot_python
