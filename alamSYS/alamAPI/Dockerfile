# Use mongodb as base image
FROM python:alpine3.16

# Copy directories (API and DB_model) to container
COPY API /alamAPI/API
COPY DB_model /alamAPI/DB_model
COPY API/routers /alamAPI/API/routers

# Setup python path for API and BD_model
ENV PYTHONPATH "${PYTHONPATH}:/alamAPI/API"
ENV PYTHONPATH "${PYTHONPATH}:/alamAPI/DB_module"

# Copy requirements.txt to container
COPY requirements.txt /alamAPI

# Set working directory
WORKDIR /alamAPI

# pip install requirements
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

# Run main.py when the container launches
CMD ["python3","/alamAPI/API/main.py"]