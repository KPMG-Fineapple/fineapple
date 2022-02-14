# %%
import json
import pandas as pd

from preprocess.consumption import UserConsumption
from model.consumption import predict_xgboost

# %%
def load_current() -> list:
    # -- current -- #
    PATH = "data/private/PowerConsumption/"
    User = UserConsumption(PATH)
    current: pd.DataFrame = User.load_data(
        PATH + "세대별 기간별(107-2201 2021년01월01일 ∼2021년12월31일).xls"
    )
    current_list: list = current["전기"].values.tolist()
    return current_list


def load_predict() -> list:

    # -- predict -- #
    _, predict = predict_xgboost.run()
    predict_list: list = predict.tolist()
    return predict_list


# %%
def predict_consumption():
    current_list = load_current()
    predict_list = load_predict()

    consumption = {
        "current": [
            {"date": "2021.1", "value": current_list[0:32]},
            {"date": "2021.2", "value": current_list[32:60]},
            {"date": "2021.3", "value": current_list[60:91]},
            {"date": "2021.4", "value": current_list[91:121]},
            {"date": "2021.5", "value": current_list[121:152]},
            {"date": "2021.6", "value": current_list[152:182]},
            {"date": "2021.7", "value": current_list[182:213]},
            {"date": "2021.8", "value": current_list[213:244]},
            {"date": "2021.9", "value": current_list[244:274]},
            {"date": "2021.10", "value": current_list[274:305]},
            {"date": "2021.11", "value": current_list[305:335]},
            {"date": "2021.12", "value": current_list[335:336]},
        ],
        "predict": [
            {"date": "2022.1", "value": predict_list[0:32]},
            {"date": "2022.2", "value": predict_list[32:60]},
            {"date": "2022.3", "value": predict_list[60:91]},
            {"date": "2022.4", "value": predict_list[91:121]},
            {"date": "2022.5", "value": predict_list[121:152]},
            {"date": "2022.6", "value": predict_list[152:182]},
            {"date": "2022.7", "value": predict_list[182:213]},
            {"date": "2022.8", "value": predict_list[213:244]},
            {"date": "2022.9", "value": predict_list[244:274]},
            {"date": "2022.10", "value": predict_list[274:305]},
            {"date": "2022.11", "value": predict_list[305:335]},
            {"date": "2022.12", "value": predict_list[335:336]},
        ],
    }

    print(json.dumps(consumption))


# %%

if __name__ == "__main__":
    predict_consumption()

# %%
