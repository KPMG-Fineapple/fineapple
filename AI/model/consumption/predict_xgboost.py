# %%
# load library
import os
import pandas as pd

from tqdm import tqdm
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

# modules
from preprocess.consumption.user_consumption import UserConsumption
from preprocess.consumption.run import run as load_dataset


# visualize
import matplotlib.pyplot as plt
import xgboost as xgb
import matplotlib.pyplot as plt


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

    # params = {'colsample_bytree': 0.3, 'learning_rate': 0.05,
    #           'max_depth': 3, 'n_estimators': 100}

    # Fitting 5 folds for each of 54 candidates, totalling 270 fits
    # Best parameters: {'colsample_bytree': 0.3, 'learning_rate': 0.05, 'max_depth': 3, 'n_estimators': 100}
    # Lowest RMSE:  7.0607787236388955

    # model
    xgb_reg = XGBRegressor(
        colsample_bytree=0.3,
        learning_rate=0.05,
        max_depth=3,
        n_estimators=100,
        seed=0)

    # Grid Search CV
    # clf = GridSearchCV(estimator=xgb_reg,
    #                    param_grid=params,
    #                    scoring='neg_mean_squared_error',
    #                    verbose=1)
    # clf.fit(x_train, y_train)
    # print("Best parameters:", clf.best_params_)
    # print("Lowest RMSE: ", (-clf.best_score_)**(1/2.0))

    # train
    xgb_reg.fit(
        x_train,
        y_train,
    )

    x_test.drop("일시", axis=1, inplace=True)   # 학습에서 '일시' 사용하지 않으므로 drop
    pred = xgb_reg.predict(x_test)
    pred = pd.Series(pred)
    return xgb_reg, pred

# %%


def visual_xgboost(y_valid, pred, xgbr) -> None:
    fig = plt.figure(figsize=(12, 4))
    chart = fig.add_subplot(1, 1, 1)
    chart.plot(y_valid, marker="o", color="blue", label="실제값")
    chart.plot(pred, marker="x", color="red", label="예측값")
    chart.set_title("XGBoost Predict", size=20)

    # num_trees : 그림을 여러개 그릴시 그림 번호
    # rankdir : 트리의 방향, 디폴트는 위아래 방향
    # rankdir="LR" : 왼쪽에서 오른쪽 방향으로 트리를 보여준다.
    xgb.plot_importance(xgbr)
    xgb.plot_tree(xgbr, num_trees=0, rankdir='TB')

    fig = plt.gcf()
    fig.set_size_inches(150, 100)

    fig.savefig('xgboost_tree.png')

    plt.show()


# %%

# 모델 및 예측결과 반환
def run(BASEDIR_PATH, x_test):

    # train dataset
    dataset = load_dataset(BASEDIR_PATH)

    # hypter parameters
    return train_xgboost(dataset, x_test)
