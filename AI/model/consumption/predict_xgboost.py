# %%
# load library
import os
import pandas as pd
import matplotlib.pyplot as plt

from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# modules
from preprocess.consumption.user_consumption import UserConsumption
from preprocess.consumption.run import run as load_dataset

# %%
# train


def split_dataset(dataset: pd.DataFrame, testset_size: float, do_shuffle: bool):
    df_y = dataset[["전력사용량"]]
    df_x = dataset.drop(["전력사용량", "일시"], axis=1)
    return train_test_split(df_x, df_y, test_size=testset_size, shuffle=do_shuffle)


def train_xgboost(dataset: pd.DataFrame, x_test):
    # training set
    x_train, x_valid, y_train, y_valid = split_dataset(
        dataset, testset_size=0.2, do_shuffle=False)

    # params
    params = {'booster':  ['gbtree', 'gblinear', 'dart'],
              'max_depth': [i for i in range(0, 20)],
              'subsample': [i*0.1 for i in range(0, 11)],
              'learning_rate': [0.01, 0.05, 0.1],
              'lambda': [i*0.1 for i in range(0, 11)],
              'alpha': [i*0.1 for i in range(0, 11)],
              'n_estimators': [i for i in range(100, 3000, 100)]}

    # Fitting 5 folds for each of 54 candidates, totalling 270 fits
    # Best parameters: {'colsample_bytree': 0.3, 'learning_rate': 0.05, 'max_depth': 3, 'n_estimators': 100}
    # Lowest RMSE:  7.0607787236388955

    # model
    xgb_reg = XGBRegressor(seed=0)

    # Grid Search CV
    clf = GridSearchCV(estimator=xgb_reg,
                       param_grid=params,
                       scoring='neg_mean_squared_error',
                       verbose=1)
    clf.fit(x_train, y_train)
    print("Best parameters:", clf.best_params_)
    print("Lowest RMSE: ", (-clf.best_score_)**(1/2.0))

    # train
    xgb_reg.fit(
        x_train,
        y_train,
        colsample_bytree=0.3,
        learning_rate=0.05,
        max_depth=3,
        n_estimators=100,
        eval_set=[(x_train, y_train), (x_valid, y_valid)],
        verbose=False,
    )

    x_test.drop("일시", axis=1, inplace=True)   # 학습에서 '일시' 사용하지 않으므로 drop
    pred = xgb_reg.predict(x_test)
    pred = pd.Series(pred)
    return xgb_reg, pred

# %%


def visual_xgboost(y_valid, pred) -> None:
    fig = plt.figure(figsize=(12, 4))
    chart = fig.add_subplot(1, 1, 1)
    chart.plot(y_valid, marker="o", color="blue", label="실제값")
    chart.plot(pred, marker="x", color="red", label="예측값")
    chart.set_title("XGBoost Predict", size=20)


# %%

# 모델 및 예측결과 반환
def run(BASEDIR_PATH, x_test):

    # train dataset
    dataset = load_dataset(BASEDIR_PATH)

    # hypter parameters
    return train_xgboost(dataset, x_test)
