from Graph import *
from BFS import *
import random

class Prey:
    
    def __init__(self,n_nodes,G : nx.Graph):
        self.n_nodes=n_nodes
        self.position=random.randint(0,n_nodes-1)
        self.G=G
    
    def simulate_step(self):
        neighbor_list=list(self.G.neighbors(self.position))
        degree=self.G.degree(self.position)
        next_pos=random.choice(neighbor_list+[self.position])
        self.position=next_pos
        return next_pos
            




