from mongoengine import Document, StringField, FloatField, ListField, IntField, DictField
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
    # Last Date refers to the last date of the stock
    last_date = StringField()
    # Predicted Closing is a dictionary of predicted closing prices for the stock with a specific ML model used
    predicted_closing = DictField()

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "last_date": self.last_date,
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
    # Last Date refers to the last date of the stock
    last_date = StringField()
    # Predicted Closing is a dictionary of predicted closing prices for the stock with a specific ML model used
    predicted_closing = DictField()

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing,
            "last_date": self.last_date,
            "predicted_closing": self.predicted_closing
        }



# Define class "Info" and inherit from "Document"
"""
About the Info class:
    - This class is used to define the structure of the "info" collection in the MongoDB database
    - This document contains the general information of the stocks included in the alamSYS
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

# Define "ML_Models_Info" and inherit from "Document"
"""
About the ML_Models_Info class:
    - This class is used to define the structure of the "ml_models_info" collection in the MongoDB database
    - This document contains the information of the Machine Learning models used in the alamSYS
"""
class ML_Models_Info(Document):
    model_name = StringField()
    model_description = StringField()
    model_scores = DictField()

    def to_json(self):
        return {
            "model_name": self.model_name,
            "model_description": self.model_description,
            "model_scores": self.model_scores
        }