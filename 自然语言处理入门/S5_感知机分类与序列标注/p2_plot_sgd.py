# -*- coding:utf-8 -*-
# 《自然语言处理入门》5.2.4 损失函数与随机梯度下降
# 《自然语言处理入门》5.2.4 损失函数与随机梯度下降
import matplotlib.pyplot as plt
import numpy as np

from 自然语言处理入门.S5_感知机分类与序列标注.p1_plot_name import newline

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.linspace(-1.5, 1.5)
y = x ** 2

newline([1, 0], [1, 1], color='g')

plt.ylim([0, 2])

plt.plot(x, y)
plt.title('$J(w)=w^2$')
plt.xlabel('$w$')
plt.ylabel('$J(w)$')
plt.annotate('梯度$\Delta w = 2$', xy=(1, 1), xytext=(0, 1.0), ha='center',
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

bbox_props = dict(boxstyle="larrow", fc='w', ec="black", lw=2)
t = plt.text(0.6, 0.1, "梯度下降方向", ha="center", va="center", rotation=0,
             bbox=bbox_props)
bbox_props['boxstyle'] = 'rarrow'
plt.text(1.4, 0.1, "梯度上升方向", ha="center", va="center", rotation=0,
         bbox=bbox_props)

plt.show()


from sklearn.datasets import make_regression


def gradient_descent(x, y, theta_init, step=0.001, maxsteps=0, precision=0.001, ):
    costs = []
    m = y.size  # number of data points
    theta = theta_init
    history = []  # to store all thetas
    preds = []
    counter = 0
    oldcost = 0
    pred = np.dot(x, theta)
    error = pred - y
    currentcost = np.sum(error ** 2) / (2 * m)
    preds.append(pred)
    costs.append(currentcost)
    history.append(theta)
    counter += 1
    while abs(currentcost - oldcost) > precision:
        oldcost = currentcost
        gradient = x.T.dot(error) / m
        theta = theta - step * gradient  # update
        history.append(theta)

        pred = np.dot(x, theta)
        error = pred - y
        currentcost = np.sum(error ** 2) / (2 * m)
        costs.append(currentcost)

        if counter % 25 == 0: preds.append(pred)
        counter += 1
        if maxsteps:
            if counter == maxsteps:
                break

    return history, costs, preds, counter


x, y = make_regression(n_samples=100,
                       n_features=1,
                       n_informative=1,
                       noise=20,
                       random_state=2017)
x = x.flatten()

xaug = np.c_[np.ones(x.shape[0]), x]
theta_i = [-15, 40] + np.random.rand(2)
history, cost, preds, iters = gradient_descent(xaug, y, theta_i, step=0.1)
theta = history[-1]


def error(X, Y, THETA):
    return np.sum((X.dot(THETA) - Y) ** 2) / (2 * Y.size)


ms = np.linspace(theta[0] - 20, theta[0] + 20, 20)
bs = np.linspace(theta[1] - 40, theta[1] + 40, 40)

M, B = np.meshgrid(ms, bs)

zs = np.array([error(xaug, y, theta)
               for theta in zip(np.ravel(M), np.ravel(B))])
Z = zs.reshape(M.shape)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(M, B, Z, rstride=1, cstride=1, color='b', alpha=0.2)
ax.contour(M, B, Z, 20, alpha=0.5, offset=0, stride=30)

ax.set_xlabel('$w_1$')
ax.set_ylabel('$w_2$')
ax.set_zlabel('$J(w_1,w_2)$')
ax.view_init(elev=30., azim=30)
ax.plot([theta[0]], [theta[1]], [cost[-1]], markerfacecolor='r', markeredgecolor='r', marker='>', markersize=7)
ax.plot([history[0][0]], [history[0][1]], [cost[0]], markerfacecolor='r', markeredgecolor='r', marker='8', markersize=7)

ax.plot([history[0][0]], [history[0][1]], 0, markerfacecolor='r', markeredgecolor='r', marker='8',
        markersize=7)
ax.plot([t[0] for t in history], [t[1] for t in history], cost, markerfacecolor='r', markeredgecolor='r', marker='.',
        markersize=2)
ax.plot([t[0] for t in history], [t[1] for t in history], 0, markerfacecolor='r', markeredgecolor='r', marker='.',
        markersize=2)
ax.plot([history[-1][0]], [history[-1][1]], 0, markerfacecolor='r', markeredgecolor='r', marker='>',
        markersize=7)
plt.show()
