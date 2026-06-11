from scipy.optimize import root
import numpy as np
import matplotlib.pyplot as plt

def eqn(x):
  return x + np.cos(x)

myroot = root(eqn, 0)

print(myroot)

from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
newArr = csr_matrix(arr).tocsc()
print(newArr)


from scipy.spatial import Delaunay
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])

simplices = Delaunay(points).simplices

plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

# plt.show()

from scipy import io

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

io.savemat('arr.mat', {"vec": arr})

mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])
