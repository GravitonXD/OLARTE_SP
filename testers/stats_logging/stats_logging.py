import os
from time import sleep

# Run docker stats command
timer = 0
# Total log time expected in seconds
#   note: 1 day = 86400 seconds (but the loop runs every 3 seconds)
#   hence, 86400/3 = 28800
total_log_time = (60 * 60 * 3) // 3
while timer < total_log_time:
    os.system("docker stats --no-stream >> stats.txt")
    timer += 1