import math


# code complexity: |V|
def Dijkstra_init(graph, vertex):
    for key in graph.keys():
        graph[key]['d'] = 0 if key == vertex else math.inf
        graph[key]['p'] = None


# relax gets 2 vertices (neighbor and current)- when e is (current,neighbor)
def relax(graph, neighbor, current, e):
    # if (distance from s to neighbor) is greater than (distance from s to current + distance from current to neighbor)
    if graph[neighbor]["d"] > graph[current]["d"] + e["weight"]:
        graph[neighbor]["d"] = graph[current]["d"] + e["weight"]
        graph[neighbor]["p"] = current


def getMinimal(graph, pq):
    minimal = pq[0]
    for current in pq:
        if graph[current]["d"] < graph[minimal]["d"]:
            minimal = current
    return minimal


def Dijkstra(graph, vertex):
    Dijkstra_init(graph, vertex)
    pq = list(graph.keys())
    while len(pq) > 0:
        current = getMinimal(graph, pq)
        for edge in graph[current]["adj"]:
            relax(graph, edge["dst"], current, edge)
        pq.remove(current)


graph = {
    "maalot": {
        "adj": [{"dst": "haifa", "weight": 1}, {"dst": "herzelia", "weight": 10}, {"dst": "tel aviv", "weight": 50}]},
    "tel aviv": {"adj": [{"dst": "petach-tikva", "weight": 5}]},
    "petach-tikva": {"adj": [{"dst": "rosh-haayn", "weight": 1}]},
    "rosh-haayn": {"adj": [{"dst": "ariel", "weight": 1}]},
    "ariel": {"adj": []},
    "ramat gan": {"adj": [{"dst": "tel aviv", "weight": 2}]},
    "herzelia": {"adj": [{"dst": "ramat gan", "weight": 7}]},
    "haifa": {"adj": [{"dst": "ariel", "weight": 100}, {"dst": "herzelia", "weight": 80}]}
}


def shortpath(graph, source, middle, destination):
    path = []
    Dijkstra(graph, middle)
    current = destination
    while current is not None:
        path.insert(0, current)
        prev = graph[current]["p"]
        if prev == middle:
            break
        current = prev
    Dijkstra(graph, source)
    current = middle
    while current is not None:
        path.insert(0, current)
        prev = graph[current]["p"]
        if prev == source:
            path.insert(0, prev)
            break
        current = prev
    print(path)


shortpath(graph, "maalot", "herzelia", "ariel")
