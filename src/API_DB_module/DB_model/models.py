from mongoengine import Document, StringField, FloatField, ListField, IntField
# Models for the database in MongoDB

# Define class "Buy" and inherit from "Document"
"""
About the Buy class:
    - This class is used to define the structure of the "buy" collection in the MongoDB database
    - This document contains the stocks to buy based from the predicted price trend from the Machine Learning model
"""
class Buy(Document):
    # Stock Symbol refers to the stock symbol of the stock
    stock_symbol =  StringField()
    # Last Closing refers to the last closing price of the stock
    last_closing =  FloatField()
    # Predicted Closing is a list of predicted closing prices for the stock
    predicted_closing = ListField()

    # When putting data to the "Buy" collection, the data will be in this format
    def from_json(self, json_data):
        self.stock_symbol = json_data.get("stock_symbol")
        self.last_closing = json_data.get("last_closing")
        self.predicted_closing = json_data.get("predicted_closing")

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "predicted_closing": self.predicted_closing
        }



# Define class "Sell" and inherit from "Document"
""""
About the Sell class:
    - This class is used to define the structure of the "sell" collection in the MongoDB database
    - This document contains the stocks to sell based from the predicted price trend from the Machine Learning model
"""
class Sell(Document):
    # Stock Symbol refers to the stock symbol of the stock
    stock_symbol =  StringField()
    # Last Closing refers to the last closing price of the stock
    last_closing =  FloatField()
    # Predicted Closing is a list of predicted closing prices for the stock
    predicted_closing = ListField()

    # When putting data to the "Sell" collection, the data will be in this format
    def from_json(self, json_data):
        self.stock_symbol = json_data.get("stock_symbol")
        self.last_closing = json_data.get("last_closing")
        self.predicted_closing = json_data.get("predicted_closing")

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "predicted_closing": self.predicted_closing
        }


# Define class "Info" and inherit from "Document"
"""
About the Info class:
    - This class is used to define the structure of the "info" collection in the MongoDB database
    - This document contains the general information of the stocks included in the Philippine Stock Market Price Trend Forecasting System
"""
class Info(Document):
    # Stock Symbol refers to the stock symbol of the stock
    stock_symbol =  StringField()
    # Stock Name refers to the name of the company
    stock_name = StringField()
    # Comapany Site refers to the company's website
    company_site = StringField()
    # Company Address refers to the company's address
    company_address = StringField()
    # Company E-mail refers to the company's e-mail address
    company_email = StringField()
    # Company Phone refers to the company's phone number
    company_phone = IntField()
    # Sector refers to the sector of the company
    sector = StringField()
    # Industry refers to the industry of the company
    industry = StringField()
    # Key Executives is a  list of tuples of the key executives of the company and their positions
    key_executives = ListField()

    def from_json(self, json_data):
        self.stock_symbol = json_data.get("stock_symbol")
        self.stock_name = json_data.get("stock_name")
        self.company_site = json_data.get("company_site")
        self.company_address = json_data.get("company_address")
        self.company_email = json_data.get("company_email")
        self.company_phone = json_data.get("company_phone")
        self.sector = json_data.get("sector")
        self.industry = json_data.get("industry")
        self.key_executives = json_data.get("key_executives")
    
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "stock_name": self.stock_name,
            "company_site": self.company_site,
            "company_address": self.company_address,
            "company_email": self.company_email,
            "company_phone": self.company_phone,
            "sector": self.sector,
            "industry": self.industry,
            "key_executives": self.key_executives
        }