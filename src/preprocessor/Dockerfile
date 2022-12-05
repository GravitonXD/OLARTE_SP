FROM python:alpine3.16

# Copy the task_scheduler to /bin/task_scheduler
COPY task_scheduler /preprocessor/task_scheduler
# Copy root to the root of crontabs
COPY root /var/spool/cron/crontabs/root
# Copy requirements.txt to /preprocessor/requirements.txt
COPY requirements.txt /preprocessor/requirements.txt
# Change the permissions of the task_scheduler
RUN chmod +x /preprocessor/task_scheduler

# Copy local directories to container
COPY data_collector /preprocessor/data_collector
COPY utils /preprocessor/utils
COPY utils/json_data /preprocessor/utils/json_data
COPY data_processor /preprocessor/data_processor
COPY data_processor/ml_model /preprocessor/data_processor/ml_model

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

# Run the task_scheduler
# Tags: -f: run in foreground
#       -L: log to stdout
#        2: log level
CMD ["crond", "-l", "2", "-f"]