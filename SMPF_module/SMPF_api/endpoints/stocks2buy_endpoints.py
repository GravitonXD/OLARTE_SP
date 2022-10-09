# Class for the stocks to buy endpoints
import json
from SMPF_database.models import Buy
from datetime import datetime

class Stocks2BuyEndpoints:
    def __init__(self):
        pass

    

    def get_all_stocks_to_buy(self):
        # Get all data from the "Buy" collection
        data = Buy.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks to Buy": json_data,
                "Last Updated": self._current_datetime()
        }

        
class PrivateEndpointsBuy:
    def __init__(self):
        pass

    def purge_stocks_to_buy(self):
        Buy.objects().delete()
        return {"message": "All data from the 'Buy' collection has been purged."}

    def put_stocks_to_buy(self):
        # Open test.json
        with open("./database/json_data/stocks2buy.json", "r") as f:
            # Read the file
            data = f.read()
            # Load the data
            json_data = json.loads(data)
        # Put the data to the "Buy" collection
        for item in json_data:
            buy = Buy(**item)
            buy.save()
        f.close()
        
        # Return the data
        return {"message": "Data from 'test.json' has been put to the 'Buy' collection."}