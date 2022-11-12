#this file does the job of simulating the movement of agent prey and predator
#Variables needed
from Graph import *
from BFS import *
from Prey import *
from Predator import *
from AgentEight import *

def simulate_agent_eight():
    
    n_sim=30      # No. of simulations
    n_trials=100    # No. of Trials. Each trial has a random new graph. Final Metrics of one simulation will be calculated from these 100 trials
                    # We then average out the metrics, from the 30 simulations we have, to eventually get the final results.
    
    n_nodes=50
    win_list=[]
    lose_list=[]
    hang_list=[]
    step_list=[]
    for sim in range(1,n_sim+1):
        n_win=0     # When agent and prey are in same position, provided pred is not in that position
        n_lose=0    # When agent and predator are in same position
        n_hang=0    # When agent can't catch prey, even after walking a certain threshold distance
        hang_threshold=100
        max_steps=300
        n_steps=0

        for trial in range(1,n_trials+1):

            #generate graph
            GraphClass=Graph(n_nodes)
            G=GraphClass.G

            #spawn prey, predator and agent at random locations
            prey=Prey(n_nodes,G)
            predator=Predator(n_nodes, G)
            agent_eight=AgentEight(n_nodes, G, prey, predator)
            
            steps=0
            #Initial survey position is randomly selected
            # survey_list=list(range(1,51))
            # survey_list.remove(agent_eight.position)
            # survey_node=random.choice(survey_list)

            #We know the predator's position initially so we start by surveying that node
            survey_node=predator.position
            # The three players move in rounds, starting with the Agent, followed by the Prey, and then the Predator.
            while(steps<=max_steps):
                steps+=1
                # print("\n\nStep ->>>>> ",steps)
                # agent_eight.print_state()
                # ========= Terminal Condition Check  ========
                if agent_eight.position==predator.position:
                    n_lose+=1
                    break
                if agent_eight.position==prey.position:
                    n_win+=1
                    n_steps+=steps
                    break
                # Threshold condition
                if steps>=hang_threshold:
                    n_hang+=1
                    break

                # 1. Update Belief system of prey and predator based on surveyed node
                # Update belief system of pred only if not certain
                agent_eight.update_belief_predator(survey_node, predator.position)
                # Update belief system of prey only if not certain
                agent_eight.update_belief_prey(survey_node, prey.position)
                #========= Agent Eight Simulation  ========
                agent_eight.simulate_step(survey_node,prey,predator)
                # Now we have our agent's next position
                # ========= Terminal Condition Check  ========
                if agent_eight.position==predator.position:
                    n_lose+=1
                    break
                if agent_eight.position==prey.position:
                    n_win+=1
                    n_steps+=steps
                    break
                # New Info : Predator/Prey and is not in current agent's position. So update belief system
                agent_eight.update_belief_prey(agent_eight.position, prey.position)
                agent_eight.update_belief_predator(agent_eight.position, predator.position)

                # ======== Prey Simulation   =========
                prey.simulate_step()
                agent_eight.transition_update_prey()
                agent_eight.p_now_prey=agent_eight.p_next_prey.copy()

                #agent_eight.print_sum()

                #========= Terminal Condition Check  ========
                if agent_eight.position==prey.position:
                    n_win+=1
                    n_steps+=steps
                    break
                
                # ======== Predator Simulation   =========
                predator.simulate_step_distracted(agent_eight.position)
                # New Info : Predator has moved. So update apply transition probability update to each node in graph
                agent_eight.transition_update_predator()
                agent_eight.p_now_predator=agent_eight.p_next_predator.copy()
                #agent_eight.print_sum()

                # ========= Terminal Condition Check  ========
                if agent_eight.position==predator.position:
                    n_lose+=1
                    break
                if agent_eight.position==prey.position:
                    n_win+=1
                    n_steps+=steps
                    break
                    
                is_pred_certain=False
                for p_now_index in range(len(agent_eight.p_now_predator)):
                    if agent_eight.p_now_predator[p_now_index] == 1:
                        is_pred_certain=True
                        # survey_node=p_now_index+1
                if is_pred_certain:
                    # Now we calculate max survey node based on prey's probability
                    m=max(agent_eight.p_now_prey) #finding value with highest prob
                    survey_list=[node+1 for node in range(len(agent_eight.p_now_prey)) if agent_eight.p_now_prey[node]==m] # List of nodes with highest prob value
                    survey_node=random.choice(survey_list) #Selecting a random element from highest prob value list
                if not is_pred_certain:

                    m=max(agent_eight.p_now_predator) #finding value with highest prob
                    max_prob_list=[node+1 for node in range(len(agent_eight.p_now_predator)) if agent_eight.p_now_predator[node]==m] # List of nodes with highest prob value
                    
                    #Choosing node with max prob and min distance from agent's position
                    distance_from_agent_list=[]
                    for max_prob_node in max_prob_list:
                        distance_from_agent_list.append(len(get_bfs_path(G, max_prob_node, agent_eight.position)[1]))
                    min_distance=min(distance_from_agent_list)
                    min_distance_list=[]
                    for max_prob_node_index in range(len(max_prob_list)):
                        if min_distance==distance_from_agent_list[max_prob_node_index]:
                            min_distance_list.append(max_prob_list[max_prob_node_index])
                
                    survey_node=random.choice(min_distance_list)
                # survey_node=random.choice(survey_list) #Selecting a random element from highest prob value list

        win_list.append(n_win)
        lose_list.append(n_lose)
        hang_list.append(n_hang)
        step_list.append(n_steps/n_win)
        # print("Sim - ",sim)
        # print("Wins = ",n_win)

    print("Win List : ",*win_list)
    print("Lose List : ",*lose_list)
    print("Hang List : ",*hang_list)
    print("Step List : ",*step_list)
    print("Average wins : ",(sum(win_list)/len(win_list)))
    print("Average losses : ",(sum(lose_list)/len(lose_list)))
    print("Average hangs : ",(sum(hang_list)/len(hang_list)))
    print("Average steps : ",(sum(step_list)/len(step_list)))
    print("Hang Threshold : ",hang_threshold)

# simulate_agent_eight()


                            
                




                





                








