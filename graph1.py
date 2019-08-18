graph = {
		'a':['c'],
		'b':['c','e'],
		'c':['a','b','d','e'],
		'd':['c'],
		'e':['c','b'],
		'f':[]
		}
def genrate_edges(graph):
	edges=[]
	for node in graph:
		for neighbour in graph[node]:
			edges.append((node,neighbour))
	return edges

print(genrate_edges(graph))

def isolated_node(graph):
	isolated = []
	for node in graph:
		if not graph[node]:
			isolated.append(node)
	return isolated

print(isolated_node(graph))
