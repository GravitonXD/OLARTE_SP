#!/bin/bash

# This will run all the scripts in the dev_tools directory.
# Author: JOHN MARKTON M. OLARTE

# Run to start the MongoDB instance
echo -e "Starting MongoDB..."
./mongodb_run.sh
echo -e "--Done."

# Run to start the uvicorn server
echo -e "Starting uvicorn server..."
./uvicorn_run.sh