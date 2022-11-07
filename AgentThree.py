from Graph import *
from BFS import *
from Prey import *
from Predator import *

class AgentThree:
    
    def __init__(self,n_nodes,G : nx.Graph,prey:Prey, predator:Predator):
        self.n_nodes=n_nodes

        ag_not_decided=True
        while ag_not_decided:
            self.position=random.randint(1, n_nodes)
            if self.position!=prey.position and self.position != predator.position:
                ag_not_decided=False

        self.G=G

    def simulate_step(self,prey : Prey,predator:Predator):
        #Agent is only aware of the predator's position. so we can only effectively use its value
        #Prey's position here is only used to check if the surveyed node is the prey's node or not

        d_predator=len(get_bfs_path(self.G, self.position, predator.position)[1])  #Distance from predator

        neighbor_list=list(self.G.neighbors(self.position))
        
        # print("Distance From Prey = ",d_prey)
        # print("Distance from Pred =",d_predator)
        # print("Current Position = ",self.position)
        # print("Neighbor List = ",neighbor_list)

        #initialize the probablities of all the nodes in the graph
        self.initialize_probabilities()

        while(True):
        #randomly survey a node
            if prey.position==self.position:
                print("Prey found")
            survey_list=list(range(1,51))
            survey_list.remove(self.position)
            survey_node=random.choice(survey_list)

            if survey_node==prey.position:
                self.G.nodes[survey_node]["P_now"]=1
                #set prob of all other nodes to 0

                for node in range(1,51):
                    if node!=survey_node:
                        self.G.nodes[node]["P_now"]=0
                
                set_next_prob_list=list(self.G.neighbors(survey_node))+survey_node

                for node in set_next_prob_list:
                    # if self.G.degree(node)==3:
                    set_next_prob_list_neightbor=list(self.G.neighbors(node))+node
                    for node_2 in set_next_prob_list_neightbor:
                        if self.G.degree(node_2)==3:
                            multiplier=1/4
                        else:
                            multiplier=1/3
                        P_next+=self.G.nodes[node_2]["P_now"]*multiplier
                    
                    self.G.nodes[node]["P_next"]=P_next
                
                
                    




        

    def initialize_probabilities(self):
        for node in range(self.n_nodes):
            self.G.nodes[node][prob_now]=1/49
    
    
