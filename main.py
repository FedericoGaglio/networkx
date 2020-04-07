import networkx as nx

g = nx.Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('D','B')
g.add_edge('E','B')
g.add_edge('C','F')
g.add_edge('C','G')

x = nx.bfs_edges(g,'A')

for i in x:
    print(i[1])

