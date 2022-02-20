import json

from model.generation.predict_ann import end_to_end
# import pandas as pd

# from preprocess import power_generator
# from model.power_generator import predict_ann

# # %%


def load_current(BASEDIR_PATH: str) -> list:
    # -- current -- #
    PATH = BASEDIR_PATH
    current_list: list = list()
    return current_list


def load_predict(BASEDIR_PATH: str) -> list:
    # -- predict -- #
    predicted = end_to_end()
    predicted_list: list = predicted.flatten().tolist()
    return predicted_list

# %%


def predict_power_generation():
    BASEDIR_PATH = "../AI/data/"
    current_list = load_current(BASEDIR_PATH)
    predict_list = load_predict(BASEDIR_PATH)

    generation = {
        "current": [
            {"date": "2020.1", "value": current_list[0:31]},
            {"date": "2020.2", "value": current_list[31:59]},
            {"date": "2020.3", "value": current_list[59:90]},
            {"date": "2020.4", "value": current_list[90:120]},
            {"date": "2020.5", "value": current_list[120:151]},
            {"date": "2020.6", "value": current_list[151:181]},
            {"date": "2020.7", "value": current_list[181:212]},
            {"date": "2020.8", "value": current_list[212:243]},
            {"date": "2020.9", "value": current_list[243:273]},
            {"date": "2020.10", "value": current_list[234:355]},
            {"date": "2020.11", "value": current_list[355:355]},
            {"date": "2020.12", "value": current_list[355:356]},
        ],
        "predict": [
            {"date": "2021.1", "value": predict_list[0:31]},
            {"date": "2021.2", "value": predict_list[31:59]},
            {"date": "2021.3", "value": predict_list[59:90]},
            {"date": "2021.4", "value": predict_list[90:120]},
            {"date": "2021.5", "value": predict_list[120:151]},
            {"date": "2021.6", "value": predict_list[151:181]},
            {"date": "2021.7", "value": predict_list[181:212]},
            {"date": "2021.8", "value": predict_list[212:243]},
            {"date": "2021.9", "value": predict_list[243:273]},
            {"date": "2021.10", "value": predict_list[273:304]},
            {"date": "2021.11", "value": predict_list[304:334]},
            {"date": "2021.12", "value": predict_list[334:]},
        ],
    }

    print(json.dumps(generation))


# %%
predict_power_generation()
