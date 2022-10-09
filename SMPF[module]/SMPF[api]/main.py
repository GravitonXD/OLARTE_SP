from fastapi import FastAPI
# import models from ../SMPF[database]/models.py
from database.models import Buy
from mongoengine import connect
import json

app = FastAPI()
connect(db="smpf", host="localhost", port=27017)

# ROOT
@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Price Forecasting API developed by John Markton M. Olarte"}


# ====== STOCKS TO BUY ======

# get all stocks to buy
@app.get("/stocks_to_buy/all")
def get_all_stocks_to_buy():
    pass

# purge documents in stocks to buy collection
@app.delete("/stocks_to_buy/purge")
def purge_stocks_to_buy():
    pass

# put the new stocks to buy
@app.put("/stocks_to_buy/new")
def put_stocks_to_buy():
    pass

# ====== END STOCKS TO BUY ======


# ===== STOCKS TO SELL =====

# get all stocks to sell
@app.get("/stocks_to_sell/all")
def get_all_stocks_to_sell():
    pass

# purge documents in stocks to sell collection
@app.delete("/stocks_to_sell/purge")
def purge_stocks_to_sell():
    pass

# put the new stocks to sell
@app.put("/stocks_to_sell/new")
def put_stocks_to_sell():
    pass

# ===== END STOCKS TO SELL =====



# TODO: DELETE TESTS AFTER DEVELOPMENT
# NOTE: TEST ONLY
@app.get("/test/buy")
def test():
    # Get all data from the "Buy" collection
    data = Buy.objects().to_json()
    json_data = json.loads(data)
    # Return the data
    return {"Test Data": json_data}

# Purge all data from the "Buy" collection
# NOTE: TEST ONLY
@app.delete("/test/purge")
def purge_buy():
    Buy.objects().delete()
    return {"message": "All data from the 'Buy' collection has been purged."}

# Put data from test.json to the "Buy" collection
# NOTE: TEST ONLY
@app.post("/test/put")
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
