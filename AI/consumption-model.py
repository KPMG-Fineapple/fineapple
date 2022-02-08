import json


def predict_consumption():
    consumption = {
        "jan": 67000,
    }

    print(json.dumps(consumption))

predict_consumption();