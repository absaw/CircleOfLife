from Graph import *
from BFS import *
from Prey import *
from Predator import *
from AgentOne import *
import copy
from CallableAgentOneFunction import *
class AgentFive:
    
    def __init__(self,n_nodes,G : nx.Graph,prey:Prey, predator:Predator):
        self.n_nodes=n_nodes
        self.G=G
        self.prey=prey
        self.predator=predator
        ag_not_decided=True
        while ag_not_decided:
            self.position=random.randint(1, n_nodes)
            if self.position!=prey.position and self.position != predator.position:
                ag_not_decided=False
        self.p_now=[0]*n_nodes
        self.p_next=[0]*n_nodes
        # Initialize the probablities of all the nodes in the graph
        self.initialize_probabilities()
        self.p_now[self.position-1]=0

    def simulate_step(self,survey_node,prey : Prey,predator:Predator):
        # Simulate step will perform following actions:-
        # 1. Update belief system for finding/not finding predator at current survey node
        # 2. Move agent to next highest prob value neighbor by rules of Agent 1
        # 3. Update belief system for finding/not finding predator at new position

        #Prey's position here is only used to check if the surveyed node is the predator's node or not
       
        # 1. Belief update based on surveyed node
        self.update_belief(survey_node, predator.position)
        G_copy=copy.deepcopy(self.G)
        
        m=max(self.p_now)
        max_prob_list=[node+1 for node in range(len(self.p_now)) if self.p_now[node]==m]
        predator_virtual_location=random.choice(max_prob_list)
        
        virtual_predator=Predator(self.n_nodes,self.G)
        virtual_predator.position=predator_virtual_location
        
        #2. Agent moves towards the highest prob_now node of predator with rules of agent One
        ag_one=AgentOne(self.n_nodes, self.G, self.prey, virtual_predator)
        ag_one.position=self.position
        ag_one.simulate_step(self.prey, virtual_predator)
        self.position=ag_one.position
        
        #Agent has now moved to the new position, according to agent 1's behaviour
        # 3. Update belief system again
        self.update_belief(self.position, predator.position)
    

    def update_belief(self,survey_node,predator_position):
        # Update belief changes the probability of the nodes based on the belief system 
        # 1. If predator was found at survey node--set P_now(survey_node)=1
        # 2. If predator was not found at survey node--set P_now(survey_node)=0, for each X out of nodes, P(X)=P(predator in the node X)*P(predator not in survey node|predator in the node X)/P(predator not in survey node)
        
        if survey_node==predator_position:
            #1. Prey found scenario
            self.p_now[survey_node-1]=1
            #set prob of all other nodes to 0
            for node in range(1,51):
                if node!=survey_node:
                    self.p_now[node-1]=0
            
        else:
            #2. Prey not found scenario
            p_new=[0]*50
            p_predator_not_in_survey_node=1-self.p_now[survey_node-1]
            for node in range(1,51):
                if node!=survey_node:
                    p_predator_in_current_node=self.p_now[node-1]
                    p_new[node-1]=p_predator_in_current_node/p_predator_not_in_survey_node
            
            self.p_now=p_new.copy()

    #simplified transition update
    def transition_update(self):
        # Example Graph
        # A --- B
        # |  /  |
        # C --- D
        #   \ /
        #    E
        # 
        # Suppose Update Node=C, Agent is at E
        for update_node in range(1,self.n_nodes+1): # C
            neighbors_of_update_node=list(self.G.neighbors(update_node)) # [A,B,D,E]

            p_update_node=0

            for neighbor_of_update_node in neighbors_of_update_node:# neighbor_of_update_node=A,B,D,E
                degree_of_neighbor_of_update_node=self.G.degree(neighbor_of_update_node)
                p_update_node+=(0.4)*self.p_now[neighbor_of_update_node-1]/degree_of_neighbor_of_update_node
                ### 0.4 component done###
                
                ### Beginning 0.6 component ###
                # N1 - neighbor of update node = Suppose B
                # N2 - neighbor of N1 = Neighbors of B = A,C,D
                # Shift to Perspective of neighbor - N1 = B

                # Calc. dist to agent for each neighbor of N1 = i.e. Neighbor of B

                neighbors_of_n1=list(self.G.neighbors(neighbor_of_update_node))
                distance_to_agent_list=[]
                for neighbor_of_n1 in neighbors_of_n1:
                    distance_to_agent=len(get_bfs_path(G, neighbor_of_n1, self.position)[1])
                    distance_to_agent_list.append(distance_to_agent)
                min_distance_to_agent=min(distance_to_agent_list)
                
                min_distance_neighbors=[]
                #now we generate min_distance_neighbors of B
                for neighbor_of_n1_index in range(len(neighbors_of_n1)):
                    if min_distance_to_agent==distance_to_agent_list[neighbor_of_n1_index]:
                        min_distance_neighbors.append(neighbors_of_n1[neighbor_of_n1_index])

                # Now we have the neighbors of N1 which are at the least from agent
                # Example Graph
                # A --- B
                # |  /  |
                # C --- D
                #   \ /
                #    E
                # To sum up the variable values at this point:---
                # Update_Node=C, Agent at E
                # When neighbor_of_update_node=B
                # Neighbors_of_n1=A,C,D
                # distance_to_agent_list=[2,1,1]
                # min_distance_to_agent=1
                # min_distance_neighbors=C,D
                # If the update node C is in the shortest path towards agent, it will be in the min_dist_neighbor list.
                # So we can consider that predator may enter C. Thought the chances will be equally divided among the min
                # dist neighbors. So we divide the chance by the no. of min distance neighbors
                #   p=p_of_neighbor_of_update_node/no. of shortest path neighbors
                if update_node in min_distance_neighbors:
                    p_update_node+=(0.6)*(self.p_now[neighbor_of_update_node-1]/len(min_distance_neighbors))
        
            self.p_next[update_node-1]=p_update_node

            #1st component done

    #Unused transition update--to complex
    def transition_update_old_unused(self):
        # This updates the prob of all nodes, for when the predator moves in the graph
        # distance_list=[0]*50
        # for node in range(1,self.n_nodes+1):
        #     distance_list[node-1]=get_bfs_path(G, node, self.position)
        
        for survey_node in range(1,self.n_nodes+1): # C
            set_next_prob_list=list(self.G.neighbors(survey_node)) # [A,B,D,E]

            p_node=0
            for node in set_next_prob_list:# node=A,B,D,E
                
                set_next_prob_list_neighbor=list(self.G.neighbors(node))#Neighbors of A = B,C
                node_2_neighbor_dist_to_agent=[]

                for node_2 in set_next_prob_list_neighbor:# node_2=B,C
                    # print(node_2)
                    if self.G.degree(node_2)==3:
                        multiplier=3
                    else:
                        multiplier=2
                    p_node+=(0.4)*(self.p_now[node_2-1]/multiplier)

                    node_2_neighbor_dist_to_agent.append(len(get_bfs_path(G,node_2, self.position)[1]))# Distances of B and C from Agent #Appending (node,distance to agent) tuple to list

                min_dist_to_agent=min(node_2_neighbor_dist_to_agent)

                #min_dist_to_agent = 2
                #set_next_prob_list_neighbor=[B,C]
                #node_2_neighbor_dist_to_agent=[2,1]
                #min_dist_list=[1]
                min_dist_list=[]
                for n_i in range(len(node_2_neighbor_dist_to_agent)):
                    if min_dist_to_agent==node_2_neighbor_dist_to_agent[n_i]:
                        min_dist_list.append(set_next_prob_list_neighbor[n_i])


                # min_dist_list=[set_next_prob_list_neighbor[node_index] for node_index in node_2_neighbor_dist_to_agent if node_2_neighbor_dist_to_agent[node_index]==min_dist_to_agent]

                if node in min_dist_list:
                    p_node+=(0.6)*(self.p_now[node-1]/len(min_dist_list))
                
            self.p_next[node-1]=p_node

    def initialize_probabilities(self):
        #Initialize all prob to 1/49
        for node in range(self.n_nodes):
            self.p_now[node]=1/49

    def print_state(self):
        #Print current values
        print("\nCurrent State ->")
        print("Agent Position : ",self.position)
        print("Neighbors : ",*list(self.G.neighbors(self.position)))
        print("Prey Position : ",self.prey.position)
        print("Neighbors : ",*list(self.G.neighbors(self.prey.position)))
        print("Predator Position : ",self.predator.position)
        print("Neighbors : ",*list(self.G.neighbors(self.predator.position)))
        d_prey=len(get_bfs_path(self.G, self.position, self.prey.position)[1])  #Distance from prey
        d_predator=len(get_bfs_path(self.G, self.position, self.predator.position)[1])  #Distance from predator
        print("Distance to Prey : ",d_prey)
        print("Distance to Predator : ",d_predator)
        print("Sum of P_now : ",sum(self.p_now))
        # print()
        # print("P_now -> ",*self.p_now)
        # print()
        print("Sum of P_next : ",sum(self.p_next))
        # print()
        # print("P_next -> ",self.p_next)
        # print("\n")

    def print_sum(self):
        print("Sum of P_now : ",sum(self.p_now))
        print("Sum of P_next : ",sum(self.p_next))


#Used for testing. Not part of the main flow. AgentFive simulator will call AgentFive
if __name__=="__main__":

    n_nodes=50
    G=Graph(n_nodes).G
    prey=Prey(n_nodes,G)
    # prey.position=6
    predator=Predator(n_nodes, G)
    agent_five=AgentFive(n_nodes, G, prey, predator)
    # survey_list=list(range(1,51))
    # survey_list.remove(agent_five.position)
    # survey_node=random.choice(survey_list)
    # print("Initial Condtion -> ")
    # agent_five.print_state()
    # agent_five.simulate_step(prey, predator)
    # for i in range(1,101):
    # # while(True):
    #     print("i = ",i)
    #     if agent_five.position==prey.position:
    #         print("Prey found main")
    #         break
        
    #     agent_five.simulate_step(survey_node,prey, predator)
    #     agent_five.print_state()
    #     m=max(agent_five.p_now)
    #     survey_list=[node+1 for node in range(len(agent_five.p_now)) if agent_five.p_now[node]==m]
    #     survey_node=random.choice(survey_list)


    # agent_five.print_state()
    # for i in range(0,10):
    #     agent_five.transition_update()
    #     agent_five.print_state()


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