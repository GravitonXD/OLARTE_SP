# NOTE: Script not yet finalized, this is just a template

from mongoengine import connect, disconnect
import os
import json
# Import models from utils
from models import Buy, Sell, Info

def connect_to_db():
    # Connect to the database
    connect(db=os.environ['MONGO_INITDB_DATABASE'], 
            host=os.environ['MONGO_HOST'], 
            port=int(os.environ['MONGO_PORT']))

def disconnect_from_db():
    # Disconnect from the database
    disconnect(db=os.environ['MONGO_INITDB_DATABASE'], 
            host=os.environ['MONGO_HOST'], 
            port=int(os.environ['MONGO_PORT']))

def purge_buy():
    # Delete all data in the "Buy" collection
    Buy.objects.delete()

def purge_sell():
    # Delete all data in the "Sell" collection
    Sell.objects.delete()

def save_buy_from_json():
    # Use the json file to save data to the "Buy" collection
    Buy.from_json("json_data/stocks_to_buy.json").save()

def save_sell_from_json():
    # Use the json file to save data to the "Sell" collection
    Sell.from_json("json_data/stocks_to_sell.json").save()

def save_info_from_json():
    # Use the json file to save data to the "Info" collection
    json_data = json.load(open("/preprocessor/utils/json_data/stock_info.json"))
    # Create a mapping of the json data
    for stock in json_data:
        Info(**stock).save()