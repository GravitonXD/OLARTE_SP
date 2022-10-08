from multiprocessing import AuthenticationError
from matplotlib import collections
from fastapi import FastAPI
# import models from ../SMPF[database]/models.py
from database.models import Buy
from mongoengine import connect
import json

app = FastAPI()
connect(db="smpf", host="localhost", port=27017)

@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Price Forecasting API developed by John Markton M. Olarte"}

# buy
# NOTE: TEST ONLY
@app.get("/buy")
def test():
    # Get all data from the "Buy" collection
    data = Buy.objects().to_json()
    json_data = json.loads(data)
    # Return the data
    return {"Test Data": json_data}

# Purge all data from the "Buy" collection
# NOTE: TEST ONLY
@app.delete("/purge_buy")
def purge_buy():
    Buy.objects().delete()
    return {"message": "All data from the 'Buy' collection has been purged."}

# Put data from test.json to the "Buy" collection
# NOTE: TEST ONLY
@app.post("/put_buy")
def put_buy():
    # Open test.json
    with open("./database/json_data/test.json", "r") as f:
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
