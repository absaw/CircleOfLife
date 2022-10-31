from GraphNetworkX import *

def get_bfs_path(G:nx.Graph,start,end):
    visited_set=set([start])
    
    fringe_q=deque([[start]])
    path_found=False

    if start==end:
        print("Goal reached")

    while fringe_q:
        path = fringe_q.popleft()
        
        curr_node=path[-1]
        
        if curr_node not in visited_set:
            neighbor_list=G.neighbors(curr_node)

            for neighbor in neighbor_list:
                updated_path=list(path)
                updated_path.append(neighbor)
                fringe_q.append(updated_path)

                if neighbor == end:
                    print("Shortest path=",*updated_path)
                    path_found=True
                    break
            visited_set.append(curr_node)

    if path_found==False:
        print("Path not found")
    

# G=generate_graph(10)

G=nx.graph()
G.add_edge()

get_bfs_path(G,)
        
