import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt



n = 10000
ratio = .95
n_0 = int((1-ratio) * n)
n_1 = int(ratio * n)

y = np.array([0] * n_0 + [1] * n_1)


# below are the probabilities obtained from a hypothetical model that always predicts the majority class
# probability of predicting class 1 is going to be 100%
y_proba = np.array([1]*n)
y_pred = y_proba > .5

print(f"accurancy score: {accuracy_score(y, y_pred)}")
cf_mat = confusion_matrix(y, y_pred)
print("Confusion matrix")
print(cf_mat)
print(f'class 0 accurancy: {cf_mat[0][0]/n_0}')
print(f'class 1 accurancy: {cf_mat[1][1]/n_1}')

# below are the probabilities obtained from a hypothetical model that doesn't always predict the mode

y_proba_2 = np.array(
    np.random.uniform(0, .7, n_0).tolist() +
    np.random.uniform(.3, 1, n_1).tolist()
)

y_pred_2 = y_proba_2 > .5
print(f"accurancy score:{accuracy_score(y, y_pred_2)}" )
cf_mat = confusion_matrix(y, y_pred_2)
print('Confusion matrix')
print(cf_mat)
print(f'class 0 accurancy: {cf_mat[0][0]/n_0}')
print(f'class 1 accurancy: {cf_mat[1][1]/n_1}')

def plot_roc_curve(true_y, y_prob_2):
    """
    plots the roc curve based of the probabilities
    """
    fpr, tpr, thresholds = roc_curve(true_y, y_prob_2)
    # plt.plot(fpr, tpr)
    # plt.xlabel('False Positive Rate')
    # plt.ylabel('True Positive Rate')
    # plt.show()
    
plot_roc_curve(y, y_proba_2)
print(f'model 2 AUC score: {roc_auc_score(y, y_proba_2)}')


n = 10000
y = np.array([0] * n + [1] * n)
y_prob_3 = np.array(
    np.random.uniform(.25, .5, n//2).tolist() +
    np.random.uniform(.3, .7, n).tolist() +
    np.random.uniform(.5, .75, n//2).tolist() 
)
y_prob_4 = np.array(
    np.random.uniform(0, .4, n//2).tolist() +
    np.random.uniform(.3, .7, n).tolist() +
    np.random.uniform(.6, 1, n//2).tolist() 
)

print(f"model 1 accurancy score: {accuracy_score(y, y_prob_3 >.5)}")
print(f"model 2 accurancy score: {accuracy_score(y, y_prob_4 >.5)}")

print(f'model 1 AUC score: {roc_auc_score(y, y_prob_3)}')
print(f'model 2 AUC score: {roc_auc_score(y, y_prob_4)}')

def plot_roc_curve(true_y, y_prob_4):
    """
    plots the roc curve based of the probabilities
    """
    fpr, tpr, thresholds = roc_curve(true_y, y_prob_4)
    plt.plot(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.show()
plot_roc_curve(y, y_prob_4)



