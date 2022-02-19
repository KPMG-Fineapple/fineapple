# %%
# load library
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

# modules
from preprocess.consumption.run import run as load_dataset

# %%
# train


def split_dataset(dataset: pd.DataFrame, testset_size: float, do_shuffle: bool):
    df_y = dataset[["전력사용량"]]
    df_x = dataset.drop(["전력사용량", "일시"], axis=1)
    return train_test_split(df_x, df_y, test_size=testset_size, shuffle=do_shuffle)


def train_xgboost(dataset: pd.DataFrame, params_n_estimators, params_learning_rate, params_early_stopping_rounds, x_test) -> tuple:
    # training set
    x_train, x_valid, y_train, y_valid = split_dataset(
        dataset, testset_size=0.2, do_shuffle=False)

    # model
    xgb_reg = XGBRegressor(n_estimators=params_n_estimators,
                           learning_rate=params_learning_rate,
                           seed=0)

    # train
    xgb_reg.fit(
        x_train,
        y_train,
        eval_set=[(x_train, y_train), (x_valid, y_valid)],
        early_stopping_rounds=params_early_stopping_rounds,
        verbose=False,
    )

    x_test.drop("일시", axis=1, inplace=True)   # 학습에서 '일시' 사용하지 않으므로 drop
    pred = xgb_reg.predict(x_test)
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
    chart.plot(y_valid_reset_index[:-30],
               marker="o", color="blue", label="실제값")
    chart.plot(pred[:-30], marker="x", color="red", label="예측값")
    chart.set_title("XGBoost Predict", size=20)

    # best iteration
    print("best iterations: {}".format(xgb_reg.best_iteration))


# %%

# 모델 및 예측결과 반환
def run(BASEDIR_PATH, n_estimators, learning_rate, early_stopping_rounds, x_test):

    # train dataset
    dataset = load_dataset(BASEDIR_PATH)

    # hypter parameters
    return train_xgboost(dataset, n_estimators, learning_rate, early_stopping_rounds, x_test)


# %%
