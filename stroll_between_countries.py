import math


# code complexity: |V|
def BFS_init(graph, vertex, queue):
    for key in graph.keys():
        graph[key]['d'] = 0 if key == vertex else math.inf
        graph[key]['p'] = None
    queue.append(vertex)


# code complexity: |E|+|V|
def BFS(graph, vertex):
    queue = []
    BFS_init(graph, vertex, queue)
    while len(queue) > 0:
        curr = queue.pop(0)
        for adj in graph[curr]['adj']:
            if graph[adj]['d'] == math.inf:
                queue.append(adj)
                graph[adj]['d'] = graph[curr]['d'] + 1
                graph[adj]['p'] = curr


graph = {
    "paris": {
        "country": "france",
        "adj": ["Mulhouse", "touluz"]
    },
    "touluz": {
        "country": "france",
        "adj": ["paris", "Mulhouse", "luxembug"]
    },
    "Mulhouse": {
        "country": "france",
        "adj": ["paris", "touluz", "marcei", "minchen"]
    },
    "marcei": {
        "country": "france",
        "adj": ["Mulhouse", "berlin"]
    },
    "minchen": {
        "country": "germany",
        "adj": ["paris", "berlin", "luxembug", "humburg"]
    },
    "berlin": {
        "country": "germany",
        "adj": ["luxembug", "minchen"]
    },
    "luxembug": {
        "country": "germany",
        "adj": ["berlin", "minchen"]
    },
    "humburg": {
        "country": "germany",
        "adj": ["luxembug", "minchen"]
    }
}


def france_to_berlin(graph):
    start_pointer = len(graph)
    graph[start_pointer] = {
        "country": "france",
        "adj": []
    }

    for key in graph.keys():
        if graph[key]["country"] == "france":
            graph[start_pointer]["adj"].append(key)

    BFS(graph, start_pointer)

    current = "berlin"

    while current is not None:
        prev = graph[current]["p"]
        if prev == start_pointer:
            break
        current = prev

    print(f'closest city to berlin is: {current}')


france_to_berlin(graph)