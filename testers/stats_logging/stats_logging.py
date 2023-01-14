import os
from time import sleep

# Run docker stats command
timer = 0
# Total log time expected in seconds
#   note: 1 day = 86400 seconds
total_log_time = 60
while timer < total_log_time:
    os.system("docker stats --no-stream >> stats.txt")
    sleep(1)
    timer += 1