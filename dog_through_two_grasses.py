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
    0: {
        "label": "grass",
        "adj": [
            {"dst": 8, "weight": 5},
            {"dst": 9, "weight": 1}
        ]
    },
    1: {
        "label": "grass",
        "adj": [
            {"dst": 10, "weight": 3},
        ]
    },
    2: {
        "label": "grass",
        "adj": [
            {"dst": 7, "weight": 1},
            {"dst": 9, "weight": 11},
            {"dst": 10, "weight": 90}
        ]
    },
    3: {
        "label": "grass",
        "adj": [
            {"dst": 8, "weight": 6},
            {"dst": 1, "weight": 1},
            {"dst": 11, "weight": 1}
        ]
    },
    4: {
        "label": "owner1",
        "adj": [
            {"dst": 2, "weight": 1}
        ]
    },
    5: {
        "label": "owner2",
        "adj": [
            {"dst": 10, "weight": 1}
        ]
    },
    6: {
        "label": "playground",
        "adj": [
            {"dst": 2, "weight": 1}
        ]
    },
    7: {
        "label": "playground",
        "adj": [
            {"dst": 10, "weight": 1}
        ]
    },
    8: {
        "label": "dog park",
        "adj": [
            {"dst": 3, "weight": 6},
            {"dst": 6, "weight": 9}
        ]
    },
    9: {
        "label": "other",
        "adj": [
            {"dst": 2, "weight": 11},
            {"dst": 0, "weight": 1}
        ]
    },
    10: {
        "label": "other",
        "adj": [
            {"dst": 5, "weight": 1},
            {"dst": 7, "weight": 1}
        ]
    },
    11: {
        "label": "other",
        "adj": [
            {"dst": 3, "weight": 1}
        ]
    }
}


def short_path(graph, label_start, label_end, label_place_to_visit_twice):
    total_distance = 0
    for key in graph.keys():
        if graph[key]["label"] == label_start:
            Dijkstra(graph, key)
            break
    min_grass_distance = math.inf
    min_grass_point = 0
    for key in graph.keys():
        if graph[key]["label"] == label_place_to_visit_twice and graph[key]["d"] < min_grass_distance:
            min_grass_distance = graph[key]["d"]
            min_grass_point = key
    total_distance += min_grass_distance
    Dijkstra(graph, min_grass_point)
    min_grass_distance = math.inf
    min_grass_point2 = 0
    for key in graph.keys():
        if graph[key]["label"] == label_place_to_visit_twice and key != min_grass_point and graph[key]["d"] < min_grass_distance:
            min_grass_distance = graph[key]["d"]
            min_grass_point2 = key
    total_distance += min_grass_distance
    Dijkstra(graph, min_grass_point2)
    for key in graph.keys():
        if graph[key]["label"] == label_end:
            total_distance += graph[key]["d"]
            break
    return total_distance


print(short_path(graph, "owner1", "owner2", "grass"))
