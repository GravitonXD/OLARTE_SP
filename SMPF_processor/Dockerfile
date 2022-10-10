FROM python:alpine3.16

# Copy the task_scheduler to /SMPF_processor/test
COPY task_scheduler /SMPF_processor/task_scheduler
# Copy root to the root of crontabs
COPY root /var/spool/cron/crontabs/root
# Copy the PHSMDataCollector_module directory to /SMPF_processor/PHSMDataCollector_module
COPY PHSMDataCollector_module /SMPF_processor/PHSMDataCollector_module
# Copy processor_utils to /bin/processor_utils
COPY processor_utils /SMPF_processor/processor_utils
# Copy requirements.txt to /bin/requirements.txt
COPY requirements.txt /SMPF_processor/requirements.txt

# Set working directory
WORKDIR /SMPF_processor

# Change the permissions of the task_scheduler
RUN chmod +x /SMPF_processor/task_scheduler

# Install the required packages
RUN pip3 install -r /SMPF_processor/requirements.txt

# Run the task_scheduler
# Tags: -f: run in foreground
#       -L: log to stdout
#        2: log level
CMD ["crond", "-l", "2", "-f"]