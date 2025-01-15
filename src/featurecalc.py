# FEATURE CALCULATORS DEFINITIONS
from feature_calculators.template_named import calculate_feature as template_feature
#from feature_calculators.closeness import calculate_feature as closeness_centrality
#from feature_calculators.betweenness import calculate_feature as betweenness_centrality
from feature_calculators.builtin import calculate_feature as builtins

calculators = [ template_feature, builtins]

# ---------------------------------------------

from sys import argv
import networkx as nx

import os


# get current directory
current_path = os.path.dirname(os.path.abspath(__file__))

# prints parent directory
parent = os.path.dirname(current_path)

# Access to the 'data' directory to access the graph files
data_dir = os.path.join(os.path.abspath(os.path.join(current_path, parent)), 'data')

files = [f for f in os.listdir(data_dir) if os.path.isfile(os.path.join(data_dir, f)) and (f.endswith('.mtx') or f.endswith('.edges'))]

# Open the file to write the features
file_name = "graphs_features.txt"
txt_file = open(os.path.join(data_dir, file_name),"a")


for file in files:
    print("Working in file ", file)
    G = nx.read_adjlist(os.path.join(data_dir, file), comments='%',nodetype=int)

    features = []
    for c in calculators:
        features += c(G)

    txt_file.write("Features for file " + file + '\n')
    for name,value in features:
        print(name,value)
        txt_file.write(name + " " + str(value) + '\n')
    
    txt_file.write('\n')

txt_file.close()