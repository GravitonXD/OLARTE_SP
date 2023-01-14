#!/bin/bash
echo "Logging has started."
# current time
echo $(date)
python3 stats_logging.py
echo "Logging has ended."
echo $(date)
echo "Processing has started."
python3 stats_log_processing.py
echo "Processing has ended."
echo $(date)