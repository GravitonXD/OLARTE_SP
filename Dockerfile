# Use mongodb as base image
FROM mongo:latest

# Copy folder to container
COPY SMPF_module /SMPF_module
# Copy SMPF_module.sh to container
COPY SMPF_module.sh /SMPF_module

# Set working directory
WORKDIR /SMPF_module

# Install python and pip
RUN apt-get update && apt-get install -y python3 python3-pip
# Install python dependencies
RUN pip3 install uvicorn fastapi mongoengine

# Expose ports
EXPOSE 8000 27017

# Run SMPF_module.sh
CMD ["./SMPF_module.sh"]