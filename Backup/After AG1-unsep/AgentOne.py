#this file does the job of simulating the movement of agent prey and predator
#Variables needed
from Graph import *
from BFS import *
from Prey import *
from Predator import *

def agent_one():
    
    n_sim=50      # No. of simulations
    n_trials=100    # No. of Trials. Each trial has a random new graph. Final Metrics of one simulation will be calculated from these 100 trials
                    # We then average out the metrics, from the 30 simulations we have, to eventually get the final results.
    
    n_nodes=50
    win_list=[]
    lose_list=[]
    for sim in range(1,n_sim+1):
        n_win=0     # When agent and prey are in same position, provided pred is not in that position
        n_lose=0    # When agent and predator are in same position
        n_hang=0    # When agent can't catch prey, even after walking a certain threshold distance
        hang_threshold=100
        for trial in range(1,n_trials+1):

            #generate graph
            G=generate_graph(n_nodes)

            #spawn prey, predator and agent at random locations

            prey=Prey(n_nodes,G)
            predator=Predator(n_nodes, G)

            ag_not_decided=True
            while ag_not_decided:
                ag_position=random.randint(1, n_nodes)
                if ag_position!=prey.position and ag_position != predator.position:
                    ag_not_decided=False

            path=[]
            path.append(ag_position)
            steps=0
            # The three players move in rounds, starting with the Agent, followed by the Prey, and then the Predator.
            # for ag_position in path:
            while(steps<hang_threshold):
                
                # # Terminal Condition Check
                # if ag_position==predator.position:
                #     n_lose+=1
                #     # print("Agent Dead")
                #     break
                # if ag_position==prey.position:
                #     n_win+=1
                #     # print("Goal Reached")
                #     break
                # # Threshold condition
                # if len(path)>hang_threshold:
                #     n_hang+=1
                #     break
                    # print("Hanged")
                
                #Agent starts moving
                #Agent one simulation
                
                d_prey=len(get_bfs_path(G, ag_position, prey.position)[1])     #Distance from prey
                d_predator=len(get_bfs_path(G, ag_position, predator.position)[1])  #Distance from predator

                neighbor_list=list(G.neighbors(ag_position))
                
                # print("Distance From Prey = ",d_prey)
                # print("Distance from Pred =",d_predator)
                # print("Current Position = ",ag_position)
                # print("Neighbor List = ",neighbor_list)

                cost_matrix={}
                for neighbor in neighbor_list:
                    c_prey=len(get_bfs_path(G, neighbor, prey.position)[1])
                    c_predator=len(get_bfs_path(G, neighbor, predator.position)[1])
                    cost_matrix[neighbor]=[c_prey,c_predator]
                l1=[]
                for neighbor in neighbor_list:
                    if cost_matrix[neighbor][0]<d_prey and cost_matrix[neighbor][1]>d_predator:
                        l1.append(neighbor)
                
                if not l1:
                    
                    l2=[]
                    for neighbor in neighbor_list:
                        if cost_matrix[neighbor][0]<d_prey and cost_matrix[neighbor][1]==d_predator:
                            l2.append(neighbor)

                    if not l2:
                        l3=[]
                        for neighbor in neighbor_list:
                            if cost_matrix[neighbor][0]==d_prey and cost_matrix[neighbor][1]>d_predator:
                                l3.append(neighbor)
                        
                        if not l3:
                            l4=[]
                            for neighbor in neighbor_list:
                                if cost_matrix[neighbor][0]==d_prey and cost_matrix[neighbor][1]==d_predator:
                                    l4.append(neighbor)
                            
                            if not l4:
                                l5=[]
                                for neighbor in neighbor_list:
                                    if cost_matrix[neighbor][1]>d_predator:
                                        l5.append(neighbor)
                                
                                if not l5:
                                    l6=[]
                                    for neighbor in neighbor_list:
                                        if cost_matrix[neighbor][1]==d_predator:
                                            l6.append(neighbor)

                                    if not l6:
                                        #sit still and pray
                                        next_position=ag_position
                                    else:
                                        next_position=random.choice(l6)

                                else:
                                    next_position=random.choice(l5)

                            else:
                                next_position=random.choice(l4)

                        else:
                            next_position=random.choice(l3)

                    else:
                        next_position=random.choice(l2)

                else:
                    next_position=random.choice(l1)
                
                ag_position=next_position
                #now we have our agent's next position
                # Terminal Condition Check
                if ag_position==predator.position:
                    n_lose+=1
                    # print("Agent Dead")
                    break
                if ag_position==prey.position:
                    n_win+=1
                    # print("Goal Reached")
                    break
                # Threshold condition
                # if len(path)>hang_threshold:
                #     n_hang+=1
                #     break

                #we will now simulate prey
                # print("Next Position = ",next_position)
                prey.simulate_step()
                # Terminal Condition Check
                if ag_position==predator.position:
                    n_lose+=1
                    # print("Agent Dead")
                    break
                if ag_position==prey.position:
                    n_win+=1
                    # print("Goal Reached")
                    break
                #we will now simulate predator
                predator.simulate_step(next_position)

                # Terminal Condition Check
                if ag_position==predator.position:
                    n_lose+=1
                    # print("Agent Dead")
                    break
                if ag_position==prey.position:
                    n_win+=1
                    # print("Goal Reached")
                    break

                # path.append(next_position)

        # print("Sim -> ", sim)
        # print("Alive ->",n_win)       
        # print("Dead ->",n_lose)       
        # print("Hang ->",n_hang)       
        # print()
        win_list.append(n_win)
        lose_list.append(n_lose)
    print("Win List : ",*win_list)
    print("Lose List : ",*lose_list)
    print("Average wins : ",(sum(win_list)/len(win_list)))
    print("Average losses : ",(sum(lose_list)/len(lose_list)))

agent_one()
                            
                




                





                









