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


graph = {i:{"adj":[]} for i in range(9)}

graph[0]["label"] = "New pharm"
graph[1]["label"] = "Medical clinic"
graph[2]["label"] = "Rami-Levi"
graph[3]["label"] = "Super-pharm"
graph[4]["label"] = "Medical clinic"
graph[5]["label"] = "Super-pharm"
graph[6]["label"] = "Shufersal"
graph[7]["label"] = "Shufersal"
graph[8]["label"] = "Rami-Levi"

graph[1]["adj"].append(2)
graph[2]["adj"].append(3)
graph[6]["adj"].append(3)
graph[6]["adj"].append(8)
graph[4]["adj"].append(6)
graph[4]["adj"].append(0)
graph[5]["adj"].append(4)
graph[7]["adj"].append(5)

def find_shortest_path(graph, startpoint, *endpoints):
    endPointer = len(graph)
    startPointer = endPointer+1

    graph[endPointer] = {
        "adj":[],
        "label": "pharmacy"
    }

    graph[startPointer] = {
        "adj":[],
        "label": "clinic"
    }

    for key in graph.keys():
        if graph[key]["label"] == startpoint:
            graph[startPointer]["adj"].append(key)
        for point in endpoints:
            if graph[key]["label"] == point:
                graph[key]["adj"].append(endPointer)

    BFS(graph, startPointer)

    end = graph[endPointer]['p']
    begin = graph[endPointer]['p']

    while begin!=None:
        prev = graph[begin]['p'] 
        if prev == startPointer:# once prev is equal to start point we break:
            break
        begin = prev # update begin as long as we're not at the start pointer

    print(f'start at {begin}:{graph[begin]["label"]}, end at {end}:{graph[end]["label"]}\nlength of path {graph[end]["d"]-1}')

find_shortest_path(graph, "Medical clinic", "New pharm", "Super-pharm")