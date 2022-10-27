class Graph:
    def __init__(self,n_nodes,node_list):
        self.n_nodes=n_nodes
        self.node_list=node_list
    
    def add_edges(self,n_beg,n_end):
        #undirected graph so adding in both adjancency lists
        self.node_list[n_beg].add(n_end)
        self.node_list[n_end].add(n_beg)
    
    def print_list(self):
        for _ in self.node_list:
            print(_,", ",self.node_list[_])
    
g = Graph(5,{1,2,3})
g.add_edges(1,2)
g.add_edges(1,3)
g.print_list()
