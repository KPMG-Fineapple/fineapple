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

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

#spliting data #need y,x from generation module
def prepare_data(x,y): 
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

def train_model(X_train,y_train, model):
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

def end_to_end(x,y):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    X_train, y_train, X_test, y_test = prepare_data(x,y)
    model = Model1(name="logistic_regression", xdim=9, hdim=17, ydim=1).to(device)
    train_model(X_train, y_train, model)
    return predict(X_test,model)
    
#loss 시각화
# fig, axes = plt.subplots(1, 1, figsize=(10, 10))
# axes.plot(np.arange(1000), losses[:1000])
# plt.grid()

#train set predict 시각화
# predict = model(X_train).detach().cpu().numpy()
# fig, axes = plt.subplots(1, 1, figsize=(50, 10))
# axes.plot(np.arange(200), predict[:200])
# y_train_numpy = y_train.detach().cpu().numpy()
# axes.plot(np.arange(200), y_train_numpy[:200])
# axes.set_xlim(0, 200)

#test set predict 시각화
# predict = model(X_test).detach().cpu().numpy()
# fig, axes = plt.subplots(1, 1, figsize=(50, 10))
# axes.plot(np.arange(200), predict[:200])
# y_test_numpy = y_test.detach().cpu().numpy()
# axes.plot(np.arange(200), y_test_numpy[:200])
# axes.set_xlim(0, 200)

#test set error 시각화
# y_test_numpy = y_test.detach().cpu().numpy()    # 모델의 최종 반환값?
# loss = (-predict + y_test_numpy)/y_test_numpy*100
# fig, axes = plt.subplots(1, 1, figsize=(50, 10))
# axes.plot(np.arange(200), loss[:200])

# 피드백
# return이 모델의 최종 반환값 (예측값)이 되게 실행하는 함수 하나 더 추가
# 시각화 코드 들어간거 같은데 제거 또는 주석처리
# 그외 기능별로 묶어둘 것: 또는 주석으로 설명 -> 나 torch 안써서 100% 이해가 안되네
