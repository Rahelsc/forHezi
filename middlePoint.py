import math

# code complexity: |V|
def BFS_init(graph,vertex,queue):
    for key in graph.keys():
        graph[key]['d']=0 if key==vertex else math.inf
        graph[key]['p']=None
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

graph = {i:{"adj":[]} for i in range(5)}

graph[1]["adj"].append(3)
graph[1]["adj"].append(0)

graph[3]["adj"].append(2)
graph[2]["adj"].append(0)
graph[2]["adj"].append(4)
graph[0]["adj"].append(4)

def middle(graph, start, middle, end):
    BFS(graph, start)
    midlength = graph[middle]['d']
    BFS(graph, middle)
    full_length = midlength+graph[end]['d']
    return full_length

print(middle(graph, 1, 2, 4))
