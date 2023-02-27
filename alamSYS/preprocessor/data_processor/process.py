"""

    This script will process the data and create the json files
    for the stock to buy and stock to sell, which will be passed to the database.

"""
# Import local modules
from utils import db_actions
from utils import logs_and_alerts as la
import ml_processor as mp
from json import dump
from os import makedirs

def main():
    # Directory for the logs
    log_directory = "data_processor_logs"

    try:
        # DEEP LEARNING MODELS APPLICATION
        model_names = ["dmd_lstm"]

        for model in model_names:
            # Load the model
            try:
                loaded_model = mp.load_model(model)
                la.Logs().success_log(f"Successfully loaded model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully loaded model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to load model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to load model: {model}. Error_Info:{e}. Program will exit")
                exit(1)
            # Process the data using the model
            try:
                processed_data = mp.process_data(loaded_model, model_name=model)
                la.Logs().success_log(f"Successfully processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to process data for model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Error_Info:{e}. Program will exit")
                exit(1)
            # Post process the data
            try:
                stocks_to_buy, stocks_to_sell = mp.post_processing(processed_data, model_name=model)
                la.Logs().success_log(f"Successfully processed data for model: {model}", log_directory)
                la.Alerts().success_alert(f"Successfully processed data for model: {model}")
            except Exception as e:
                la.Logs().error_log(f"Failed to process data for model: {model}. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to process data for model: {model}. Error_Info:{e}. Program will exit")
                exit(1)

            # Save the stocks to buy and stocks to sell to json files in utils/json_data
            makedirs("/data/db/json_data", exist_ok=True)

            try:
                with open("/data/db/json_data/stocks2buy.json", "w") as f:
                    dump(stocks_to_buy, f)
                la.Logs().success_log(f"Successfully saved stocks to buy", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to buy")
            except Exception as e:
                la.Logs().error_log(f"Failed to save stocks to buy or sell. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to buy or sell. Error_Info:{e}. Program will exit")
                exit(1)

            try:
                with open("/data/db/json_data/stocks2sell.json", "w") as f:
                    dump(stocks_to_sell, f)
                la.Logs().success_log(f"Successfully saved stocks to sell", log_directory)
                la.Alerts().success_alert(f"Successfully saved stocks to sell")
            except Exception as e:
                la.Logs().error_log(f"Failed to save stocks to buy or sell. Error_Info:{e}", log_directory)
                la.Alerts().error_alert(f"Failed to save stocks to buy or sell. Error_Info:{e}. Program will exit")
                exit(1)

    except Exception as e:
        la.Logs().error_log(f"Failed to apply machine learning model/s to collected data. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to apply machine learning model/s to collected data. Error_Info:{e}. Program will exit")
        exit(1)

    try:
        # DATABASE ACTIONS
        db_actions.connect_to_db()
        la.Logs().success_log(f"Successfully connected to database", log_directory)
        la.Alerts().success_alert(f"Successfully connected to database")
    except Exception as e:
        la.Logs().error_log(f"Failed to connect to database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to connect to database. Error_Info:{e} Program will exit")
        exit(1)
    try:
        # Purge old documents from the database
        db_actions.purge_buy()
        db_actions.purge_sell()
        la.Logs().success_log(f"Successfully purged old documents from database", log_directory)
        la.Alerts().success_alert(f"Successfully purged old documents from database")
    except Exception as e:
        la.Logs().error_log(f"Failed to purge old documents from database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to purge old documents from database. Error_Info:{e} Program will exit")
    
    try:
        # Save the stocks to buy and stocks to sell to the database
        db_actions.save_buy()
        db_actions.save_sell()
        la.Logs().success_log(f"Successfully saved stocks to buy and sell to database", log_directory)
        la.Alerts().success_alert(f"Successfully saved stocks to buy and sell to database")
    except Exception as e:
        la.Logs().error_log(f"Failed to save stocks to buy and sell to database. Error_Info:{e}", log_directory)
        la.Alerts().error_alert(f"Failed to save stocks to buy and sell to database. Error_Info:{e} Program will exit")
        exit(1)

if __name__ == "__main__":
    main()
