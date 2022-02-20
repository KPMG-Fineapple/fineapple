# -*- coding: utf-8 -*-
"""
Generation_data_2.ipynb

Automatically generated by Colaboratory.
"""

# %%
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.utils.data.dataset import random_split

import torch
import torch.nn as nn
import torch.optim as optim
import torch.functional as F
import openpyxl


# %%

def prepocess_67(loc_6, loc_7):
    loc_6.drop(["발전기명", "년월일", "설비용량(MW)", "01시", "02시", "03시",
               "04시", "05시", "24시"], axis=1, inplace=True)
    loc_7.drop(["발전기명", "년월일", "설비용량(MW)", "01시", "02시", "03시",
               "04시", "05시", "24시"], axis=1, inplace=True)

    loc_6.rename(columns={"06시": "6", "07시": "7", "08시": "8", "09시": "9", "10시": "10", "11시": "11", "12시": "12", "13시": "13",
                          "14시": "14", "15시": "15", "16시": "16", "17시": "17", "18시": "18", "19시": "19", "20시": "20", "21시": "21", "22시": "22", "23시": "23"}, inplace=True)

    loc_7.rename(columns={"06시": "6", "07시": "7", "08시": "8", "09시": "9", "10시": "10", "11시": "11", "12시": "12", "13시": "13",
                          "14시": "14", "15시": "15", "16시": "16", "17시": "17", "18시": "18", "19시": "19", "20시": "20", "21시": "21", "22시": "22", "23시": "23"}, inplace=True)
    loc_7.interpolate(method="linear", axis=1, inplace=True)

    return loc_6, loc_7


def drop_attributes(df):
    # dropping attributes
    df = df.drop(["구분", "총량", "평균", "최대", "최소", "최대(시간별)",
                 "최소(시간별)", "1", "2", "3", "4", "5", "24"], axis=1)
    return df


def drop_attributes(df):
    df = df.drop(["구분", "총량", "평균", "최대", "최소", "최대(시간별)",
                 "최소(시간별)", "1", "2", "3", "4", "5", "24"], axis=1)
    return df


def extract_hogi(df, num):
    df = df[df["호기"] == num]
    return df


def normalize_hogi(df):
    m = df.mean().mean()
    std = df.to_numpy().flatten().std()
    return (df-m)/std


def drop_attributes_w(df):
    df = df.drop(["지점", "지점명", "일사(MJ/m2)", "적설(cm)",
                 "운형(운형약어)", "현상번호(국내식)"], axis=1)
    df = df.fillna(0)
    return df


def drop_attributes_w1(df):
    df = df.drop(["지점", "지점명", "일사(MJ/m2)", "적설(cm)",
                 "운형(운형약어)", "지면상태(지면상태코드)"], axis=1)
    df = df.fillna(0)
    return df


def drop_time(df):
    for i in range(df["일시"].count()):
        time = int(df['일시'][i].split(":")[0].split()[1])
        if not(time >= 6 and time <= 23):
            df = df.drop(index=i, axis=1)
    return df


def lose_time(df):
    for i in range(df.shape[0]):
        df["month"][i] = int(df["일시"][i].split()[0].split("-")[1])
        df["time"][i] = int(df["일시"][i].split()[1].split(":")[0])
    df = df.drop(["일시"], axis=1)
    return df


def lose_time2(df):
    for i in range(df.shape[0]):
        df["month"][i] = int(df["일시"][i].split()[0].split(".")[1])
        df["time"][i] = int(df["일시"][i].split()[1].split(":")[0])
    df = df.drop(["일시"], axis=1)
    return df


def normalize_w(df):
    for idx, column in enumerate(df.columns[:7]):
        m = df[column].mean()
        s = df[column].std()
        df[column] = (df[column]-m)/s

    m = np.arange(1, 13).mean()
    s = np.arange(1, 13).std()
    df["month"] = (df["month"]-m)/s
    m = np.arange(0, 25).mean()
    s = np.arange(0, 25).std()
    df["time"] = (df["time"]-m)/s

    return df

# %%


def preprocess(BASEDIR_PATH):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    loc_1_1 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_1(삼천포)/loc_1_p_1.csv',
                          encoding='cp949')
    loc_1_2 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_1(삼천포)/loc_1_p_2.csv',
                          encoding='cp949')
    loc_2 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_2(본사사옥_진주)/loc2_p.csv',
                        encoding='cp949')
    loc_3 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_3(구미)/loc_3_p.csv',
                        encoding='cp949')
    loc_4 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_4(두산MG_창원)/loc_4_p.csv',
                        encoding='cp949')
    loc_5 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_5(농어촌공사 영암)/loc_5_p.csv',
                        encoding='cp949')
    loc_6 = pd.read_excel(
        BASEDIR_PATH + "/generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_p.xlsx", engine="openpyxl")
    loc_7 = pd.read_excel(
        BASEDIR_PATH + "/generation/PowerGeneration/loc_7(세종시매립장태양광)/loc_7_p.xlsx", engine="openpyxl")
    loc_1_w = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_1(삼천포)/loc_1_w.csv',
                          encoding='cp949')
    loc_2_w = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_2(본사사옥_진주)/loc2_w.csv',
                          encoding='cp949')
    loc_3_w = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_3(구미)/loc_3_w.csv',
                          encoding='cp949')
    loc_4_w = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_4(두산MG_창원)/loc_4_w.csv',
                          encoding='cp949')
    loc_5_w = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_5(농어촌공사 영암)/loc_5_w.csv',
                          encoding='cp949')

    loc_6_w_17 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_w_17.csv',
                             encoding='cp949')
    loc_6_w_18 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_w_18.csv',
                             encoding='cp949')
    loc_6_w_19 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_w_19.csv',
                             encoding='cp949')
    loc_6_w_20 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_w_20.csv',
                             encoding='cp949')
    loc_6_w_21 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_6(영암에프원태양광)/loc_6_w_21.csv',
                             encoding='cp949')

    loc_7_w_20 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_7(세종시매립장태양광)/loc_7_w_20.csv',
                             encoding='cp949')
    loc_7_w_21 = pd.read_csv(BASEDIR_PATH + 'generation/PowerGeneration/loc_7(세종시매립장태양광)/loc_7_w_21.csv',
                             encoding='cp949')

    loc_6.drop([364, 729, 1094, 1460], axis=0, inplace=True)
    loc_7.drop([365], axis=0, inplace=True)
    loc_6_n, loc_7_n = prepocess_67(loc_6, loc_7)
    loc_1_1_n = drop_attributes(loc_1_1)
    loc_1_2_n = drop_attributes(loc_1_2)
    loc_2_n = drop_attributes(loc_2)
    loc_3_n = drop_attributes(loc_3)
    loc_4_n = drop_attributes(loc_4)
    loc_5_n = loc_5.drop(["월", "일", " 계 ", " 1h ", " 2h ",
                         " 3h ", " 4h ", " 5h ", " 24h "], axis=1)
    loc_5_n.rename(columns={" 6h ": "6", " 7h ": "7", " 8h ": "8", " 9h ": "9", " 10h ": "10", " 11h ": "11",
                            " 12h ": "12", " 13h ": "13", " 14h ": "14", " 15h ": "15", " 16h ": "16", " 17h ": "17",
                            " 18h ": "18", " 19h ": "19", " 20h ": "20", " 21h ": "21", " 22h ": "22", " 23h ": "23"}, inplace=True)
    GenerationLoc_list = []  # 지역별로 hogi_list를 담는 list
    # GenerationLoc_list[location_num][hogi_num] = location_num번째 지역에 해당하는 hogi_num 번째 발전기의 발전량
    # LOC_1
    hogi_list = []  # 각 지역의 호기 list
    for i in range(1, 5):
        hogi_list.append(extract_hogi(loc_1_1_n, i))

    hogi_list.append(extract_hogi(loc_1_2_n, 1))
    hogi_list.append(extract_hogi(loc_1_2_n, 2))

    GenerationLoc_list.append(hogi_list)

    # LOC_2
    hogi_list = []
    hogi_list.append(extract_hogi(loc_2_n, 1))
    GenerationLoc_list.append(hogi_list)

    # LOC_3
    hogi_list = []
    hogi_list.append(extract_hogi(loc_3_n, 1))
    GenerationLoc_list.append(hogi_list)

    # LOC_4
    hogi_list = []
    hogi_list.append(extract_hogi(loc_4_n, 1))
    GenerationLoc_list.append(hogi_list)

    # LOC_5
    hogi_list = []
    hogi_list.append(loc_5_n)
    GenerationLoc_list.append(hogi_list)

    # LOC_6
    hogi_list = []
    hogi_list.append(loc_6_n)
    GenerationLoc_list.append(hogi_list)

    # LOC_7
    hogi_list = []
    hogi_list.append(loc_7_n)
    GenerationLoc_list.append(hogi_list)

    # 호기 cloumn drop
    for i in range(len(GenerationLoc_list[0])):
        GenerationLoc_list[0][i] = GenerationLoc_list[0][i].drop(
            ["호기", "년월일"], axis=1)

    GenerationLoc_list[1][0] = GenerationLoc_list[1][0].drop(
        ["호기", "년월일"], axis=1)
    GenerationLoc_list[2][0] = GenerationLoc_list[2][0].drop(
        ["호기", "년월일"], axis=1)
    GenerationLoc_list[3][0] = GenerationLoc_list[3][0].drop(
        ["호기", "년월일"], axis=1)

    GenerationLoc_list[4][0] = GenerationLoc_list[4][0].fillna(0)

    GenerationLoc_list_norm = []

    for i in range(len(GenerationLoc_list)):
        hogi_list_norm = []
        GenerationLoc_list_norm.append(hogi_list_norm)
        for hogi in GenerationLoc_list[i]:
            GenerationLoc_list_norm[i].append(normalize_hogi(
                hogi).set_index(np.arange(hogi.shape[0])))

    loc_1_w_n = drop_attributes_w(loc_1_w)
    loc_2_w_n = drop_attributes_w(loc_2_w)
    loc_3_w_n = drop_attributes_w(loc_3_w)
    loc_4_w_n = drop_attributes_w(loc_4_w)
    loc_5_w_n = loc_5_w.drop(
        ["지점", "지점명", "일사(MJ/m2)", "운형(운형약어)", "현상번호(국내식)"], axis=1)
    loc_5_w_n = loc_5_w_n.fillna(0)

    loc_6_w_17_n = drop_attributes_w1(loc_6_w_17)
    loc_6_w_18_n = drop_attributes_w1(loc_6_w_18)
    loc_6_w_19_n = loc_6_w_19.drop(
        ["지점", "지점명", "일사(MJ/m2)", "운형(운형약어)", "현상번호(국내식)"], axis=1)
    loc_6_w_19_n = loc_6_w_19_n.fillna(0)
    loc_6_w_20_n = drop_attributes_w1(loc_6_w_20)
    loc_6_w_21_n = drop_attributes_w1(loc_6_w_21)
    loc_7_w_20_n = drop_attributes_w(loc_7_w_20)
    loc_7_w_21_n = drop_attributes_w(loc_7_w_21)

    loc_1_w_n = drop_time(loc_1_w_n)
    loc_2_w_n = drop_time(loc_2_w_n)
    loc_3_w_n = drop_time(loc_3_w_n)
    loc_4_w_n = drop_time(loc_4_w_n)
    loc_5_w_n = drop_time(loc_5_w_n)
    loc_6_w_17_n = drop_time(loc_6_w_17_n)
    loc_6_w_18_n = drop_time(loc_6_w_18_n)
    loc_6_w_19_n = drop_time(loc_6_w_19_n)
    loc_6_w_20_n = drop_time(loc_6_w_20_n)
    loc_6_w_21_n = drop_time(loc_6_w_21_n)
    loc_7_w_20_n = drop_time(loc_7_w_20_n)
    loc_7_w_21_n = drop_time(loc_7_w_21_n)

    loc_1_w_n = loc_1_w_n.set_index(np.arange(loc_1_w_n.shape[0]))
    loc_2_w_n = loc_2_w_n.set_index(np.arange(loc_2_w_n.shape[0]))
    loc_3_w_n = loc_3_w_n.set_index(np.arange(loc_3_w_n.shape[0]))
    loc_4_w_n = loc_4_w_n.set_index(np.arange(loc_4_w_n.shape[0]))
    loc_5_w_n = loc_5_w_n.set_index(np.arange(loc_5_w_n.shape[0]))
    loc_6_w_17_n = loc_6_w_17_n.set_index(np.arange(loc_6_w_17_n.shape[0]))
    loc_6_w_18_n = loc_6_w_18_n.set_index(np.arange(loc_6_w_18_n.shape[0]))
    loc_6_w_19_n = loc_6_w_19_n.set_index(np.arange(loc_6_w_19_n.shape[0]))
    loc_6_w_20_n = loc_6_w_20_n.set_index(np.arange(loc_6_w_20_n.shape[0]))
    loc_6_w_21_n = loc_6_w_21_n.set_index(np.arange(loc_6_w_21_n.shape[0]))
    loc_7_w_20_n = loc_7_w_20_n.set_index(np.arange(loc_7_w_20_n.shape[0]))
    loc_7_w_21_n = loc_7_w_21_n.set_index(np.arange(loc_7_w_21_n.shape[0]))

    loc_1_w_n["month"] = np.zeros(3294)
    loc_1_w_n["time"] = np.zeros(3294)
    loc_2_w_n["month"] = np.zeros(2484)
    loc_2_w_n["time"] = np.zeros(2484)
    loc_3_w_n["month"] = np.zeros(3294)
    loc_3_w_n["time"] = np.zeros(3294)
    loc_4_w_n["month"] = np.zeros(3294)
    loc_4_w_n["time"] = np.zeros(3294)
    loc_5_w_n["month"] = np.zeros(6552)
    loc_5_w_n["time"] = np.zeros(6552)
    loc_6_w_17_n["month"] = np.zeros(len(loc_6_w_17_n))
    loc_6_w_17_n["time"] = np.zeros(len(loc_6_w_17_n))

    loc_6_w_18_n["month"] = np.zeros(len(loc_6_w_18_n))
    loc_6_w_18_n["time"] = np.zeros(len(loc_6_w_18_n))

    loc_6_w_19_n["month"] = np.zeros(len(loc_6_w_19_n))
    loc_6_w_19_n["time"] = np.zeros(len(loc_6_w_19_n))

    loc_6_w_20_n["month"] = np.zeros(len(loc_6_w_20_n))
    loc_6_w_20_n["time"] = np.zeros(len(loc_6_w_20_n))

    loc_6_w_21_n["month"] = np.zeros(len(loc_6_w_21_n))
    loc_6_w_21_n["time"] = np.zeros(len(loc_6_w_21_n))

    loc_7_w_20_n["month"] = np.zeros(len(loc_7_w_20_n))
    loc_7_w_20_n["time"] = np.zeros(len(loc_7_w_20_n))

    loc_7_w_21_n["month"] = np.zeros(len(loc_7_w_21_n))
    loc_7_w_21_n["time"] = np.zeros(len(loc_7_w_21_n))

    loc_1_w_n = lose_time(loc_1_w_n)
    loc_2_w_n = lose_time(loc_2_w_n)
    loc_3_w_n = lose_time(loc_3_w_n)
    loc_4_w_n = lose_time(loc_4_w_n)
    loc_5_w_n = lose_time(loc_5_w_n)
    loc_6_w_17_n = lose_time(loc_6_w_17_n)
    loc_6_w_18_n = lose_time(loc_6_w_18_n)
    loc_6_w_19_n = lose_time2(loc_6_w_19_n)
    loc_6_w_20_n = lose_time(loc_6_w_20_n)
    loc_6_w_21_n = lose_time(loc_6_w_21_n)
    loc_7_w_20_n = lose_time2(loc_7_w_20_n)
    loc_7_w_21_n = lose_time2(loc_7_w_21_n)

    loc_1_w_n = normalize_w(loc_1_w_n)
    loc_2_w_n = normalize_w(loc_2_w_n)
    loc_3_w_n = normalize_w(loc_3_w_n)
    loc_4_w_n = normalize_w(loc_4_w_n)
    loc_5_w_n = normalize_w(loc_5_w_n)
    loc_6_w_17_n = normalize_w(loc_6_w_17_n)
    loc_6_w_18_n = normalize_w(loc_6_w_18_n)
    loc_6_w_19_n = normalize_w(loc_6_w_19_n)
    loc_6_w_20_n = normalize_w(loc_6_w_20_n)
    loc_6_w_21_n = normalize_w(loc_6_w_21_n)
    loc_7_w_20_n = normalize_w(loc_7_w_20_n)
    loc_7_w_21_n = normalize_w(loc_7_w_21_n)

    print(loc_6_w_17_n.shape)
    print(loc_6_w_18_n.shape)
    print(loc_6_w_19_n.shape)
    print(loc_6_w_20_n.shape)
    print(loc_6_w_21_n.shape)
    print(loc_7_w_20_n.shape)
    print(loc_7_w_21_n.shape)

    GenerationLoc_list_norm_numpy = []
    for i in range(6):
        GenerationLoc_list_norm_numpy.append(
            GenerationLoc_list_norm[i][0].to_numpy().flatten())
        GenerationLoc_list_norm_numpy[i] = GenerationLoc_list_norm_numpy[i][:
                                                                            GenerationLoc_list_norm_numpy[i].shape[0]-18].reshape(-1, 1)
        print(GenerationLoc_list_norm_numpy[i].shape)

    y = np.concatenate((GenerationLoc_list_norm_numpy), axis=0)
    W_list_numpy = []
    W_list_numpy.append(loc_1_w_n.to_numpy())
    W_list_numpy.append(loc_2_w_n.to_numpy())
    W_list_numpy.append(loc_3_w_n.to_numpy())
    W_list_numpy.append(loc_4_w_n.to_numpy())
    W_list_numpy.append(loc_5_w_n.to_numpy())
    W_list_numpy.append(loc_6_w_17_n.to_numpy())
    W_list_numpy.append(loc_6_w_18_n.to_numpy())
    W_list_numpy.append(loc_6_w_19_n.to_numpy())
    W_list_numpy.append(loc_6_w_20_n.to_numpy())
    W_list_numpy.append(loc_6_w_21_n.to_numpy())
    # W_list_numpy.append(loc_7_w_20_n.to_numpy())
    # W_list_numpy.append(loc_7_w_21_n.to_numpy())
    x = np.concatenate((W_list_numpy), axis=0)

    # TO CSV
    np.save("power-generation-x", arr=x)
    np.save("power-generation-y", arr=y)


def load_npy():
    npy_x = np.load(
        file="AI/preprocess/power-generation/power-generation-x.npy")
    npy_y = np.load(
        file="AI/preprocess/power-generation/power-generation-y.npy")
    x = torch.tensor(npy_x, dtype=float)
    y = torch.tensor(npy_y, dtype=float)
    return x, y


# %%
if __name__ == "__main__":
    start = time.time()
    preprocess("AI/data/")
    # [preprocess] time : 42.225852966308594
    print("[preprocess] time :", time.time() - start)
    x, y = load_npy()
    print(x)
    print(y)

# %%

'''TEST LOG'''

# python AI/preprocess/power_generator.py

# (6552, 9)
# (6552, 9)
# (6552, 9)
# (6570, 9)
# (4356, 9)
# (6588, 9)
# (4356, 9)
# (3294, 1)
# (2484, 1)
# (3294, 1)
# (3294, 1)
# (6552, 1)
# (30582, 1)
# [preprocess] time : 42.225852966308594
# tensor([[ 0.3338, -0.1521,  0.3077,  ...,  0.0043,  0.1448, -0.8321],
#         [ 0.4630, -0.1521,  0.0916,  ...,  0.2882,  0.1448, -0.6934],
#         [ 0.6157, -0.1521, -0.1786,  ...,  0.7484,  0.1448, -0.5547],
#         ...,
#         [ 0.7647, -0.1388,  1.5226,  ...,  0.4699,  0.4345,  1.2481],
#         [ 0.7545, -0.1388,  1.5811,  ...,  0.4616,  0.4345,  1.3868],
#         [ 0.7647, -0.1388,  1.5226,  ...,  0.4533,  0.4345,  1.5254]],
#        dtype=torch.float64)
# tensor([[-0.7659],
#         [-0.7659],
#         [-0.4963],
#         ...,
#         [-0.8255],
#         [-0.8255],
#         [-0.8255]], dtype=torch.float64)