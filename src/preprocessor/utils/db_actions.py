# NOTE: Script not yet finalized, this is just a template

from mongoengine import connect, disconnect
import os
import json
from models import Buy, Sell, Info
import logs_and_alerts as la


def connect_to_db():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    try:
        # Connect to the database
        connect(db=os.environ['MONGO_INITDB_DATABASE'], 
                host=os.environ['MONGO_HOST'], 
                port=int(os.environ['MONGO_PORT']))
        
        ### LOG AND ALERT ###
        message = "Successfully connected to the database"
        # Log the successful connection to the database in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful connection to the database
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to connect to the database"
        # Log the failed connection to the database in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed connection to the database
        la.Alerts().error_alert(message)
        ######################


def disconnect_from_db():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs
    try:
        # Disconnect from the database
        disconnect(db=os.environ['MONGO_INITDB_DATABASE'], 
                host=os.environ['MONGO_HOST'], 
                port=int(os.environ['MONGO_PORT']))\
        
        ### LOG AND ALERT ###
        message = "Successfully disconnected from the database"
        # Log the successful disconnection from the database in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful disconnection from the database
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to disconnect from the database"
        # Log the failed disconnection from the database in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed disconnection from the database
        la.Alerts().error_alert(message)
        ######################


def purge_buy():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs
    try:
        # Delete all data in the "Buy" collection
        Buy.objects.delete()

        ### LOG AND ALERT ###
        message = "Successfully purged the Buy Collection"
        # Log the successful purging of the Buy Collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful purging of the Buy Collection
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to purge the Buy Collection"
        # Log the failed purging of the Buy Collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed purging of the Buy Collection
        la.Alerts().error_alert(message)
        ######################


def purge_sell():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs
    try:
        # Delete all data in the "Sell" collection
        Sell.objects.delete()

        ### LOG AND ALERT ###
        message = "Successfully purged the Sell Collection"
        # Log the successful purging of the Sell Collection in the success_log.txt file
        la.Logs().success_log(message, log_directory)
        # Alert the successful purging of the Sell Collection
        la.Alerts().success_alert(message)
        ######################
    except:
        ### LOG AND ALERT ###
        message = "Failed to purge the Sell Collection"
        # Log the failed purging of the Sell Collection in the error_log.txt file
        la.Logs().error_log(message, log_directory)
        # Alert the failed purging of the Sell Collection
        la.Alerts().error_alert(message)
        ######################


def save_buy_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Buy" collection
    json_data = json.load(open("/preprocessor/utils/json_data/stocks2buy.json"))
    # Create a mapping of the json data
    for stock in json_data:
        try:
            Buy(**stock).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {stock['stock_symbol']} to the Buy Collection"
            # Log the successful saving of the stock to the Buy Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the stock to the Buy Collection
            la.Alerts().success_alert(message)
        except:
            ### LOG AND ALERT ###
            message = f"Failed to save {stock['stock_symbol']} to the Buy Collection"
            # Log the failed saving of the stock to the Buy Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the stock to the Buy Collection
            la.Alerts().error_alert(message)
            # Continue to the next stock
            continue

def save_sell_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Sell" collection
    json_data = json.load(open("/preprocessor/utils/json_data/stocks2sell.json"))
    # Create a mapping of the json data
    for stock in json_data:
        try:
            Sell(**stock).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {stock['stock_symbol']} to the Sell Collection"
            # Log the successful saving of the stock to the Sell Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the stock to the Sell Collection
            la.Alerts().success_alert(message)
        except:
            ### LOG AND ALERT ###
            message = f"Failed to save {stock['stock_symbol']} to the Sell Collection"
            # Log the failed saving of the stock to the Sell Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the stock to the Sell Collection
            la.Alerts().error_alert(message)

            # Continue to the next stock
            continue


def save_info_from_json():
    log_directory = "preprocessor_utils_logs/db_actions" # Directory for the logs

    # Use the json file to save data to the "Info" collection
    json_data = json.load(open("/preprocessor/utils/json_data/stock_info.json"))
    # Create a mapping of the json data
    for stock in json_data:
        try:
            Info(**stock).save()

            ### LOG AND ALERT ###
            message = f"Successfully saved {stock['stock_symbol']} to the Info Collection"
            # Log the successful saving of the stock to the Info Collection in the success_log.txt file
            la.Logs().success_log(message, log_directory)
            # Alert the successful saving of the stock to the Info Collection
            la.Alerts().success_alert(message)
        except:
            ### LOG AND ALERT ###
            message = f"Failed to save {stock['stock_symbol']} to the Info Collection"
            # Log the failed saving of the stock to the Info Collection in the error_log.txt file
            la.Logs().error_log(message, log_directory)
            # Alert the failed saving of the stock to the Info Collection
            la.Alerts().error_alert(message)

            # Continue to the next stock
            continue