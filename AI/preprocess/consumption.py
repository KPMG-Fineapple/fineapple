# %%
# basic tools
import os
import glob

# preprocess
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# CONSTANT

# data path

# %%
class UserConsumption:
    def __init__(self, PATH):
        self.USER_PATH = PATH
    
    # 최종 값 - 시작 값 = 사용량이므로 사용량만 살림 -> 사용량은 3, 6, 9, 12, 15(끝)
    # ['전기', '수도', '온수', '가스', '열량'] 으로 rename
    # 마지막 두 행인 합계와 평균은 삭제
    def extract_realvalue(self, df:pd.DataFrame, columns:list) -> pd.DataFrame:
        df_realvalues = pd.DataFrame()
        leng = len(df.columns)
        for idx in range(leng):
            if idx % 3 == 0:
                column_index = idx//3
                df_realvalues[columns[column_index]] = df.iloc[3:-2, idx]
        return df_realvalues    # 사용량만 추출한 데이터 프레임


    def load_data(self, PATH:str, encoding_format:str='cp949') -> pd.DataFrame:
        # 엑셀 로드
        if PATH.endswith(".xls"):
            df_raw = pd.read_excel(PATH)
        # 지원하지 않는 확장자
        elif not PATH.endswith(".csv"):
            return "[ERROR: 파일확장자] xls 또는 csv 확장자 파일을 입력하세요."
        # csv 로드
        else:
            df_raw = pd.read_csv(PATH, encoding=encoding_format)

        # 가공: 사용량만 추출
        new_columns = ['datetime', '전기', '수도', '온수', '가스', '열량']
        df = UserConsumption.extract_realvalue(self, df_raw, new_columns)
        # datetime으로 변경, 시간은 무의미하므로 format으로 제거
        df['datetime'] = pd.to_datetime(df['datetime'].str.split(" ").str[0])

        # 가공: datetime 제외한 값 모두 float 변환
        # datetime은 index로 설정
        df.set_index('datetime', inplace=True)
        # 명목형 변수인 나머지 값들을 float 변환
        df = df.astype('float')
        # datetime 원상태로 돌림
        df.reset_index(inplace=True)

        return df

    # 전체 데이터 연결한 데이터프레임 생성
    def concat_dataframes(self) -> pd.DataFrame:
        PATH = self.USER_PATH
        df=pd.DataFrame()
        consumption_file_names = glob.glob(PATH + "**")
        for consumption_file_name in consumption_file_names:
            df_2 = UserConsumption.load_data(self, consumption_file_name)
            df = pd.concat([df,df_2],ignore_index=True)
        return df
# %%

TEST_PATH = "/Users/a4923/Desktop/repositories/fork_fineapple_ai/AI/data/private/PowerConsumption/세대별 기간별(107-2201 2018년01월01일 ∼2018년12월31일).xls"
User = UserConsumption('../data/private/PowerConsumption/')    # prophet.py 파일 기준으로 상대경로 입력
user_consumption = User.concat_dataframes()
user_consumption.info()

# temp = User.load_data(TEST_PATH).info()
# %%
