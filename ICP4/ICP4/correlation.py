import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv('drive/My Drive/Colab Notebooks/train_preprocessed.csv')
train_df['Sex'] = train_df['Sex'].map({1: 'female', 0: 'male'})
train_df[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)

# plot graph
graph = sns.FacetGrid(train_df, col='Survived')
graph.map(plt.hist, 'Sex', bins=20)
plt.show()
