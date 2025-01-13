from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sys import argv
import numpy as np

FEATURE_NAMES = [
        "density",
        "assortativity",
        "avg_clustering"
    ]

def lines_to_stats(lines) -> dict:
    title = lines[0]
    body = lines[1:]
    ans = {}
    ans["name"] = title.removeprefix("Features for ")
    ans["features"] = {}
    for line in body:
        feature_name,feature_value = line.split()
        ans["features"][feature_name] = float(feature_value)
    return ans

with open(argv[1]) as file:
    data = file.readlines()
data = [d.strip() for d in data]
data.append("")
d = []
chunk = []
for line in data:
    if line == "":
        d.append(chunk)
        chunk = []
        continue
    chunk.append(line)
data = d

def kmeans_with_clusters(samples,point_names,cluster_number) -> tuple[list,float]:
    """
    compute kmeans with the given samples and number of clusters
    return detected clusters as list of sets and silhouette score
    """
    kmeans = KMeans(n_clusters=cluster_number,n_init="auto")
    y = kmeans.fit_predict(samples)
    numbers = max(y)+1
    sets = []
    for i in range(numbers):
        newset = set()
        for index,value in enumerate(y):
            if value == i:
                newset.add(point_names[index])
        sets.append(newset)
    return sets,silhouette_score(samples,y)


data = [lines_to_stats(d) for d in data]
X = np.array([[d["features"][f] for f in FEATURE_NAMES] for d in data])
names = [d["name"] for d in data]

for i in range(2,10):
    _,silhouette = kmeans_with_clusters(X,names,i)
    print(f"{silhouette:.2f}")

for k in [2,5,6]:
    sets,_ = kmeans_with_clusters(X,names,k)
    for s in sets:
        print(s)
    print("---")
