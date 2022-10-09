from mongoengine import Document, StringField, IntField, FloatField
# Models for the database in MongoDB

# NOTE: CONFIGURE SCHEMA, THIS IS FOR EXAMPLE ONLY
# Define class "Buy" and inherit from "Document"
class Buy(Document):
    stock_symbol =  StringField()
    last_closing =  FloatField()

    # When putting data to the "Buy" collection, the data will be in this format
    def from_json(self, json_data):
        self.stock_symbol = json_data.get("stock_symbol")
        self.last_closing = json_data.get("last_closing")

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing
        }
    
# Define class "Sell" and inherit from "Document"
class Sell(Document):
    stock_symbol =  StringField()
    last_closing =  FloatField()

    # When putting data to the "Sell" collection, the data will be in this format
    def from_json(self, json_data):
        self.stock_symbol = json_data.get("stock_symbol")
        self.last_closing = json_data.get("last_closing")

    # Format the data to JSON
    def to_json(self):
        return {
            "stock_symbol": self.stock_symbol,
            "last_closing": self.last_closing
        }