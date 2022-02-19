# %%
import matplotlib.pyplot as plt
from model.consumption import predict_xgboost
from preprocess.consumption import user_consumption  # UserConsumption
from preprocess.consumption import weather_asos  # preprocess_test
import pandas as pd
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


# %%


def load_current(BASEDIR_PATH: str) -> list:
    # -- current -- #
    PATH = BASEDIR_PATH + "private/PowerConsumption/train/"
    Consumption_instance = user_consumption.UserConsumption(PATH)
    current: pd.DataFrame = Consumption_instance.load_data(
        # 2021 -> 2020
        PATH + "세대별 기간별(107-2201 2020년01월01일 ∼2020년12월31일).xls"
    )
    current_list: list = current["전기"].values.tolist()
    return current_list


def load_predict(BASEDIR_PATH: str) -> list:
    # -- predict -- #
    x_test = weather_asos.preprocess_test(BASEDIR_PATH)
    _, predicted = predict_xgboost.run(BASEDIR_PATH, x_test)

    predicted_list: list = predicted.tolist()
    return predicted_list

# %%


def load_2021(BASEDIR_PATH: str) -> list:
    # -- current -- #
    PATH = BASEDIR_PATH + "private/PowerConsumption/test/"
    Consumption_instance = user_consumption.UserConsumption(PATH)
    current: pd.DataFrame = Consumption_instance.load_data(
        # 2021
        PATH + "세대별 기간별(107-2201 2021년01월01일 ∼2021년12월31일).xls"
    )
    y_valid = current["전기"]
    return y_valid
# %%


def predict_consumption():
    BASEDIR_PATH = "../AI/data/"
    current_list = load_current(BASEDIR_PATH)
    predict_list = load_predict(BASEDIR_PATH)

    consumption = {
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
    print(json.dumps(consumption))

    # --- Visualization ---
    y_valid = load_2021(BASEDIR_PATH)
    pred = pd.Series(predict_list)
    predict_xgboost.visual_xgboost(y_valid, pred)


# %%

if __name__ == "__main__":
    predict_consumption()

# %%

# %%
