# Database Intialization
import os
import pymongo
import json

def main():
    # This file will initialize the database connection, create the database and the collections if they don't exist
    # and will also create the indexes for the collections

    # Create a database (if it doesn't exist)
    db = pymongo.MongoClient(os.environ['MONGO_HOST'], int(os.environ['MONGO_PORT']))
    list_db = db.list_database_names()

    if os.environ['MONGO_INITDB_DATABASE'] not in list_db:
        db.create_collection(os.environ['MONGO_INITDB_DATABASE'])
        print("SMPTF Database created!")

    # Create a collection (if it doesn't exist)
    db = pymongo.MongoClient("mongodb://0.0.0.0:27017/").smptf
    list_collection = db.list_collection_names()
    collections = ["Buy", "Sell", "Info"]

    for collection in collections:
        if collection not in list_collection:
            db.create_collection(collection)
            print(f"{collection} collection successfully created!")

    # insert the documents in the collection

    # Info
    # Parse the json file
    info_dict = json.load(open("/API_DB_module/DB_model/json_data/stock_info.json", "r"))
    # Insert the documents in the collection
    if db.Info.count_documents({}) == 0:
        db.Info.insert_many(info_dict)
        print("Info collection successfully populated!")

    # Buy and Sell will be populated by the preprocessor module

if __name__ == "__main__":
    main()