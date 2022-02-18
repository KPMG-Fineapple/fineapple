# %%
# import json
# import pandas as pd

# from preprocess import consumption  # import UserConsumption
# from model.consumption import predict_xgboost

from model.consumption import predict_xgboost
from preprocess import consumption  # import UserConsumption
import pandas as pd
import json
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning) 

# %%


def load_current() -> list:
    # -- current -- #
    PATH = "../AI/data/private/PowerConsumption/"
    User = consumption.UserConsumption(PATH)
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
    # consumption = {
    #     "current": [
    #         {
    #             "date": "2021.2",
    #             "value": [5, 2, 5, 7, 3, 6, 4, 1, 3, 7, 9, 8, 7, 6, 5, 5, 7, 1, 4, 6, 3, 1, 1, 2, 7, 6, 3, 1]
    #         },
    #         {
    #             "date": "2021.3",
    #             "value": [7, 5, 8, 2, 7, 7, 4, 8, 4, 8, 3, 3, 9, 0, 4, 6, 7, 0, 8, 2, 8, 5, 6, 8, 5, 5, 4, 9, 9, 3, 8]
    #         },
    #         {
    #             "date": "2021.4",
    #             "value": [8, 3, 9, 7, 8, 1, 8, 7, 9, 2, 1, 4, 7, 4, 8, 3, 7, 8, 9, 0, 5, 6, 1, 0, 3, 8, 8, 1, 8, 9],
    #         },
    #         {
    #             "date": "2021.5",
    #             "value": [7, 8, 4, 9, 3, 8, 2, 2, 4, 6, 3, 5, 5, 6, 7, 7, 2, 3, 1, 6, 1, 2, 0, 4, 0, 6, 0, 5, 4, 4, 9],
    #         },
    #         {
    #             "date": "2021.6",
    #             "value": [8, 3, 9, 7, 8, 1, 8, 7, 9, 2, 1, 4, 7, 4, 8, 3, 7, 8, 9, 0, 5, 6, 1, 0, 3, 8, 8, 1, 8, 9],
    #         },
    #         {
    #             "date": "2021.7",
    #             "value": [8, 6, 6, 3, 1, 8, 7, 2, 2, 6, 1, 9, 3, 3, 5, 7, 1, 7, 1, 4, 7, 9, 3, 7, 1, 0, 4, 6, 0, 0, 1],
    #         },
    #         {
    #             "date": "2021.8",
    #             "value": [2, 8, 7, 5, 9, 7, 5, 8, 4, 1, 1, 5, 8, 8, 5, 9, 6, 6, 9, 0, 8, 9, 1, 1, 2, 4, 4, 1, 4, 3, 8]
    #         },
    #         {
    #             "date": "2021.9",
    #             "value": [8, 3, 9, 7, 8, 1, 8, 7, 9, 2, 1, 4, 7, 4, 8, 3, 7, 8, 9, 0, 5, 6, 1, 0, 3, 8, 8, 1, 8, 9],
    #         },
    #         {
    #             "date": "2021.10",
    #             "value": [2, 0, 7, 0, 8, 1, 0, 2, 3, 5, 9, 7, 5, 4, 1, 5, 5, 3, 9, 4, 9, 0, 7, 9, 5, 0, 2, 1, 7, 9, 3],
    #         },
    #         {
    #             "date": "2021.11",
    #             "value": [
    #                 10, 10, 10, 10, 10, 10, 10,
    #                 10, 10, 10, 10, 10, 10, 10,
    #                 10, 10, 10, 10, 10, 10, 10,
    #                 10, 10, 10, 10, 10, 10, 10,
    #                 10, 10
    #             ],
    #         },
    #         {
    #             "date": "2021.12",
    #             "value": [4, 1, 5, 3, 0, 6, 8, 7, 2, 2, 3, 0, 1, 0, 4, 7, 1, 5, 2, 3, 2, 2, 2, 1, 9, 5, 8, 2, 9, 6, 7],
    #         },
    #         {
    #             "date": "2022.1",
    #             "value": [2, 9, 2, 5, 7, 1, 5, 5, 4, 7, 6, 3, 1, 0, 6, 0, 4, 2, 5, 7, 0, 4, 4, 2, 0, 2, 5, 2, 1, 5, 6],
    #         }
    #     ],
    #     "predict": [
    #         {
    #             "date": "2022.2",
    #             "value": [1, 8, 9, 0, 0, 5, 6, 2, 2, 6, 0, 2, 6, 0, 3, 8, 2, 9, 3, 3, 8, 1, 9, 6, 7, 3, 0, 1],
    #         },
    #         {
    #             "date": "2022.3",
    #             "value": [5, 9, 9, 4, 7, 3, 5, 0, 2, 1, 2, 6, 9, 6, 4, 7, 0, 0, 3, 9, 7, 4, 0, 0, 1, 3, 8, 1, 2, 7, 4],
    #         },
    #         {
    #             "date": "2022.4",
    #             "value": [3, 4, 9, 3, 3, 7, 9, 6, 3, 6, 7, 7, 1, 7, 7, 0, 1, 7, 5, 6, 8, 1, 5, 2, 9, 5, 2, 6, 2, 3],
    #         },
    #         {
    #             "date": "2022.5",
    #             "value": [5, 5, 4, 2, 1, 9, 3, 4, 0, 7, 2, 4, 8, 9, 0, 9, 0, 2, 7, 5, 1, 5, 7, 8, 9, 7, 3, 2, 2, 5, 3],
    #         },
    #         {
    #             "date": "2022.6",
    #             "value": [6, 6, 3, 3, 1, 0, 9, 5, 6, 3, 4, 8, 2, 1, 1, 1, 3, 4, 0, 1, 2, 6, 2, 7, 8, 5, 9, 8, 8, 0],
    #         },
    #         {
    #             "date": "2022.7",
    #             "value": [4, 3, 4, 8, 8, 3, 3, 9, 5, 2, 8, 5, 7, 4, 3, 0, 8, 4, 4, 6, 2, 6, 9, 4, 0, 7, 4, 0, 7, 3, 0],
    #         },
    #         {
    #             "date": "2022.8",
    #             "value": [2, 0, 7, 9, 9, 3, 6, 1, 8, 3, 4, 3, 3, 3, 2, 0, 5, 1, 1, 1, 9, 1, 5, 1, 0, 1, 3, 4, 3, 3, 1],
    #         },
    #         {
    #             "date": "2022.9",
    #             "value": [5, 1, 9, 3, 3, 0, 5, 7, 2, 8, 2, 0, 1, 7, 9, 8, 8, 5, 3, 6, 8, 5, 9, 3, 0, 0, 7, 9, 3, 4],
    #         },
    #         {
    #             "date": "2022.10",
    #             "value": [5, 0, 7, 4, 2, 5, 7, 7, 3, 8, 7, 1, 3, 5, 8, 1, 3, 5, 3, 7, 0, 8, 4, 7, 6, 9, 5, 5, 0, 2, 5],
    #         },
    #         {
    #             "date": "2022.11",
    #             "value": [5, 3, 6, 7, 9, 8, 9, 5, 2, 9, 5, 0, 8, 6, 4, 3, 5, 3, 3, 6, 2, 1, 0, 4, 4, 3, 5, 8, 1, 0],
    #         },
    #         {
    #             "date": "2022.12",
    #             "value": [6, 3, 3, 8, 3, 9, 7, 5, 2, 1, 4, 3, 5, 4, 8, 9, 7, 2, 1, 9, 9, 9, 1, 9, 7, 8, 9, 0, 8, 7, 0],
    #         },
    #         {
    #             "date": "2023.1",
    #             "value": [5, 0, 7, 7, 0, 6, 1, 0, 9, 4, 2, 5, 8, 5, 2, 4, 1, 5, 5, 3, 5, 1, 5, 5, 3, 7, 9, 2, 4, 1, 2],
    #         }
    #     ]}
    print(json.dumps(consumption))


# %%

if __name__ == "__main__":
    predict_consumption()

# %%