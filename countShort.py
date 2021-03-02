import math

# code complexity: |V|
def Dijkstra_init(graph,vertex):   
    for key in graph.keys():
        graph[key]['d']=0 if key==vertex else math.inf
        graph[key]['p']=None
        graph[key]["counter"]=1 if key==vertex else 0


# relax gets 2 vertices (neighbor and current)- when e is (current,neighbor)
def relax(graph,neighbor,current,e):

    # if (distance from s to neighbor) is greater than (distance from s to current + distance from current to neighbor)
    if graph[neighbor]["d"]> graph[current]["d"]+e["weight"]:
        graph[neighbor]["d"]=graph[current]["d"]+e["weight"]
        graph[neighbor]["p"]=current
    if graph[neighbor]["d"] == graph[current]["d"]+e["weight"]:
        graph[neighbor]["counter"]+=graph[current]["counter"]

def getMinimal(graph, pq):
    minimal=pq[0]
    for current in pq:
        if graph[current]["d"]<graph[minimal]["d"]:
            minimal=current
    return minimal

def Dijkstra(graph,vertex):
    Dijkstra_init(graph,vertex)
    pq=list(graph.keys())
    while len(pq)>0:
        current=getMinimal(graph, pq)
        for edge in graph[current]["adj"]:
            relax(graph,edge["dst"], current, edge)
        pq.remove(current)

def print_res(graph):
    for key in graph.keys():
        print(f"vertex {key}: distance {graph[key]['d']}, num of paths {graph[key]['counter']}")

graph={
    1: {"adj":[{"dst":2,"weight":5},{"dst":4,"weight":3}]},
    2: {"adj":[{"dst":3,"weight":7}]},
    3: {"adj":[{"dst":5,"weight":1}]},
    4: {"adj":[{"dst":3,"weight":9}]},
    5: {"adj":[]}  
}

Dijkstra(graph,1)
print_res(graph)

