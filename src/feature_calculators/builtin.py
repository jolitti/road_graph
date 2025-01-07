# This is a collection of features that are easily calculated
# via builtin functions of networkx

# By Marco

# Calculated features:
# - density
# - degree assortativity coefficient
# - average clustering

import networkx as nx

def calculate_feature(graph) -> list[tuple[str,float]]:
    ans = []
    ans.append(("density",nx.density(graph)))
    ans.append(("assortativity",nx.degree_assortativity_coefficient(graph)))
    ans.append(("avg_clustering",nx.average_clustering(graph)))
    return ans
