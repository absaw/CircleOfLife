#this file does the job of simulating the movement of agent prey and predator
#Variables needed
from Graph import *
from BFS import *
from Prey import *
from Predator import *
from AgentTwo import *

def simulate_agent_two():
    
    n_sim=30      # No. of simulations
    n_trials=100    # No. of Trials. Each trial has a random new graph. Final Metrics of one simulation will be calculated from these 100 trials
                    # We then average out the metrics, from the 30 simulations we have, to eventually get the final results.
    
    n_nodes=50
    win_list=[]
    lose_list=[]
    hang_list=[]
    for sim in range(1,n_sim+1):
        n_win=0     # When agent and prey are in same position, provided pred is not in that position
        n_lose=0    # When agent and predator are in same position
        n_hang=0    # When agent can't catch prey, even after walking a certain threshold distance
        hang_threshold=200
        max_steps=300
        for trial in range(1,n_trials+1):

            #generate graph
            G=generate_graph(n_nodes)

            #spawn prey, predator and agent at random locations

            prey=Prey(n_nodes,G)
            predator=Predator(n_nodes, G)
            agent_two=AgentTwo(n_nodes, G, prey, predator)
            
            path=[]
            path.append(agent_two.position)
            steps=0
            
            # The three players move in rounds, starting with the Agent, followed by the Prey, and then the Predator.
            while(steps<=max_steps):
                steps+=1
                #========= Agent Two Simulation  ========
                agent_two.simulate_step(prey, predator)
                # Now we have our agent's next position

                #========= Terminal Condition Check  ========
                if agent_two.position==predator.position:
                    n_lose+=1
                    break
                if agent_two.position==prey.position:
                    n_win+=1
                    break
                # Threshold condition
                if steps>=hang_threshold:
                    n_hang+=1
                    break

                # ======== Prey Simulation   =========
                prey.simulate_step()

                #========= Terminal Condition Check  ========
                if agent_two.position==predator.position:
                    n_lose+=1
                    # print("Agent Dead")
                    break
                if agent_two.position==prey.position:
                    n_win+=1
                    # print("Goal Reached")
                    break
                # ======== Predator Simulation   =========
                predator.simulate_step(agent_two.position)

                #========= Terminal Condition Check  ========
                if agent_two.position==predator.position:
                    n_lose+=1
                    break
                if agent_two.position==prey.position:
                    n_win+=1
                    break

                # path.append(next_position)

        # print("Sim -> ", sim)
        # print("Alive ->",n_win)       
        # print("Dead ->",n_lose)       
        # print("Hang ->",n_hang)       
        # print()
        win_list.append(n_win)
        lose_list.append(n_lose)
        hang_list.append(n_hang)
    print("Win List : ",*win_list)
    print("Lose List : ",*lose_list)
    print("Hang List : ",*hang_list)
    print("Average wins : ",(sum(win_list)/len(win_list)))
    print("Average losses : ",(sum(lose_list)/len(lose_list)))
    print("Average hangs : ",(sum(hang_list)/len(hang_list)))
    print("Hang Threshold : ",hang_threshold)

simulate_agent_two()


                            
                




                





                









