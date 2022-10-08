from mongoengine import Document, StringField, IntField, FloatField
# Models for the database in MongoDB

# NOTE: CONFIGURE SCHEMA, THIS IS FOR EXAMPLE ONLY
# Define class "Buy" and inherit from "Document"
class Buy(Document):
    stock_symbol = StringField()
    last_closing = FloatField()