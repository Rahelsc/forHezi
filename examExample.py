import math

# code complexity: |V|
def Dijkstra_init(graph,vertex):   
    for key in graph.keys():
        graph[key]['d']=0 if key==vertex else math.inf
        graph[key]['p']=None


# relax gets 2 vertices (neighbor and current)- when e is (current,neighbor)
def relax(graph,neighbor,current,e):

    # if (distance from s to neighbor) is greater than (distance from s to current + distance from current to neighbor)
    if graph[neighbor]["d"]> graph[current]["d"]+e["weight"]:
        graph[neighbor]["d"]=graph[current]["d"]+e["weight"]
        graph[neighbor]["p"]=current

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


graph ={
    0:{"adj":[
        {"dst":1, "weight":4},
        {"dst":7, "weight":8}]},
    1:{"adj":[
        {"dst":0, "weight":4},
        {"dst":2, "weight":8},
        {"dst":7, "weight":11}]},
    2:{"adj":[
        {"dst":1, "weight":8},
        {"dst":8, "weight":2},
        {"dst":5, "weight":4},
        {"dst":3, "weight":7}
    ]},
    3:{"adj":[
        {"dst":2, "weight":7},
        {"dst":5, "weight":14},
        {"dst":4, "weight":9}
    ]},
    4:{"adj":[
        {"dst":3, "weight":9},
        {"dst":5, "weight":10}
    ]},
    5:{"adj":[
        {"dst":4, "weight":10},
        {"dst":3, "weight":14},
        {"dst":2, "weight":4},
        {"dst":6, "weight":2}
    ]},
    6:{"adj":[
        {"dst":5, "weight":2},
        {"dst":8, "weight":6},
        {"dst":7, "weight":1}
    ]},
    7:{"adj":[
        {"dst":0, "weight":8},
        {"dst":1, "weight":11},
        {"dst":8, "weight":7},
        {"dst":6, "weight":1}
    ]},
    8:{"adj":[
        {"dst":2, "weight":2},
        {"dst":6, "weight":6},
        {"dst":7, "weight":7}
    ]}
}

def find_path(graph, path, start, end):
    path.append("(")
    path.append(end)
    current = end
    while current!=None:
        prev = graph[current]['p']
        path.append(prev)
        if prev==start:
            break
        current = prev
    
    path.append(")")


def get_triangle(graph, start, middle, end):
    distance = 0
    path = []
    Dijkstra(graph, start)
    distance+=graph[middle]["d"]
    find_path(graph, path, start, middle)
    distance+=graph[end]["d"]
    find_path(graph, path, start, end)
    Dijkstra(graph, middle)
    distance+=graph[end]["d"]
    find_path(graph, path, middle, end)
    print(path)
    return distance

print(get_triangle(graph, 2,7,5))

