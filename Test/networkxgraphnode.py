import networkx as nx
import matplotlib.pyplot as plt
G= nx.Graph()

G.add_node(1,prob=0.2)
G.add_node(2,prob=0)
G.nodes[1]["prob"]+=0.22
print(G.nodes.data())
print(G.nodes[1]["prob"])
print(G.nodes[2]["prob"])
nx.draw(G,with_labels=True)
plt.show()

