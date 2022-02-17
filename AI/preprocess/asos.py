# %%
# basic tools
import glob

# basic tools for ML
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 외부 모듈
from preprocess.consumption import UserConsumption

# 과학적 표기법 해제
pd.options.display.float_format = "{:.5f}".format

# %%


class WeatherASOS:
    def __init__(self, PATH):
        self.USER_PATH = PATH

    def load_data(
        self, PATH: str, parse_cols: list = ["일시"], encoding_format: str = "cp949"
    ) -> pd.DataFrame:
        return pd.read_csv(PATH, parse_dates=parse_cols, encoding=encoding_format)

    # 전체 데이터 연결한 데이터프레임 생성
    def concat_dataframes(self) -> pd.DataFrame:
        PATH = self.USER_PATH
        df = pd.DataFrame()
        file_names = glob.glob(PATH + "**")
        for file_name in file_names:
            df_2 = self.load_data(PATH=file_name)
            df = pd.concat([df, df_2], ignore_index=True)
        return df


# %%


class PreprocessASOS:
    def __init__(self, ASOS_PATH: str, USER_PATH: str):
        self.ASOS_PATH = ASOS_PATH  # "../data/~" -> "/data/ASOS/seoul_day_108/"
        self.USER_PATH = USER_PATH  # '../data/~' -> "/data/private/PowerConsumption/"

    def pick_columns(self, col_names: list, df_asos: pd.DataFrame) -> pd.DataFrame:
        df_simple = df_asos[col_names]
        return df_simple

    def combine_consumption(
        self, df_origin, df_consumption: pd.DataFrame
    ) -> pd.DataFrame:
        temp_df = df_origin.copy()
        # y value: 전기 소비량 추가
        temp_df["전력사용량"] = df_consumption["전기"]
        # 생각이상으로 수도, 온수 사용량과 관계가 큰 것으로 보임 (상관관계 확인결과)
        other_consumption = df_consumption.copy().drop(["datetime", "전기"], axis=1)
        df_combined = pd.concat([temp_df, other_consumption], axis=1)
        return df_combined

    # ta: 기온, rh: 습도
    def add_comfort_information(
        self, df: pd.DataFrame, ta_column: str, rh_column: str
    ) -> pd.DataFrame:
        temp_df = df.copy()
        ta, rh = temp_df[ta_column], temp_df[rh_column]
        discomfort_information = (
            (9 / 5 * ta) - 0.55 * (1 - rh) * ((9 / 5 * ta) - 26) + 32
        )
        temp_df["불쾌지수"] = discomfort_information

        # ~ 20 : 0
        # 20 ~ 25 : 1 # 25 ~ : 2 -> 통합
        temp_df.loc[(temp_df["불쾌지수"] <= 20), "불쾌지수"] = 0
        temp_df.loc[(temp_df["불쾌지수"] > 20), "불쾌지수"] = 1
        return temp_df


# %%
# run


def run() -> pd.DataFrame:
    # consumption-xgboost에서 돌리므로 경로는 해당파일 기준으로 작성
    SEOUL_PATH_108 = "data/ASOS/seoul_day_108/"
    USER_PATH = "data/private/PowerConsumption/"

    Weather_instance = WeatherASOS(SEOUL_PATH_108)
    df_asos = Weather_instance.concat_dataframes()

    User_instance = UserConsumption(USER_PATH)
    df_consumption = User_instance.concat_dataframes()
    Asos_instance = PreprocessASOS(SEOUL_PATH_108, USER_PATH)

    # run
    col_names = [
        "일시",
        "평균기온(°C)",
        "최저기온(°C)",
        "평균 상대습도(%)",
        "평균 증기압(hPa)",
        "평균 중하층운량(1/10)",
        "최저 초상온도(°C)",
        "1.5m 지중온도(°C)",
    ]
    df_simple = Asos_instance.pick_columns(col_names, df_asos)
    df_combined = Asos_instance.combine_consumption(df_simple, df_consumption)
    df_added_comfort = Asos_instance.add_comfort_information(
        df_combined, ta_column="평균기온(°C)", rh_column="평균 상대습도(%)"
    )

    # 안쓰는 데이터 (사용완료) drop
    dataset = df_added_comfort.drop(
        ["평균기온(°C)", "평균 상대습도(%)", "평균 중하층운량(1/10)"], axis=1
    )

    return dataset


# %%

if __name__ == "__main__":
    run()
