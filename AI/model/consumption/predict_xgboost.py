# %%
# load library
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# modules
from preprocess import asos
from preprocess import consumption

# %%


def split_dataset(dataset: pd.DataFrame, testset_size: float, do_shuffle: bool):
    df_y = dataset[["전력사용량"]]
    df_x = dataset.drop(["전력사용량", "일시"], axis=1)
    return train_test_split(df_x, df_y, test_size=testset_size, shuffle=do_shuffle)


# %%
# train


def train_xgboost(x_train: list, y_train: list, x_valid: list, y_valid: list) -> tuple:
    xgb_reg = XGBRegressor(n_estimators=50, learning_rate=0.01, seed=0)
    xgb_reg.fit(
        x_train,
        y_train,
        eval_set=[(x_train, y_train), (x_valid, y_valid)],
        early_stopping_rounds=300,
        verbose=False,
    )

    pred = xgb_reg.predict(x_valid)
    pred = pd.Series(pred)
    return xgb_reg, pred


# %%


def visual_xgboost(x_train: list, y_train: list, x_valid: list, y_valid: list) -> None:

    # load model, pred result
    # 함수에 입력한 dataset에 따라 train 후 모델과 예측값을 시각화 (plt)
    xgb_reg, pred = train_xgboost(x_train, y_train, x_valid, y_valid)

    # visualization
    fig = plt.figure(figsize=(12, 4))
    chart = fig.add_subplot(1, 1, 1)
    # series의 기존 인덱스가 시각화에 불필요하므로 `.reset_index()`
    y_valid_reset_index = y_valid["전력사용량"].reset_index()["전력사용량"]
    chart.plot(y_valid_reset_index[:-30], marker="o", color="blue", label="실제값")
    chart.plot(pred[:-30], marker="x", color="red", label="예측값")
    chart.set_title("XGBoost Predict", size=20)

    # best iteration
    print("best iterations: {}".format(xgb_reg.best_iteration))


# %%

# 모델 및 예측결과 반환
def run():
    dataset = asos.run()
    x_train, x_valid, y_train, y_valid = split_dataset(
        dataset, testset_size=0.2, do_shuffle=False
    )

    # TEST
    # xgb_reg, pred = train_xgboost(x_train, y_train, x_valid, y_valid)
    # print("[Complete!]")
    # print(pred)

    return train_xgboost(x_train, y_train, x_valid, y_valid)


# %%
