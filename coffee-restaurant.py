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

# def find_shortest_path(graph, startLabel, endLabel):
#     res = ""
#     prev = math.inf
#     for key in graph.keys():
#         if graph[key]["label"] == startLabel:
#             BFS(graph, key)
#             for k in graph.keys():
#                 if graph[k]["label"] == endLabel and graph[k]["d"] < prev:
#                     prev = graph[k]["d"]
#                     res = f'length of path is: {graph[k]["d"]}, start point is: {key}-{startLabel}, end point is: {k}-{endLabel}'
#     return res

def find_shortest_path(graph, startLabel, endLabel):
    endPointer = len(graph)
    startPointer = len(graph)+1

    graph[endPointer] = {
        "adj": [],
        "label": endLabel
    }
    graph[startPointer] = {
    "adj": [],
    "label": startLabel
    }

    for key in graph.keys():
        if graph[key]["label"] == startLabel:
            graph[startPointer]["adj"].append(key)
        if graph[key]["label"] == endLabel:
            graph[key]["adj"].append(endPointer)
    
    BFS(graph, startPointer)

    end = graph[endPointer]['p']
    length = graph[endPointer]['d']-2

    prev = end
    begin = ""

    while graph[prev]['p'] !=None:
        prev = graph[prev]['p']
        if graph[prev]['p']!=None:
            begin = prev
        
    
    print(f'shortest path from {startLabel} to {endLabel}\nstarts at {begin} and ends at {end}\npath length is:{length}')


num_of_vertices = 8

graph = {i:{"adj":[]} for i in range(num_of_vertices)}

# adding labels
graph[0]["label"] = "restaurant"
graph[5]["label"] = "restaurant"

graph[1]["label"] = "other"
graph[4]["label"] = "other"
graph[6]["label"] = "other"

graph[2]["label"] = "coffee"
graph[3]["label"] = "coffee"
graph[7]["label"] = "coffee"

# adding neighbours
graph[1]["adj"].append(0)
graph[2]["adj"].append(1)
graph[3]["adj"].append(2)
graph[3]["adj"].append(4)
graph[4]["adj"].append(5)
graph[6]["adj"].append(5)
graph[7]["adj"].append(5)
graph[7]["adj"].append(6)

#print(find_shortest_path(graph, "coffee", "restaurant"))
find_shortest_path(graph, "coffee", "restaurant")