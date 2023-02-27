# Using Python 3.10.10 for specific libraries compatibility
FROM python:3.10.10

# Copy the main to /preprocessor/main
COPY main.py /preprocessor/main.py

# Copy local directories to container
COPY data_collector /preprocessor/data_collector
COPY utils /preprocessor/utils
COPY utils/json_data /preprocessor/utils/json_data
COPY data_processor /preprocessor/data_processor
COPY data_processor/ml_model /preprocessor/data_processor/ml_model
COPY requirements.txt /preprocessor/requirements.txt

# Install vim for additional debugging capabilities
RUN apt-get update && apt-get install -y vim

# Initialize the python path for the data_collector, utils, data_processor, and ml_model
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_collector"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_processor"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/utils"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/utils/db_actions.py"
ENV PYTHONPATH "${PYTHONPATH}:/preprocessor/data_processor/ml_model"

# Set working directory
WORKDIR /preprocessor

# Install the required packages
RUN pip install --upgrade pip
RUN pip3 install -r /preprocessor/requirements.txt

# Run the main
CMD ["python", "-u", "/preprocessor/main.py"]

# For testing a specific module
#CMD ["python", "-u", "/preprocessor/data_processor/process.py"]