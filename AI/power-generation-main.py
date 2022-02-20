import json

import numpy as np
import pandas as pd
import torch

from model.generation.predict_ann import end_to_end
# import pandas as pd

# from preprocess import power_generator
# from model.power_generator import predict_ann
from preprocess.generation import run as generation_preprocess
from sklearn.metrics import mean_squared_error

# # %%

# 2019


def load_current(BASEDIR_PATH: str) -> list:
    # -- current -- #
    PATH = BASEDIR_PATH
    df_gen_19, _ = generation_preprocess.load_generation()
    m, std = generation_preprocess.find_m_s(df_gen_19)
    current_list: list = df_gen_19[0].tolist()
    return current_list, m, std


def load_predict(BASEDIR_PATH: str, m, std) -> list:
    X_test = generation_preprocess.load_w20().values.tolist()
    X_torch = torch.tensor(X_test, dtype=torch.double)

    # -- predict -- #
    predicted: torch.tensor = end_to_end(X_torch)

    # -- undo norm -- #
    predicted_unnorm: np.ndarray = generation_preprocess.undo_norm(
        m, std, predicted)

    # -- change time to day -- #
    predicted_by_day: np.ndarray = generation_preprocess.change_time_to_day_n(
        predicted_unnorm)

    # -- make it a list -- #
    predicted_list: list = predicted_by_day.tolist()

    return predicted_list


# %%
def loss(y, y_pred):
    # squared : bool, default=True
    # If True returns MSE value, if False returns RMSE value.
    RMSE = mean_squared_error(y, y_pred, squared=False)
    return RMSE
    # %%


def predict_power_generation():
    BASEDIR_PATH = "../AI/data/"
    current_list, m, std = load_current(BASEDIR_PATH)
    predict_list = load_predict(BASEDIR_PATH, m, std)

    generation = {
        "current": [
            {"date": "2019.1", "value": current_list[0:31]},
            {"date": "2019.2", "value": current_list[31:59]},
            {"date": "2019.3", "value": current_list[59:90]},
            {"date": "2019.4", "value": current_list[90:120]},
            {"date": "2019.5", "value": current_list[120:151]},
            {"date": "2019.6", "value": current_list[151:181]},
            {"date": "2019.7", "value": current_list[181:212]},
            {"date": "2019.8", "value": current_list[212:243]},
            {"date": "2019.9", "value": current_list[243:273]},
            {"date": "2019.10", "value": current_list[273:304]},
            {"date": "2019.11", "value": current_list[304:334]},
            {"date": "2019.12", "value": current_list[334:]},
        ],
        "predict": [
            # 2020년 윤년
            {"date": "2020.1", "value": predict_list[0:30]},
            {"date": "2020.2", "value": predict_list[30:58]},
            {"date": "2020.3", "value": predict_list[58:89]},
            {"date": "2020.4", "value": predict_list[89:119]},
            {"date": "2020.5", "value": predict_list[119:150]},
            {"date": "2020.6", "value": predict_list[150:180]},
            {"date": "2020.7", "value": predict_list[180:211]},
            {"date": "2020.8", "value": predict_list[211:242]},
            {"date": "2020.9", "value": predict_list[242:272]},
            {"date": "2020.10", "value": predict_list[272:303]},
            {"date": "2020.11", "value": predict_list[303:333]},
            {"date": "2020.12", "value": predict_list[333:]},
        ],
    }

    print(json.dumps(generation))

    # loss
    # _, y = generation_preprocess.load_generation()
    # print(loss(y, predict_list))


# %%

if __name__ == "__main__":
    predict_power_generation()
