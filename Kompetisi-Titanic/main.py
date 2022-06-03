import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics

dataset_train = pd.read_csv('~/Desktop/mywork/Kaggle/dataset/titanic/train.csv')
dataset_test = pd.read_csv('~/Desktop/mywork/Kaggle/dataset/titanic/test.csv')
contoh_submission = pd.read_csv('~/Desktop/mywork/Kaggle/dataset/titanic/gender_submission.csv')

print(dataset_train)
