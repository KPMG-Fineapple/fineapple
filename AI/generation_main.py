# %%
# library, modules
import json
import pandas as pd

# %%


def load_current() -> list:     # 지난 일년치 (2021년)
    # -- current -- #
    PATH = ""
    current: pd.DataFrame = pd.DataFrame()  # 경로로 일년 발전량 가져오기
    current_list: list = current.values.tolist()
    return current_list


def load_predict() -> list:     # 일년치 (2022년)
    # -- predict -- #
    predict_list: list = list()
    return predict_list


def predict_power_generation():
    current_list = load_current()
    predict_list = load_predict()

    generation = {
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

    print(json.dumps(generation))

# %%


if __name__ == "__main__":
    predict_power_generation()
