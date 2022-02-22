# %%

import numpy as np
import pandas as pd
import torch


# %%
# AI/power-generation-model.py

def load_npy():
    npy_x = np.load(
        file="../AI/preprocess/generation/power-generation-x.npy", allow_pickle=True)
    npy_y = np.load(
        file="../AI/preprocess/generation/power-generation-y.npy", allow_pickle=True)
    x = torch.tensor(npy_x, dtype=float)
    y = torch.tensor(npy_y, dtype=float)
    return x, y


def load_w20() -> pd.DataFrame:
    npy_w20 = np.load(
        file="../AI/preprocess/generation/W_list_numpy.npy",
        allow_pickle=True
    )
    w20 = pd.DataFrame(npy_w20[8])
    return w20

# 관측값 load


def load_generation() -> pd.DataFrame:
    npy_GenerationLoc_list_norm = np.load(
        file="../AI/preprocess/generation/GenerationLoc_list_norm.npy",
        allow_pickle=True)  # array(list())

    df_gen_19 = pd.DataFrame(
        npy_GenerationLoc_list_norm[5][0][728:1092].sum(axis=1))
    df_gen_20 = pd.DataFrame(
        npy_GenerationLoc_list_norm[5][0][1092:1457].sum(axis=1))

    return df_gen_19, df_gen_20

# %%

# 만약 모델 아웃풋이 cuda위에 있으면 predict.detach().cpu()실행


def change_time_to_day(predict: torch.tensor) -> np.ndarray:
    # predict = predict.detach().cpu()
    out = predict.detach().numpy().reshape(-1, 18)
    out = out.sum(axis=1)
    return out


# numpy input numpy output
def change_time_to_day_n(predict: np.ndarray) -> np.ndarray:
    out = predict.reshape(-1, 18)
    out = out.sum(axis=1)
    return out


def find_m_s(df):
    m = df.mean().mean()
    std = df.to_numpy().flatten().std()
    return m, std


def undo_norm(m: float, s: float, predict: torch.tensor) -> np.ndarray:
    #predict = predict.detach().cpu()
    out = predict.detach().numpy()
    out = out * s
    out = out + m
    return out

# %%


if __name__ == "__main__":
    None
