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

# from preprocess.generation import power_generator
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


# %%
# spliting data #need y,x from generation module


def prepare_data(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    return X_train, y_train, X_test, y_test


# 모델


class Model3(nn.Module):
    def __init__(self, name="3layer", xdim=9, h1dim=32, h2dim=16, h3dim=8, ydim=1):
        super(Model3, self).__init__()
        self.name = name
        self.xdim = xdim
        self.h1dim = h1dim
        self.h2dim = h2dim
        self.h3dim = h3dim
        self.ydim = ydim
        self.linear1 = torch.nn.Linear(
            self.xdim, self.h1dim, dtype=float).to(device)
        self.linear2 = torch.nn.Linear(
            self.h1dim, self.h2dim, dtype=float).to(device)
        self.linear3 = torch.nn.Linear(
            self.h2dim, self.h3dim, dtype=float).to(device)
        self.linear4 = torch.nn.Linear(
            self.h3dim, self.ydim, dtype=float).to(device)
        self.init_param()

    def init_param(self):
        nn.init.kaiming_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)
        nn.init.kaiming_normal_(self.linear3.weight)
        nn.init.zeros_(self.linear3.bias)
        nn.init.kaiming_normal_(self.linear4.weight)
        nn.init.zeros_(self.linear4.bias)

    def forward(self, x):
        net = x
        net = self.linear1(net)
        net = torch.relu(net)
        net = self.linear2(net)
        net = torch.relu(net)
        net = self.linear3(net)
        net = torch.relu(net)
        outputs = self.linear4(net)
        # outputs = torch.sigmoid(net)
        return outputs


# 실행코드

def train_model(X_train, y_train, model):
    losses = []
    epochs = 50000
    criterion = torch.nn.MSELoss().to(device)
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
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


def load_npy():
    npy_x = np.load(
        file="../AI/preprocess/generation/power-generation-x.npy")
    npy_y = np.load(
        file="../AI/preprocess/generation/power-generation-y.npy")
    x = torch.tensor(npy_x, dtype=float)
    y = torch.tensor(npy_y, dtype=float)
    return x, y

# Model Save & Load
# https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-for-inference


def model_save(model, x, y, PATH="../AI/model/generation/ann_model_50k.pt"):
    X_train, y_train, X_test, y_test = prepare_data(x, y)
    train_model(X_train, y_train, model)
    torch.save(model.state_dict(), PATH)
    print("[Complete] Model Save")


def model_load(PATH="../AI/model/generation/ann_model_50k.pt"):
    # model = TheModelClass(*args, **kwargs)
    model = Model3(name="logistic_regression",
                   xdim=9, h1dim=32, h2dim=16, h3dim=8, ydim=1).to(device)
    model.load_state_dict(torch.load(PATH, map_location='cpu'))
    model.eval()
    return model
# %%

# RUN


def end_to_end(X_test):
    x, y = load_npy()
    X_train, y_train, _, _ = prepare_data(x, y)
    model = Model3(name="logistic_regression",
                   xdim=9, h1dim=32, h2dim=16, h3dim=8, ydim=1).to(device)
    model = model_load()
    print("[Complete] Model Load")
    predicted = predict(X_test, model)
    return predicted


# %%
if __name__ == "__main__":
    # load_data
    # x, y = load_npy()

    # # model load
    # result = end_to_end()

    # train
    # model = Model3(name="logistic_regression",
    #                xdim=9, h1dim=32, h2dim=16, h3dim=8, ydim=1.to(device)
    # model_save(model, x, y)
    None
