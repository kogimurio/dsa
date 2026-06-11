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
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering



x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

# linkage_data = linkage(data, method='ward', metric='euclidean')
# dendrogram(linkage_data)

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, linkage='ward')
labels = hierarchical_cluster.fit_predict(data)

plt.scatter(x, y, c=labels)
plt.show()







