#this file does the job of simulating the movement of agent prey and predator
#Variables needed
from Graph import *
from BFS import *
from PreySimulation import *

def agent_one():
    
    n_sim=30        # No. of simulations
    n_trials=100    # No. of Trials. Each trial has a random new graph. Final Metrics of one simulation will be calculated from these 100 trials
                    # We then average out the metrics, from the 30 simulations we have, to eventually get the final results.
    
    n_nodes=10
    for sim in range(1,n_sim+1):

        for trial in range(1,n_trials+1):

            #generate graph
            G=generate_graph(n_nodes)

            #spawn prey, predator and agent at random locations

            prey=Prey(n_nodes,G)
            predator=Predator(n_nodes, G)

            agent_pos=random.randint(1, n_nodes)






