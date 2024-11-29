# This script will import a graph from a file and print out some useful stats for it

# by Marco


from sys import argv,getsizeof
import networkx as nx

# read network file
assert len(argv)>=2, "Must specify a file containing a graph"
G = nx.read_adjlist(argv[1],nodetype=int)
graphsize = sum(getsizeof(v) for v in G.nodes) + sum(getsizeof(e) for e in G.edges)
graphsize = graphsize // (1024*1024)
print(f"Graph occupies {graphsize} MBs in memory")
