#NEW CODE FOR FEATURECALC.PY (using igraph instead of networkx)
'''

# This file will calculate each desired feature for each graph in the dataset and save it
# in a file to avoid repeated computations

# by Marco

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

import igraph as ig
from igraph import GraphBase

# read network file
assert len(argv)>=2
#G = nx.read_adjlist(argv[1], comments='#',nodetype=int)
G = GraphBase.Read_Ncol(f=argv[1], directed=False)  #WATCH OUT THE COMMENTS ON THE FILES! (Unfortunately, Read_Ncol doesn't have a parameter for the comments as nx.read_adjlist has...)
features = []
for c in calculators:
    features += c(G)

for f in features:
    print(f)
    
'''
