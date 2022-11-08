from Graph import *
from BFS import *
from Prey import *
from Predator import *

class AgentThree:
    
    def __init__(self,n_nodes,G : nx.Graph,prey:Prey, predator:Predator):
        self.n_nodes=n_nodes
        self.prey=prey
        self.predator=predator

        ag_not_decided=True
        while ag_not_decided:
            self.position=random.randint(1, n_nodes)
            if self.position!=prey.position and self.position != predator.position:
                ag_not_decided=False

        self.G=G
        self.p_now=[0]*n_nodes
        self.p_next=[0]*n_nodes
        # Initialize the probablities of all the nodes in the graph
        self.initialize_probabilities()
        self.p_now[self.position-1]=0
        # self.p_now[5]=1
        # print(*self.p_now)

    def simulate_step(self,survey_node,prey : Prey,predator:Predator):
        #Agent is only aware of the predator's position. so we can only effectively use its value
        #Prey's position here is only used to check if the surveyed node is the prey's node or not

        # d_predator=len(get_bfs_path(self.G, self.position, predator.position)[1])  #Distance from predator

        # neighbor_list=list(self.G.neighbors(self.position))
   
        # self.initialize_probabilities()
        
        # self.print_state()

        prey_found=False
        # while(not prey_found):
        #randomly survey a node
        # if prey.position==self.position:
        #     print("Prey found sim step 1")
        #     prey_found=True
        #     return
        
        
        # survey_node=5
        # Belief update based on surveyed node
        self.update_belief(survey_node, prey.position)
        # self.print_state()

        #Agent moves towards the highest prob_now node of prey with rules of agent One
        #call agent one now!
        m=max(self.p_now)
        max_prob_list=[node+1 for node in range(len(self.p_now)) if self.p_now[node]==m]
        target_node=random.choice(max_prob_list)

        path_to_target=get_bfs_path(self.G, self.position, target_node)[1]

        self.position=path_to_target[1]
        #Agent has now moved to the new position
        #Has agent reached the prey and won?
        # if self.position==prey.position:
        #     print("Prey found sim step 2")
        #     prey_found=True
        #     return
        #If not won, update belief system again
        self.update_belief(self.position, prey.position)
        # self.print_state()

        # #Now prey will move
        # prey.simulate_step()
    
    

    def update_belief(self,survey_node,prey_positon):
        
        if survey_node==prey_positon:
            self.p_now[survey_node-1]=1
            #set prob of all other nodes to 0

            for node in range(1,51):
                if node!=survey_node:
                    self.p_now[node-1]=0
            
            self.transition_update()
            self.p_now=self.p_next
            print("After locating prey transition updates P_now-> ",*self.p_now)
            print("After locating prey P_next-> ",*self.p_next)
        else:
            print("Survey node:",survey_node)
            p_new=[0]*50
            p_prey_not_in_survey_node=1-self.p_now[survey_node-1]
            # self.p_next[survey_node-1]=0

            for node in range(1,51):
                if node!=survey_node:
                    p_prey_in_current_node=self.p_now[node-1]
                    p_new[node-1]=p_prey_in_current_node/p_prey_not_in_survey_node
            
            #updating current belief system
            self.p_now=p_new
            # Survey is done. We have updated our beliefs based on current info. Now we 
            # estimate which could be the next best step to take. So that's why we need
            # transition probability update which will change the probability of each
            # node, to reflect, the probability of the prey being there in the next
            # step. Thus giving our agent an idea of moving to which direction next
            #Now updating next belief system
            self.transition_update()
            self.p_now=self.p_next
            #P_now contains existing prob system
            #P_next contains the belief system possible for next step
            # self.p_next=self.p_now

    def transition_update(self):
        for survey_node in range(1,self.n_nodes+1):
            set_next_prob_list=list(self.G.neighbors(survey_node))+[survey_node]

            for node in set_next_prob_list:
                set_next_prob_list_neighbor=list(self.G.neighbors(node))+[node]
                p_node_2=0
                for node_2 in set_next_prob_list_neighbor:
                    if self.G.degree(node_2)==3:
                        multiplier=4
                    else:
                        multiplier=3
                    p_node_2+=self.p_now[node_2-1]/multiplier
                
                self.p_next[node-1]=p_node_2

    def initialize_probabilities(self):
        for node in range(self.n_nodes):
            self.p_now[node]=1/49

    def print_state(self):
        print("\nCurrent State ->")
        print("Prey Position : ",self.prey.position)
        print("Agent Position : ",self.position)
        d_prey=len(get_bfs_path(self.G, self.position, self.prey.position)[1])  #Distance from prey
        print("Distance to Prey : ",d_prey)
        print("Sum of P_now : ",sum(self.p_now))
        print()
        print("P_now -> ",*self.p_now)
        print()
        print("Sum of P_next : ",sum(self.p_next))
        print()
        print("P_next -> ",self.p_next)
        print("\n")
    
        
    
if __name__=="__main__":
    n_nodes=50
    G=Graph(n_nodes).G
    prey=Prey(n_nodes,G)
    # prey.position=6
    predator=Predator(n_nodes, G)
    agent_three=AgentThree(n_nodes, G, prey, predator)
    # agent_three.simulate_step(prey, predator)
    for i in range(0,100):
    # while(True):
        if agent_three.position==prey.position:
            print("Prey found main")
            break
        survey_list=list(range(1,51))
        survey_list.remove(agent_three.position)
        survey_node=random.choice(survey_list)
        
        agent_three.simulate_step(prey, predator)
        agent_three.print_state()

    # agent_three.print_state()
    # for i in range(0,10):
    #     agent_three.transition_update()
    #     agent_three.print_state()

    




# def transition_update(self,survey_node):
#         set_next_prob_list=list(self.G.neighbors(survey_node))+[survey_node]

#         for node in set_next_prob_list:
#             # if self.G.degree(node)==3:
#             set_next_prob_list_neighbor=list(self.G.neighbors(node))+[node]
#             p_node_2=0
#             for node_2 in set_next_prob_list_neighbor:
#                 if self.G.degree(node_2)==3:
#                     multiplier=1/4
#                 else:
#                     multiplier=1/3
#                 # P_next_calc+=self.G.nodes[node_2]["P_now"]*multiplier
#                 p_node_2+=self.p_now[node_2-1]*multiplier
            
#             # self.G.nodes[node]["P_next"]=P_next
#             # self.p_next[node-1]=p_node_2
#             self.p_now[node-1]=p_node_2