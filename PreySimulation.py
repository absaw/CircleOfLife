from GraphNetworkX import *
import random

class Prey:
    
    def __init__(self,n_nodes,G : nx.Graph):
        self.n_nodes=n_nodes
        self.curr_pos=random.randint(0,n_nodes-1)
        self.G=G

    # def get_curr_pos(self):
    #     return self.curr_pos
    
    def simulate_step(self):
        neighbor_list=list(self.G.neighbors(self.curr_pos))
        degree=self.G.degree(self.curr_pos)
        next_pos=random.choice(neighbor_list+[self.curr_pos])
        self.curr_pos=next_pos
        return next_pos
    

