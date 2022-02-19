# %%
import time
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.utils.data.dataset import random_split

import torch
import torch.nn as nn
import torch.optim as optim
import torch.functional as F
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from preprocess import power_generator

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


# %%
# spliting data #need y,x from generation module


def prepare_data(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
    X_train = X_train.to(device)
    X_test = X_test.to(device)
    y_train = y_train.to(device)
    y_test = y_test.to(device)
    return X_train, y_train, X_test, y_test


# 모델


class Model1(nn.Module):
    def __init__(self, name="logistic_regression", xdim=9, hdim=13, ydim=1):
        super(Model1, self).__init__()
        self.name = name
        self.xdim = xdim
        self.hdim = hdim
        self.ydim = ydim
        self.linear1 = torch.nn.Linear(
            self.xdim, self.hdim, dtype=float).to(device)
        self.linear2 = torch.nn.Linear(
            self.hdim, self.ydim, dtype=float).to(device)
        self.init_param()

    def init_param(self):
        nn.init.kaiming_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

    def forward(self, x):
        net = x
        net = self.linear1(net)
        net = torch.relu(net)
        outputs = self.linear2(net)
        # outputs = torch.sigmoid(net)
        return outputs


# 실행코드

def train_model(X_train, y_train, model):
    losses = []
    epochs = 50000
    criterion = torch.nn.MSELoss().to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)
    losses_test = []
    Iterations = []
    iter = 0
    for epoch in tqdm(range(int(epochs)), desc='Training Epochs'):
        x = X_train
        labels = y_train
        optimizer.zero_grad()  # Setting our stored gradients equal to zero
        outputs = model(X_train)
        # loss
        loss = criterion(outputs, labels)
        losses.append(loss)
        loss.backward()  # Computes the gradient of the given tensor w.r.t. the weights/bias

        optimizer.step()  # Updates weights and biases with the optimizer (SGD)


def predict(X, model):
    return model(X)

# %%


# Model Save & Load
# https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-for-inference


def model_save(model, x, y, PATH="AI/model/power_generator/ann_model.pt"):
    X_train, y_train, X_test, y_test = prepare_data(x, y)
    train_model(X_train, y_train, model)
    torch.save(model.state_dict(), PATH)
    print("[Complete] Model Save")


def model_load(PATH="AI/model/power_generator/ann_model.pt"):
    # model = TheModelClass(*args, **kwargs)
    model = Model1(name="logistic_regression",
                   xdim=9, hdim=17, ydim=1).to(device)
    model.load_state_dict(torch.load(PATH))
    model.eval()
    return model
# %%

# RUN


def end_to_end(x, y):
    X_train, y_train, X_test, y_test = prepare_data(x, y)
    model = Model1(name="logistic_regression",
                   xdim=9, hdim=17, ydim=1).to(device)
    model = model_load()
    print("[Complete] Model Load")
    predicted = predict(X_test, model)
    print(type(predicted), predicted)
    return predicted


# %%
if __name__ == "__main__":
    # preprocess에 시간이 너무 오래 걸리는 문제
    start = time.time()
    x, y = power_generator.generator_preprocess()
    # [preprocess] time : 168.9127242565155
    print("[preprocess] time :", time.time() - start)

    # model load
    start = time.time()
    result = end_to_end(x, y)
    print(result)
    # [load] time : 0.0028848648071289062
    print("[load] time :", time.time() - start)

    # train
    # model = Model1(name="logistic_regression",
    #                xdim=9, hdim=17, ydim=1).to(device)
    # model_save(model, x, y)

# %%
