#!/bin/bash
echo "Logging has started."
python3 stats_logging.py
echo "Logging has ended."
echo "Processing has started."
python3 stats_log_processing.py
echo "Processing has ended."