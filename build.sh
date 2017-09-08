#!/bin/bash

DATE=`date +%Y%m%d`

docker build -t sempr/ipservice:$DATE .
docker push sempr/ipservice:$DATE

