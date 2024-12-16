# Betweenness centrality calculator
# by Eddie

#import networkx as nx
import math
import random

import igraph as ig
import time        #to measure the time to compute features

def calculate_feature(graph:ig.Graph) -> list[float]:
    start = time.time()
    vertex_betweenness = graph.betweenness()
    end = time.time()
    print(vertex_betweenness)
    print("------------------------------------------------")
    print(end - start, "seconds")
    return []



#NEW CODE FOR FEATURECALC.PY
'''

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
