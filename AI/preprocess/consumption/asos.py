# %%
# basic tools
import glob

# basic tools for ML
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
    def __init__(self, ASOS_PATH: str):
        self.ASOS_PATH = ASOS_PATH

    def pick_columns(self, col_names: list, df_asos: pd.DataFrame) -> pd.DataFrame:
        df_simple = df_asos[col_names]
        return df_simple

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

    def drop_columns(self, df: pd.DataFrame):    # 안쓰는 데이터 (사용완료) drop
        temp_df = df.copy()
        temp_df.drop(["평균기온(°C)", "평균 상대습도(%)", "평균 중하층운량(1/10)"],
                     axis=1, inplace=True)
        return temp_df

# %%
# run


def run(BASEDIR_PATH: str) -> pd.DataFrame:
    SEOUL_PATH_108 = BASEDIR_PATH + "ASOS/train/seoul_day_108/"

    Weather_instance = WeatherASOS(SEOUL_PATH_108)
    df_asos = Weather_instance.concat_dataframes()
    Preprocessed_instance = PreprocessASOS(SEOUL_PATH_108)

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
    df_simple = Preprocessed_instance.pick_columns(col_names, df_asos)
    df_added_comfort = Preprocessed_instance.add_comfort_information(
        df_simple, ta_column="평균기온(°C)", rh_column="평균 상대습도(%)"
    )
    df_preprocessed = Preprocessed_instance.drop_columns(df_added_comfort)

    return df_preprocessed


# %%

if __name__ == "__main__":
    df = run("../../data/")
    df.info()

    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 1461 entries, 0 to 1460
    # Data columns (total 6 columns):
    # #   Column         Non-Null Count  Dtype
    # ---  ------         --------------  -----
    # 0   일시             1461 non-null   datetime64[ns]
    # 1   최저기온(°C)       1461 non-null   float64
    # 2   평균 증기압(hPa)    1461 non-null   float64
    # 3   최저 초상온도(°C)    1460 non-null   float64
    # 4   1.5m 지중온도(°C)  1459 non-null   float64
    # 5   불쾌지수           1461 non-null   float64

# %%
