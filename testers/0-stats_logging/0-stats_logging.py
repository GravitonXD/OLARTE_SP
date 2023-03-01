import os

# Run docker stats command
timer = 0
# Total log time expected in seconds
#   note: 1 day = 86400 seconds (but the loop runs every 3 seconds)
#   hence, 86400/3 = 28800
seconds, minutes, hours = 60, 60, 24
total_log_time = 10
os.system("date > ./raw_data/start_time.txt")
print(f'Logging for {hours} hours')
while timer < total_log_time:
    os.system("docker stats --no-stream >> ./raw_data/stats.txt")
    timer += 1
os.system("date > ./raw_data/end_time.txt")
print('Logging complete')