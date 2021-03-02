number_of_vertices = 6

graph = {i:[] for i in range(1,number_of_vertices+1)}

graph[1].append(2)
graph[1].append(4)

graph[2].append(1)
graph[2].append(4)
graph[2].append(6)

graph[4].append(2)
graph[4].append(3)
graph[4].append(6)
graph[4].append(5)

graph[3].append(4)

print(graph)