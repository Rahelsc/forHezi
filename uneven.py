import math


# code complexity: |V|
def Dijkstra_init(graph, vertex):
    for key in graph.keys():
        graph[key]['d'] = 0 if key == vertex else math.inf
        graph[key]['p'] = None


# relax gets 2 vertices (neighbor and current)- when e is (current,neighbor)
def relax(graph, neighbor, current, e):
    # if (distance from s to neighbor) is greater than (distance from s to current + distance from current to neighbor)
    if e["weight"] % 2 != 0 and graph[neighbor]["d"] > graph[current]["d"] + e["weight"]:
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


def uneven_path(graph, source, destination):
    Dijkstra(graph, source)
    return graph[destination]["d"]


graph = {
    0: {"adj": [
        {"dst": 1, "weight": 3},
        {"dst": 3, "weight": 7},
        {"dst": 4, "weight": 8}]},
    1: {"adj": [
        {"dst": 0, "weight": 3},
        {"dst": 3, "weight": 4},
        {"dst": 2, "weight": 1}]},
    2: {"adj": [
        {"dst": 1, "weight": 1},
        {"dst": 3, "weight": 2}
    ]},
    3: {"adj": [
        {"dst": 2, "weight": 2},
        {"dst": 1, "weight": 4},
        {"dst": 0, "weight": 7},
        {"dst": 4, "weight": 3}
    ]},
    4: {"adj": [
        {"dst": 0, "weight": 8},
        {"dst": 3, "weight": 3}
    ]}
}

print(uneven_path(graph, 2, 3))
