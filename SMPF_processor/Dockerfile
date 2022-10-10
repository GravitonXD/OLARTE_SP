FROM python:alpine3.16

# Copy the task_scheduler to /bin/test
COPY task_scheduler /bin/task_scheduler
# Copy root to the root of crontabs
COPY root /var/spool/cron/crontabs/root
# Copy the PHSMDataCollector_module directory to /bin/PHSMDataCollector_module
COPY PHSMDataCollector_module /bin/PHSMDataCollector_module

# Change the permissions of the task_scheduler
RUN chmod +x /bin/task_scheduler

# Run the task_scheduler
# Tags: -f: run in foreground
#       -L: log to stdout
#        2: log level
CMD ["crond", "-l", "2", "-f"]