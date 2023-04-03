import re
import os

stats = []
# Read the file
with open('./stats.txt', 'r') as f:
    line_counter = 0
    for line in f:
        words = line.split()
        try:
            # Use regex to only include words that has a number in it
            if re.search(r'\d', words[0]) and line_counter%4 != 0:
                stats.append(words)
            line_counter += 1
        except Exception as e:
            print(e)

# Initialize the stat arrays for each container
cpu_stats_preprocessor = []
cpu_stats_alamAPI_API = []
cpu_stats_alamAPI_DB = []

memory_stats_preprocessor = []
memory_stats_alamAPI_API = []
memory_stats_alamAPI_DB = []

network_stats_preprocessor = []
network_stats_alamAPI_API = []
network_stats_alamAPI_DB = []

# Loop through the stats array and append the stats to the correct container
line_counter = 0
for items in stats:
    counter = line_counter % 3
    if counter == 1:
        cpu_stats_preprocessor.append(items[2])
        memory_stats_preprocessor.append(items[3])
        network_stats_preprocessor.append(items[7])
    elif counter == 2:
        cpu_stats_alamAPI_API.append(items[2])
        memory_stats_alamAPI_API.append(items[3])
        network_stats_alamAPI_API.append(items[7])
    elif counter == 0:
        cpu_stats_alamAPI_DB.append(items[2])
        memory_stats_alamAPI_DB.append(items[3])
        network_stats_alamAPI_DB.append(items[7])
    line_counter += 1

# PROCEESSING CPU STATS
# For CPU stats split the % sign and convert to float
cpu_stats_preprocessor = [float(i.split('%')[0]) for i in cpu_stats_preprocessor]
cpu_stats_alamAPI_API = [float(i.split('%')[0]) for i in cpu_stats_alamAPI_API]
cpu_stats_alamAPI_DB = [float(i.split('%')[0]) for i in cpu_stats_alamAPI_DB]

# PROCEESSING MEMORY STATS
# use regex to put the non-numeric characters in another array (as a string)
size_stats_preprocessor = [re.sub(r'[0-9]+', '', i) for i in memory_stats_preprocessor]
size_stats_alamAPI_API = [re.sub(r'[0-9]+', '', i) for i in memory_stats_alamAPI_API]
size_stats_alamAPI_DB = [re.sub(r'[0-9]+', '', i) for i in memory_stats_alamAPI_DB]
# Use regex to delete the non-numeric characters and convert to float
memory_stats_preprocessor = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in memory_stats_preprocessor]
memory_stats_alamAPI_API = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in memory_stats_alamAPI_API]
memory_stats_alamAPI_DB = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in memory_stats_alamAPI_DB]
# Convert the memory stats to (GiB) if the size is (MiB)
for i, j in zip(memory_stats_preprocessor, size_stats_preprocessor):
    if j == "MiB" or ".MiB":
        i = i/1024
for i, j in zip(memory_stats_alamAPI_API, size_stats_alamAPI_API):
    if j == "MiB" or ".MiB":
        i = i/1024
for i, j in zip(memory_stats_alamAPI_DB, size_stats_alamAPI_DB):
    if j == "MiB" or ".MiB":
        i = i/1024

# PROCEESSING NETWORK STATS
# Use regex to put the non-numeric characters in another array (as a string)
size_stats_preprocessor_network = [re.sub(r'[0-9]+', '', i) for i in network_stats_preprocessor]
size_stats_alamAPI_API_network = [re.sub(r'[0-9]+', '', i) for i in network_stats_alamAPI_API]
size_stats_alamAPI_DB_network = [re.sub(r'[0-9]+', '', i) for i in network_stats_alamAPI_DB]
# Use regex to delete the non-numeric characters and convert to float
network_stats_preprocessor = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in network_stats_preprocessor]
network_stats_alamAPI_API = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in network_stats_alamAPI_API]
network_stats_alamAPI_DB = [float(re.sub(r'[a-zA-Z]+', '', i)) for i in network_stats_alamAPI_DB]
# Convert the network stats to (MB) if the size is (kB)
network_stats_preprocessor = [i/1024 if j == 'kB' else i for i, j in zip(network_stats_preprocessor, size_stats_preprocessor_network)]
network_stats_alamAPI_API = [i/1024 if j == 'kB' else i for i, j in zip(network_stats_alamAPI_API, size_stats_alamAPI_API_network)]
network_stats_alamAPI_DB = [i/1024 if j == 'kB' else i for i, j in zip(network_stats_alamAPI_DB, size_stats_alamAPI_DB_network)]
# Convert the network stats to (MB) if the size is (GB)
network_stats_preprocessor = [i*1024 if j == 'GB' else i for i, j in zip(network_stats_preprocessor, size_stats_preprocessor_network)]
network_stats_alamAPI_API = [i*1024 if j == 'GB' else i for i, j in zip(network_stats_alamAPI_API, size_stats_alamAPI_API_network)]
network_stats_alamAPI_DB = [i*1024 if j == 'GB' else i for i, j in zip(network_stats_alamAPI_DB, size_stats_alamAPI_DB_network)]


os.makedirs('./processed_data', exist_ok=True)
# Save the processed stats (CPU) to a csv file (preprocessor, alamAPI_API, alamAPI_DB)
with open('./processed_data/cpu_stats.csv', 'w') as f:
    f.write("time(s),preprocessor,alamAPI_API,alamAPI_DB\n")
    for i in range(len(cpu_stats_preprocessor)):
        f.write(f"{i},{cpu_stats_preprocessor[i]},{cpu_stats_alamAPI_API[i]},{cpu_stats_alamAPI_DB[i]}\n")

# Save the processed stats (Memory) to a csv file (preprocessor, alamAPI_API, alamAPI_DB)
with open('./processed_data/memory_stats.csv', 'w') as f:
    f.write("time(s),preprocessor,alamAPI_API,alamAPI_DB\n")
    for i in range(len(memory_stats_preprocessor)):
        f.write(f"{i},{memory_stats_preprocessor[i]},{memory_stats_alamAPI_API[i]},{memory_stats_alamAPI_DB[i]}\n")

# Save the processed stats (Network) to a csv file (preprocessor, alamAPI_API, alamAPI_DB)
with open('./processed_data/network_stats.csv', 'w') as f:
    f.write("time(s),preprocessor,alamAPI_API,alamAPI_DB\n")
    for i in range(len(network_stats_preprocessor)):
        f.write(f"{i},{network_stats_preprocessor[i]},{network_stats_alamAPI_API[i]},{network_stats_alamAPI_DB[i]}\n")

