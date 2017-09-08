#!/bin/bash
DIR="$( cd "$( dirname "$BASH_SOURCE[0]" )" && pwd )"
cd "$DIR"

DATE=`date +%Y%m%d`
docker login -u="$DOCKER_USERNAME" -p="$DOCKER_PASSWORD"
docker build -t sempr/ipservice:$DATE .
docker push sempr/ipservice:$DATE

