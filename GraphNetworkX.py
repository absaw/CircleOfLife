from math import degrees
from turtle import pos
import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque

def generate_graph(n_nodes):
    # n_nodes=50
    
    G=nx.Graph()
    
    #add nodes to the graph

    for node in range(0,n_nodes):
        G.add_node(node)
    
    node_list=list(G.nodes())
    # print("Node list : ",node_list)
    #adding initial edges

    for node in range(0,n_nodes):
        if node==n_nodes-1:
            G.add_edge(n_nodes-1,0)
        else:
            G.add_edge(node,node+1)
    # print("Initial No. of edges = ",G.number_of_edges())

    #adding edges randomly till degree is less than 3
    addEdge=True
    k=0
    while len(node_list)>0:
        # print(len(node_list))
        # if len(node_list)<=5:
            # print("here")
            # visualize_graph(G)
        # k+=1
    # for node_beg in range(0,n_nodes):
        # node_beg=random.randint(0,n_nodes)
        node_beg=random.choice(node_list)
        
        possible_node_list=list(range(node_beg-5,node_beg-1))+list(range(node_beg+2,node_beg+6))
        
        if G.degree(node_beg)<3:
            possible_node_list_copy=possible_node_list.copy()
            for node in possible_node_list:
                if G.degree(node%n_nodes)>=3:
                    possible_node_list_copy.remove(node)
            if not possible_node_list_copy:
                node_list.remove(node_beg)
                continue
            possible_node_list=possible_node_list_copy

            #if list is empty
            
            # if 5<node_beg<n_nodes-5:
            # endNodeNotFound=True
            # max_tries=10
            # while endNodeNotFound:
                # max_tries-=1
            node_end=random.choice(possible_node_list)%n_nodes
            # node_end=abs(random.randint(node_beg-5,node_beg+5))%50
            if G.degree(node_end)<3 and node_end!=node_beg:
                # endNodeNotFound=False
                G.add_edge(node_beg,node_end)
                node_list.remove(node_beg)
                node_list.remove(node_end)
            # elif G.degree(node_end)>=3:
            #     node_list.remove(node_end)
            # if max_tries==0:
            #     break
            
            # else:
        # if k==20:
            # break
        else:
            node_list.remove(node_beg)
        

    # print("No. of edges = ",G.number_of_edges())
    # for node in range(0,G.number_of_nodes()):
        # print("Node - ",node," Degree - ",G.degree(node),"- Neighbors - ",list(G.neighbors(node)))
        
    # visualize_graph(G)
    return G

def visualize_graph(G):
    plt.figure(figsize=(12,8))
    pos=nx.circular_layout(G)
    nx.draw_networkx(G,pos=pos,with_labels=True,edge_color="Green")
    # nx.draw_circular(G,with_labels=True)
    # nx.draw(G,with_labels=True)
    plt.show()

# def get_shortest_path():
# for i in range(0,100):
#     generate_graph(50)
# generate_graph(50)