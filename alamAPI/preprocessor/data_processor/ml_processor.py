import pickle
import pandas as pd
import json

class MLP:
    def load_model(model_path):
        model = pickle.load(open(model_path, 'rb'))
        return model

    def load_data(data_path):
        data = pd.read_csv(data_path)
        # return the number in data
        return data["number"][0]

    def process_data(data, model):
        # NOTE: FOR TESTING PURPOSES ONLY
        processed_data = { "data": data, "model": model }
        return processed_data

    def save_to_json(data, path):
        # Convert dict to json
        with open(path, 'a') as c:
            c.write("{" + f'"data": {data["data"]}, "model": "{data["model"]}"' + "},")


# TODO: load the model from the pickle file
model = MLP.load_model('ml_model/model.pkl')
# TODO: load the data from the csv file
data = MLP.load_data("ml_model/sample.csv")
# TODO: process the data
processed_data = MLP.process_data(data, model)
print(model)
print(data)
print(processed_data)
# TODO: save the data to the json files and put them in the json_data folder
MLP.save_to_json(processed_data, "json_data/data.json")