#!/bin/bash

app="flask-app"

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker rmi flask-app