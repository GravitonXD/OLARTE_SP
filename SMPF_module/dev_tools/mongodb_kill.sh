#!/bin/bash

# This script will kill a MongoDB instance on the local machine.
# Author: JOHN MARKTON OLARTE

sudo /usr/bin/mongod --shutdown --config /etc/mongod.conf
if [ $? -eq 0 ]; then
    echo -e "\e[42;30m    MongoDB successfully stopped.    \e[0m\n"
else
    echo -e "\e[41;30m    MongoDB failed to stop/there is no MongoDB to stop    \e[0m\n"
fi