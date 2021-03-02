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

def print_res(graph):
    for key in graph.keys():
        print(f"{key}:{graph[key]['d']},{graph[key]['p']}")

graph={
    0: {"adj": [], "label":"restaurant"},
    1: {"adj":[{"dst":0,"weight":10}], "label":"other"},
    2: {"adj":[{"dst":1,"weight":17}], "label":"coffee"},
    3: {"adj":[{"dst":2,"weight":7}, {"dst":4,"weight":12}], "label":"coffee"},
    4: {"adj":[{"dst":5,"weight":4}], "label":"other"},
    5: {"adj":[], "label":"restaurant"},
    6: {"adj":[{"dst":5,"weight":13}], "label":"other"},
    7: {"adj":[{"dst":5,"weight":20},{"dst":6,"weight":14}], "label":"coffee"}
}

# Dijkstra(graph, "s")
# print_res(graph)

def get_min_path(graph, start_label, end_label):
    end_pointer = len(graph)
    start_pointer = end_pointer+1

    graph[end_pointer] = {"adj":[], "label":end_label}
    graph[start_pointer] = {"adj":[], "label":start_label}

    for key in graph.keys():
        if graph[key]["label"] == start_label:
            graph[start_pointer]["adj"].append({"dst":key, "weight":0})
        elif graph[key]["label"] == end_label:
            graph[key]["adj"].append({"dst":end_pointer, "weight":0})
    
    Dijkstra(graph, start_pointer)

    end = graph[end_pointer]["p"]
    current = end

    while current!=None:
        prev = graph[current]["p"]
        if prev == start_pointer:
            break
        current = prev

    
    print(f'meet at {start_label}:{current}, from there go to {end_label}:{end}, distance is: {graph[end]["d"]}')


get_min_path(graph, "coffee", "restaurant")