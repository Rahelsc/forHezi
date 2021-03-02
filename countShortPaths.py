import math

# code complexity: |V|
def BFS_init(graph,vertex,queue):
    for key in graph.keys():
        graph[key]['d']=0 if key==vertex else math.inf
        graph[key]['p']=None
        graph[key]['counter'] = 1 if key==vertex else 0
    queue.append(vertex)

# code complexity: |E|+|V|
def BFS(graph,vertex):
    queue=[]
    BFS_init(graph,vertex,queue)
    while len(queue)>0:
        curr=queue.pop(0)
        for adj in graph[curr]['adj']:
            if graph[adj]['d']==math.inf:
                queue.append(adj)
                graph[adj]['d']=graph[curr]['d']+1
                graph[adj]['p']=curr
            if graph[adj]['d'] == graph[curr]['d']+1:
                graph[adj]['counter']+=graph[curr]['counter'] # adding the previous path count to the current path count so that paths with only one access will be added and counted as well


## ------------------------
def print_BFS_res(graph):
    for key in graph.keys():
        path=[]
        curr=key

        while curr!=None:
            prev=graph[curr]['p']
            if prev!=None:
                path.insert(0, (prev,curr) )
            curr=prev

        print(f"dist to {key}: {graph[key]['d']}, path: {path}, num of short paths: {graph[key]['counter']}")



num_of_vertices=6

adjacency_list={i:{'adj':[]} for i in range(num_of_vertices)}


print(adjacency_list) # --> {0: {'adj': []}, 1: {'adj': []}, 2: {'adj': []}, 3: {'adj': []}, 4: {'adj': []}, 5: {'adj': []}}

adjacency_list[0]['adj'].append(1)

adjacency_list[1]['adj'].append(5)

adjacency_list[2]['adj'].append(0)
adjacency_list[2]['adj'].append(3)

adjacency_list[3]['adj'].append(1)
adjacency_list[3]['adj'].append(4)


print(adjacency_list) #--> {0: {'adj': [1]}, 1: {'adj': [5]}, 2: {'adj': [0, 3]}, 3: {'adj': [1, 4]}, 4: {'adj': []}, 5: {'adj': []}}

BFS(adjacency_list,2)
print(adjacency_list) #--> {0: {'adj': [1], 'd': 1, 'p': 2}, 1: {'adj': [5], 'd': 2, 'p': 0}, 2: {'adj': [0, 3], 'd': 0, 'p': None}, 3: {'adj': [1, 4], 'd': 1, 'p': 2}, 4: {'adj': [], 'd': 2, 'p': 3}, 5: {'adj': [], 'd': 3, 'p': 1}}


print_BFS_res(adjacency_list)
"""
dist to 0: 1, path: [(2, 0)]
dist to 1: 2, path: [(2, 0), (0, 1)]
dist to 2: 0, path: []
dist to 3: 1, path: [(2, 3)]
dist to 4: 2, path: [(2, 3), (3, 4)]
dist to 5: 3, path: [(2, 0), (0, 1), (1, 5)]
"""