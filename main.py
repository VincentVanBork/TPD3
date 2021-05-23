from typing import Dict, List, Literal, Tuple

from matplotlib import pyplot as plt
from graph import ActivityNode
import string
from collections import defaultdict
import networkx as nx


graph_pro = nx.DiGraph()

activities = list(string.ascii_uppercase)[:10]
print(activities)
time_costs = [
    1,
    3,
    4,
    7,
    2,
    5,
    2,
    1,
    3,
    1
]
predecessors = [
    [''],
    ['A'],
    ['A'],
    ['B'],
    ['D'],
    ['C'],
    ['C'],
    ['C'],
    ['F', 'G', 'H'],
    ['E', 'I'],
]
nodes = []
edges = []
for activity, activity_time, required_before in zip(
        activities, time_costs, predecessors):
    nodes.append(ActivityNode(
        name=activity,
        time=activity_time,
        required=required_before))
    for req in required_before:
        edges.append((req, activity, activity_time))

graph: Dict[str, List[str]] = defaultdict()
G = nx.DiGraph()

for node in nodes:
    print(node)
    graph[node.name] = node.required



G.add_nodes_from(activities)
print(graph)

# G.add_edges_from(edges)
# G.add_edge("A", "B", weight=1)
G.add_weighted_edges_from(edges)
print(G.graph)
nx.draw(G, with_labels=True, )
plt.show()
