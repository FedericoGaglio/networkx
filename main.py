import networkx as nx
from networkx.algorithms.shortest_paths.greedy import greedy_path



#g = nx.Graph()

#g.add_edge('A','B')
#g.add_edge('A','C')
#g.add_edge('A','H')
#g.add_edge('A','Z')
#g.add_edge('D','B')
#g.add_edge('E','B')
#g.add_edge('C','F')
#g.add_edge('C','G')





#a = nx.bfs_edges(g,source='A')


#print(it)
#for i in a:
 #   print(i[1])



romania_neighbours = dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142))


romania_plot_positions = dict(
    Arad=(92, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))



g = nx.Graph()

node_labels = {}
for city, _ in romania_plot_positions.items():
    g.add_node(city, position=romania_plot_positions[city])
    node_labels[city]=city


for city, neighborhood in romania_neighbours.items():
    for neighbour, distance in neighborhood.items():
        g.add_edge(city, neighbour, weight=distance)



def dist(a, b):
    (x1, y1) = g.nodes[a]['position']
    (x2, y2) = g.nodes[b]['position']
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


it = greedy_path(g, 'Arad', 'Bucharest', heuristic=dist)

print(it)







