#!/bin/bash

DATE=`date +%Y%m%d`
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t sempr/ipservice:$DATE .
docker push sempr/ipservice:$DATE

