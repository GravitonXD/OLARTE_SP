# Class for the stocks to sell endpoints
import json
from SMPF_database.models import Sell

class Stocks2SellEndpoints:
    def __init__(self):
        pass

    def get_all_stocks_to_buy(self):
        # Get all data from the "Buy" collection
        data = Sell.objects().to_json()
        json_data = json.loads(data)
        # Return the data and the current datetime
        return {
                "All Stocks to Sell": json_data,
                "Last Updated": self._current_datetime()
        }


class PrivateEndpointsBuy:
    def __init__(self):
        pass

    def purge_stocks_to_buy(self):
        Sell.objects().delete()
        return {"message": "All data from the 'Buy' collection has been purged."}

    def put_stocks_to_buy(self):
        # Open test.json
        with open("./database/json_data/stocks2sell.json", "r") as f:
            # Read the file
            data = f.read()
            # Load the data
            json_data = json.loads(data)
        # Put the data to the "Buy" collection
        for item in json_data:
            sell = Sell(**item)
            sell.save()
        f.close()
        
        # Return the data
        return {"message": "Data from 'test.json' has been put to the 'Buy' collection."}