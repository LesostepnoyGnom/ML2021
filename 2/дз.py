# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 21:39:30 2021

@author: 1618047
"""

from sklearn.datasets import load_boston
from matplotlib import pyplot as plt

boston = load_boston()
print(boston['DESCR'])

X, y = boston['data'], boston['target']

plt.scatter(X[:,0], y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.neighbors import KNeighborsRegressor

# Создаём объект
knn = KNeighborsRegressor(n_neighbors=5, weights='uniform', p=2) # Все веса одинаковы независиом от удалённости объектов

knn.fit(X_train, y_train) # создаём модель

print(knn.predict(X_test))

from sklearn.metrics import mean_squared_error

print(mean_squared_error(y_test, knn.predict(X_test))) # Ошибка

from sklearn.model_selection import GridSearchCV
grid_searcher = GridSearchCV(KNeighborsRegressor(),
             param_grid={
                 'n_neighbors': [1, 2,3,4,5,6,7,8,9,10],
                 'weights': ['uniform', 'distance'],
                 'p': [1,2,3]
            },
            cv=5
        )

grid_searcher.fit(X_train, y_train)
grid_searcher.best_params_
print(grid_searcher.best_params_) # находит лучшие параметры

grid_searcher.predict(X_test)
print(grid_searcher.predict(X_test))

print('mse', mean_squared_error(y_test, grid_searcher.predict(X_test)))

metrics = []

for n in range(1, 30, 3):
    knn = KNeighborsRegressor(n_neighbors=n)
    knn.fit(X_train, y_train)
    metrics.append(mean_squared_error(y_test, knn.predict(X_test)))

fig, ax = plt.subplots(figsize=(8, 5), dpi=300)
plt.plot(range(1,30,3), metrics)

