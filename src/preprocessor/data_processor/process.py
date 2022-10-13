"""

    This script will process the data and create the json files
    for the stock to buy and stock to sell, which will be passed to the database.

"""

# Importing the libraries

# Import local modules
from utils import db_actions
import ml_processor as mp

def main():
    pass
    # TODO: run the main function from ml_processor.py
    mp.main()
    # TODO: connect to the database
    db_actions.connect_to_db()
    # TODO: purge the database collections data and save the new data, add checks before continuing
    db_actions.purge_buy()
    db_actions.purge_sell()
    db_actions.save_buy_from_json()
    db_actions.save_sell_from_json()
    # disconnect from the database
    db_actions.disconnect_from_db()
