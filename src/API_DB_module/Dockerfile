# Use mongodb as base image
FROM python:alpine3.16

# Copy directories (API and DB_model) to container
COPY API /API_DB_module/API
COPY DB_model /API_DB_module/DB_model

# Setup python path for API and BD_model
ENV PYTHONPATH "${PYTHONPATH}:/API_DB_module/API"
ENV PYTHONPATH "${PYTHONPATH}:/API_DB_module/DB_module"

# Copy requirements.txt to container
COPY requirements.txt /API_DB_module

# Set working directory
WORKDIR /API_DB_module

# pip install requirements
RUN pip install -r requirements.txt

# Expose ports
EXPOSE 8000

# Run main.py when the container launches
CMD ["python3","/API_DB_module/API/main.py"]