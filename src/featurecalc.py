# This file will calculate each desired feature for each graph in the dataset and save it
# in a file to avoid repeated computations

# FEATURE CALCULATORS DEFINITIONS
# example of feature calculator import
from feature_calculators.template import calculate_feature as template_feature
# import additional calculators below

calculators = [ template_feature, ] # add as we write

# ---------------------------------------------

from sys import argv
import networkx as nx

# read network file
assert len(argv)>=2
G = nx.read_adjlist(argv[1])
features = []
for c in calculators:
    features += c(G)

for f in features:
    print(f)
