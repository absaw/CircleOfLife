from Graph import *
from BFS import *
import random

class Prey:
    
    def __init__(self,n_nodes,G : nx.Graph):
        self.n_nodes=n_nodes
        self.curr_pos=random.randint(0,n_nodes-1)
        self.G=G
    
    def simulate_step(self):
        neighbor_list=list(self.G.neighbors(self.curr_pos))
        degree=self.G.degree(self.curr_pos)
        next_pos=random.choice(neighbor_list+[self.curr_pos])
        self.curr_pos=next_pos
        return next_pos

class Predator:

    def __init__(self,n_nodes,G:nx.Graph):
        self.n_nodes=n_nodes
        self.curr_pos=random.randint(0,n_nodes-1)
        self.G=G
    
    def simulate_step(self,agent_pos):

        neighbor_list=list(self.G.neighbors(self.curr_pos))
        degree=self.G.degree(self.curr_pos)
        shortest_path_list=[]
        shortest_path_len_list=[]
        for neighbor in neighbor_list:
            bfs_result=get_bfs_path(G, neighbor, agent_pos)
            if bfs_result[0]:
                shortest_path_list.append(bfs_result[1])
                shortest_path_len_list.append(len(bfs_result[1]))
            else:
                continue
        
        min_path_len=min(shortest_path_len_list)
        min_path_list=[node for node in shortest_path_list if len(node)==min_path_len]
        shortest_path=random.choice(min_path_list)
        next_pos=shortest_path[0]#neighbor with the shortest path length
        self.curr_pos=next_pos
        return next_pos


            



