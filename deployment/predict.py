import numpy as np
import pandas as pd
import joblib

model = joblib.load('models/TMDB_rf.joblib')

def get_form_data(data):
    feature_values = {
        'budget': 0,
        'popularity': 0,
        'runtime': 0, 
        'has_collection': 0,
        'has_homepage': 0,
        'is_en_original_language': 0,
        'crew_count':0,
        'cast_count':0,
        'produced_US':0,
        'collection_and_homepage': 0
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
    return feature_values

def predict(data, debug=False):
    values = get_form_data(data)

    if debug: print(f'Feature values: {values}\n')

    colums_order = ['budget', 'popularity', 'runtime', 'has_collection', 'has_homepage', 'is_en_original_language', 
    'crew_count', 'cast_count', 'produced_US', 'collection_an_homepage']

    values = np.array([values[feature] for feature in colums_order], dtype=object)

    if debug:
        print('ordered feature values: ')
        print(list(zip(colums_order, values)))

    pred = model.predict(values.reshape(1,-1))
    return str(pred[0])