FROM python:3.11

# Copy the task_scheduler to /bin/task_scheduler
COPY task_scheduler.py /preprocessor/task_scheduler.py

# Copy local directories to container
COPY data_collector /preprocessor/data_collector
COPY utils /preprocessor/utils
COPY utils/json_data /preprocessor/utils/json_data
COPY data_processor /preprocessor/data_processor
COPY data_processor/ml_model /preprocessor/data_processor/ml_model
COPY requirements.txt /preprocessor/requirements.txt

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

CMD ["python", "/preprocessor/task_scheduler.py"]