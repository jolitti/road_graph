# Closeness centrality calculator
# by Marco

import networkx as nx

def calculate_feature(graph:nx.Graph) -> list[float]:
    size = graph.number_of_nodes()
    centralities = nx.closeness_centrality(graph)
    return [sum(v for k,v in centralities.items())/size]
