from Graph import *
from BFS import *
from Prey import *
from Predator import *


def agent_one_simulate_step(G:nx.Graph,agent_position,prey_positon,predator_position):
    
    d_prey=len(get_bfs_path(G, agent_position, prey_positon)[1])     #Distance from prey
    d_predator=len(get_bfs_path(G, agent_position, predator_position)[1])  #Distance from predator
    # print("Distance to prey -> ",d_prey)
    # print("Distance to pred -> ",d_predator)
    neighbor_list=list(G.neighbors(agent_position))
    
    # print("Distance From Prey = ",d_prey)
    # print("Distance from Pred =",d_predator)
    # print("Current Position = ",agent_position)
    # print("Neighbor List = ",neighbor_list)

    cost_matrix={}
    for neighbor in neighbor_list:
        c_prey=len(get_bfs_path(G, neighbor, prey_positon)[1])
        c_predator=len(get_bfs_path(G, neighbor, predator_position)[1])
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
                            next_position=agent_position
                        else:
                            next_position=random.choice(l6)
                            #print(l6)

                    else:
                        next_position=random.choice(l5)
                        #print(l5)


                else:
                    next_position=random.choice(l4)
                    #print(l4)

            else:
                next_position=random.choice(l3)
                #print(l3)

        else:
            next_position=random.choice(l2)
            #print(l2)

    else:
        next_position=random.choice(l1)
        #print(l1)

    return next_position

if __name__=="__main__":
    n_nodes=50
    
    # print("Prey at -> ",prey.position)
    # print("Predator at -> ",predator.position)
    n_win=0
    n_sim=30
    n_hang=0

    win_list=[]
    lose_list=[]
    hang_list=[]
    while(n_sim>0):
        n_sim-=1
        n_win=0
        n_hang=0
        n_lose=0
        
        for sims in range(0,100):
            # print(i)
            G=Graph(n_nodes).G
            prey=Prey(n_nodes,G)
            predator=Predator(n_nodes, G)
            ag_not_decided=True
            while ag_not_decided:
                agent_position=random.randint(1, n_nodes)
                if agent_position!=prey.position and agent_position != predator.position:
                    ag_not_decided=False

            for steps in range(200):
                if agent_position==prey.position:
                    # print("Win")
                    n_win+=1
                    break
                elif agent_position==predator.position:
                    # print("lose")
                    n_lose+=1
                    break
                if steps>=100:
                    n_hang+=1
                    break
                agent_position=agent_one_simulate_step(G, agent_position, prey.position, predator.position)
                # print("Agent Position -> ",agent_position)
                prey.simulate_step()
                if agent_position==prey.position:
                    # print("Win")
                    n_win+=1
                    break
                elif agent_position==predator.position:
                    # print("lose")
                    n_lose+=1
                    break
                predator.simulate_step(agent_position)
                if agent_position==prey.position:
                    # print("Win")
                    n_win+=1
                    break
                elif agent_position==predator.position:
                    # print("lose")
                    n_lose+=1
                    break
        win_list.append(n_win)
        lose_list.append(n_lose)
        hang_list.append(n_hang)
    
    print("Win List : ",*win_list)
    print("Average = ",sum(win_list)/30)
    print("Lose List : ",*lose_list)
    print("Average = ",sum(lose_list)/30)
    print("Hang List : ",*hang_list)
    print("Average = ",sum(hang_list)/30)