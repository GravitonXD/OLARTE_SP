#!/bin/bash

# This script will run the python virtual environment for the module and start the uvicorn server.
# Author: JOHN MARKTON M. OLARTE

# Go back to the root directory of the module
echo -e "Going back to the root directory of the module..."
cd ..
echo -e "--Done."
# Activate the virtual environment
echo -e "Activating the virtual environment..."
source venv/bin/activate
echo -e "--Done."
# Go to the SMPF[api] directory
echo -e "Going to the SMPF[api] directory..."
cd SMPF[api]
echo -e "--Done."
# Start the uvicorn server
echo -e "Now starting the uvicorn server..."
uvicorn main:app --reload
