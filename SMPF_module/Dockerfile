# Use mongodb as base image
FROM python:alpine3.16

# Copy folder to container
COPY SMPF_api /SMPF_api
# Copy requirements.txt to container
COPY requirements.txt /SMPF_api

# Set working directory
WORKDIR /SMPF_api

# pip install requirements
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

# Run main.py when the container launches
CMD ["python3","main.py"]