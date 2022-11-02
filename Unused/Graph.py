import networkx as nx
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,n_nodes):
        self.n_nodes=n_nodes
        self.node_list=range(1,n_nodes+1)
        self.edge_list=[]
        self.node_properties={}
        for node in self.node_list:
            self.node_properties[node]={"neighbors":[],"probability":[]}
    
    def add_edges(self,n_beg,n_end):
        #undirected graph so adding in both adjancency lists
        self.node_properties[n_beg]["neighbors"].append(n_end)
        self.node_properties[n_end]["neighbors"].append(n_beg)
        self.edge_list.append((n_beg,n_end))
    
    def get_edge_list(self):
        return self.edge_list
    
    def print_adj_dict(self):
        for key in self.node_properties:
            print(key,", ",self.node_properties[key]["neighbors"])

    def get_node_degree(self,node):
        return self.node_properties[node]["neighbors"].count
    
    def visualize_graph(self):
        G = nx.Graph()
        G.add_edges_from(self.edge_list)
        nx.draw_networkx(G)
        plt.show()

    
class Node:
    def __init__(self,id,adjacent_node_list):
        self.id=id
        self.adjacent_node_list=adjacent_node_list


# g = Graph(3)
# g.add_edges(1,2)
# g.add_edges(1,3)
# g.print_adj_dict()
# g.visualize_graph()

def circle():

    n_nodes=10
    g = Graph(3)
    g.add_edges(1,2)
    g.add_edges(1,3)
    g.print_adj_dict()
    g.visualize_graph()
