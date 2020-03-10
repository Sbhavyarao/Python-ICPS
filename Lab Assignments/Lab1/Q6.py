import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn import metrics

sns.set(style="white", color_codes=True)

#reading the data CC.csv
dataset = pd.read_csv('CC.csv')
# dataset.drop(["CREDIT_LIMIT"], axis=1, inplace=True)
x = dataset.iloc[:, 1:18]
null = pd.DataFrame(x.isnull().sum().sort_values(ascending=False)[:25])
print(null)
x= x.apply(lambda x:x.fillna(x.mean()),axis=0)
# x["MINIMUM_PAYMENTS"].fillna(x["MINIMUM_PAYMENTS"].mean(), inplace=True)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=300, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

k = 3
km = KMeans(n_clusters=k)
y = kmeans.predict(x)
score = metrics.silhouette_score(x, y)
print(score)
