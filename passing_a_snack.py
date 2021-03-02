import math


# code complexity: |V|
def Dijkstra_init(graph, vertex):
    for key in graph.keys():
        graph[key]['d'] = 0 if key == vertex else math.inf
        graph[key]['p'] = None


# relax gets 2 vertices (neighbor and current)- when e is (current,neighbor)
def relax(graph, neighbor, current, e):
    # if (distance from s to neighbor) is greater than (distance from s to current + distance from current to neighbor)
    if e["weight"] % 2 == 0 and graph[neighbor]["d"] > graph[current]["d"] + e["weight"]:
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
    0: {"adj": [{"dst": 5, "weight": 10}], "label": "yoad"},
    1: {"adj": [{"dst": 6, "weight": 100}, {"dst": 4, "weight": 22}, {"dst": 7, "weight": 26}], "label": "other"},
    2: {"adj": [{"dst": 5, "weight": 14}], "label": "shai"},
    3: {"adj": [{"dst": 7, "weight": 55}, {"dst": 6, "weight": 6}], "label": "other"},
    4: {"adj": [{"dst": 1, "weight": 22}], "label": "other"},
    5: {"adj": [{"dst": 0, "weight": 10}, {"dst": 2, "weight": 14}, {"dst": 7, "weight": 2}], "label": "other"},
    6: {"adj": [{"dst": 1, "weight": 100}, {"dst": 3, "weight": 6}], "label": "other"},
    7: {"adj": [{"dst": 1, "weight": 26}, {"dst": 3, "weight": 55}, {"dst": 5, "weight": 2}], "label": "hezi"}
}


def save_path(graph, end, path):
    current = end
    while current is not None:
        path.insert(0, current)
        prev = graph[current]["p"]
        if prev is None:
            break
        current = prev


def visit_two_friends(graph, source_label, friend1_label, friend2_label):
    path = []
    sum_path = 0

    for key in graph.keys():
        if graph[key]["label"] == source_label:
            source = key
        elif graph[key]["label"] == friend1_label:
            friend1 = key
        elif graph[key]["label"] == friend2_label:
            friend2 = key

    Dijkstra(graph, friend1)
    save_path(graph, friend2, path)
    sum_path += graph[friend2]["d"]
    Dijkstra(graph, source)
    save_path(graph, friend1, path)
    sum_path += graph[friend1]["d"]

    print(f'the path is: {path}\nlength of path is: {sum_path}')


visit_two_friends(graph, "yoad", "shai", "hezi")
