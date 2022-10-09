# Use mongodb as base image
FROM ubuntu:latest

# Copy folder to container
COPY SMPF_module /SMPF_module
# Copy SMPF_module.sh to container
COPY SMPF_module.sh /SMPF_module

# Set working directory
WORKDIR /SMPF_module

# install python3
RUN apt-get update && apt-get install -y python3 python3-pip
# Install python dependencies
RUN pip3 install uvicorn fastapi mongoengine

# Expose ports
EXPOSE 8000

# Run SMPF_module.sh
CMD ["python3","SMPF_api/main.py"]