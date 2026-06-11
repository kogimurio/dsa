import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


cars = pd.read_csv('car_data.csv')
ohe_cars = pd.get_dummies(cars[['Car']])
# print(ohe_cars.to_string())

X = pd.concat([cars[['Volume', 'Weight']], ohe_cars], axis=1)
y = cars['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

##predict the CO2 emission of a VW where the weight is 2300kg, and the volume is 1300cm3:
predicted = regr.predict([[2300, 1300,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
print(predicted)

colors = pd.DataFrame({'color': ['blue', 'red', 'green']})
dummies = pd.get_dummies(colors, drop_first=True)

print(dummies)

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# plt.scatter(x, y)
# plt.show()
data = list(zip(x, y))
inertias = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)
plt.plot(range(1, 11), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertial')
# plt.scatter(x, y, c=kmeans.labels_)
# plt.show()


