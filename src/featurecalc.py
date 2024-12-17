# FEATURE CALCULATORS DEFINITIONS
# example of feature calculator import
from feature_calculators.template import calculate_feature as template_feature
# import additional calculators below
from feature_calculators.closeness import calculate_feature as closeness_centrality
from feature_calculators.betweenness import calculate_feature as betweenness_centrality

calculators = [ template_feature, closeness_centrality, betweenness_centrality] # add as we write

# ---------------------------------------------

from sys import argv
import networkx as nx


# read network file
assert len(argv)>=2
G = nx.read_adjlist(argv[1], comments='%',nodetype=int)

# Check if the graph is connected
if(nx.is_connected(G)):
    print("The graph is connected")
else:
    print("NO!! The graph is NOT connected!!!!!")


features = []
for c in calculators:
    features += c(G)

for f in features:
    print(f)