import json


def predict_power_generation():
    consumption = {
        "jan": 67000,
    }

    print(json.dumps(consumption))

predict_power_generation();