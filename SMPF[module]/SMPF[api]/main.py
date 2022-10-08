from matplotlib import collections
from fastapi import FastAPI
# import models from ../SMPF[database]/models.py
from database.models import Buy
from mongoengine import connect

app = FastAPI()
connect(db="smpf", host="localhost", port=27017)

@app.get("/")
def home():
    return {"message": "Welcome to Stock Market Price Forecasting API developed by John Markton M. Olarte"}

# Test endpoint
@app.get("/test")
def test():
    # Get all data from the "Buy" collection
    data = Buy.objects()
    # Return the data
    return data.to_json()