import networkx as nx
import matplotlib.pyplot as plt
import random
def graph():
    n_nodes=10
    
    G=nx.Graph()
    
    #add nodes to the graph

    for node in range(1,n_nodes+1):
        G.add_node(node)
    
    #adding initial edges

    for node in range(1,n_nodes+1):
        if node==n_nodes:
            G.add_edge(n_nodes,1)
        else:
            G.add_edge(node,node+1)

    #adding edges randomly till degree is less than 3
    addEdge=True
    while(addEdge):
        node_beg=random.randint(1,n_nodes)

        if G.degree(node_beg)<3:
            
            # if 5<node_beg<n_nodes-5:
            endNodeNotFound=True
            while endNodeNotFound:
                node_end=random.randint((node_beg-5)%50,(node_beg+5)%50)
                if G.degree(node_end)<3:
                    endNodeNotFound=False
            
            G.add_edge(node_beg,node_end)
            # else:
            

    nx.draw(G,with_labels=True)
    plt.show()
graph()