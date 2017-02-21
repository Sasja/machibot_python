#!/usr/bin/env bash

commit=$(git log --format="%H" -n 1)
docker build -t machitest github.com/sasja/machibot_python#$commit
