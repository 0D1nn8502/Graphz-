## Graph-based planning (self driving cars) : Rapidly expanding random trees ## 

from queue import Queue 

vs = [1,2,3,4,5]
edges = [(1,3),(1,5),(2,1),(3,2),(3,1),(4,3),(5,4)] 

class graph: 
    
    ## Decide in what form edges and their connections will be given ## 
    def __init__(self,edges,connections):
        return 0 
    
  

def adj_list (vertices, edges): 
    
    dictum = {x:[]for x in vertices} #Fancy# 
        
    for y in edges:
            src,dest = y 
            if dest != src:
                dictum[src].append(dest)   
         
    return dictum 


def adj_matrix (vertices, edges):
    
    num = len(vertices) 
    i = 0 
    mat = [[0 for i in range(num)] for i in range(num)] ## also fancy ## 
        
    for y in edges:
        ind1 = y[0] - 1 
        ind2 = y[1] - 1 
            
        mat[ind1][ind2] = 1 
            
    return mat 


## Given an adjacency list of undirected, unweighted graph and a source vertex, returns vertices to which a path exists and their distance from the source (which will happen to be the shortest in these kinds of graphs) ## 
def bfs_vertices(adj_list, source, distance_dict):  
         
    counter = source 
    visited = [False]*len(adj_list) 
    q = Queue() 
    
    q.put(counter) 
    visited.append(counter) 
     
    distance = 0 
    
    while not q.empty():  
        
        counter = q.get()
        distance += 1 
        
        for x in adj_list[counter]:
            
            if x not in visited: 
                
                visited.append(x) 
                q.put(x)  
                
                distance_dict[x] = distance   
                      
    
    return distance_dict 
    

def max_flow_min_cut(): 
    return 0 

adj = adj_list(vs,edges) 
print(adj) 

print(bfs_vertices(adj,5,{}))  