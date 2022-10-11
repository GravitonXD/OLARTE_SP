FROM python:alpine3.16

# Copy the task_scheduler to /preprocessor/task_scheduler
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
COPY ML_model_processor /preprocessor/ML_model_processor

# Set working directory
WORKDIR /preprocessor


# Install the required packages
RUN pip3 install -r /preprocessor/requirements.txt

# Run the task_scheduler
# Tags: -f: run in foreground
#       -L: log to stdout
#        2: log level
CMD ["crond", "-l", "2", "-f"]