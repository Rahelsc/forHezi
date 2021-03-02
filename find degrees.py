from typing import Counter


number_of_vertices = 6

graph = {i:{"counter":0,"adj":[]} for i in range(1,number_of_vertices+1)}

graph[1]["adj"].append(2)
graph[1]["adj"].append(4)

graph[2]["adj"].append(1)
graph[2]["adj"].append(4)
graph[2]["adj"].append(6)

graph[4]["adj"].append(2)
graph[4]["adj"].append(3)
graph[4]["adj"].append(6)
graph[4]["adj"].append(5)

graph[3]["adj"].append(4)

for key in graph.keys():
    graph[key]["counter"] = len(graph[key]["adj"])
    for k in graph.keys():
        if key in graph[k]["adj"] and k not in graph[key]["adj"]:
            graph[key]["counter"] +=1

print(graph)