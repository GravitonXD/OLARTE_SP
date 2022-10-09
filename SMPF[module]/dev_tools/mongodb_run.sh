#!/bin/bash

# This script will start a MongoDB instance on the local machine.
# It will use the default port 27017 and the default data directory
# Author: JOHN MARKTON OLARTE

sudo /usr/bin/mongod --fork --config /etc/mongod.conf
if [ $? -eq 0 ]; then
    echo -e "\e[42;30m    MongoDB successfully started.    \e[0m\n"
else
    echo -e "\e[41;30m   MongoDB failed to start/already running    \e[0m\n"
fi