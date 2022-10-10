# SMPF Processor
This directory contains the scheduler (using CRON), PHSM Data Collector Module (PDCM), and the Stock Price Forecasting Model (SPFM)

SMPF Processor processes the data collection and passing of data to the SPFModel in a set schedule for each weekday.

# Schedules Defined
In this section define the schedule for the processing.

1. Weekday (Monday to Friday) - PSE Active days
2. Hour:Minute    (18th Hour: 0 minutes (6PM)) - Closing time of the market is arounf 5PM, data from EODHD is delayed for 15 minutes, however we need to make sure to provide ample time for any delay in the data updating on the third-party data provider.
