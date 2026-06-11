import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from sklearn import tree, metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score
import pandas as pd
import sys
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()


# x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# slope, intercept, r, p, stad_err = stats.linregress(x, y)

# def myfunc(x):
#     return slope * x + intercept

# mymodel = list(map(myfunc, x))

# speed = myfunc(10)
# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
# print(r)
# # print(p)
# # print(stad_err)
# print(speed)


# x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
# y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

# mymodel = np.poly1d(np.polyfit(x, y, 3))
# myline = np.linspace(1, 22, 100)

# plt.scatter(x, y)
# plt.plot(myline, mymodel(myline))
# plt.show()
# print(r2_score(y, mymodel(x)))
# speed = mymodel(17)
# print(speed)





# df = pd.read_csv('data.csv')
# X = df[['Weight', 'Volume']]
# y = df['CO2']

# regr = linear_model.LinearRegression()
# regr.fit(X, y)

# predictedCO2 = regr.predict([[3300, 1300]])
# print(predictedCO2)
# print(regr.coef_)

# scaledX = scale.fit_transform(X)
# print(scaledX)

# df = pd.read_csv('data.csv')
# X = df[['Weight', 'Volume']]
# y = df['CO2']

# regre = linear_model.LinearRegression()
# regre.fit(scaledX, y)

# scaled = scale.transform([[2300, 1.3]])
# predictedCO2 = regre.predict([scaled[0]])
# print(predictedCO2)


# np.random.seed(2)

# x = np.random.normal(3, 1, 100)
# y = np.random.normal(150, 40, 100) / x

# train_x = x[:80]
# train_y = y[:80]

# test_x = x[80:]
# test_y = y[80:]

# mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))
# myline = np.linspace(0, 6, 100)

# r2 = r2_score(test_y, mymodel(test_x))
# print(r2)
# print(mymodel(6))

# plt.scatter(train_x, train_y)
# plt.plot(myline, mymodel(myline))
# plt.show()

df = pd.read_csv("user_data.csv")
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {"YES": 1, "NO": 0}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']

# X = df[features]
# y = df['Go']

# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X, y)

# tree.plot_tree(dtree, feature_names=features, filled=True)

# plt.show()
# print(dtree.predict([[40, 10, 6, 1]]))


actual = np.random.binomial(1, 0.9, size = 1000)
predicted = np.random.binomial(1, 0.9, size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels= [0, 1])

cm_display.plot()
# plt.show()

accurancy = metrics.f1_score(actual, predicted)
print(accurancy)




