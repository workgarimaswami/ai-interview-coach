from sklearn.cluster import KMeans
import numpy as np

def cluster_weakness(scores):
    X = np.array(scores).reshape(-1, 1)
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    return kmeans.labels_.tolist()
