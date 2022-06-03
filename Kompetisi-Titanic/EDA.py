import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


dataset = pd.read_csv('~/Desktop/mywork/Kaggle/dataset/titanic/train.csv')

sns.scatterplot(x='Age', y='Fare', data=dataset)
plt.show()
