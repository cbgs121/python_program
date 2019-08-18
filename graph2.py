class Graph:
	def __init__(self,graph_dict=None):
		if graph_dict==None:
			graph_dict = {}
		self.__graph_dict = graph_dict
		
		
	def vertices(self):
		return list(self.__graph_dict.keys())
		
	
	def edge(self):
		return self.__genrate_edges()
		
	
	def add_vertex(self,vertex):
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []
			
			
	def add_edge(self,edge):
		edge = set(edge)
		(vertex1,vertex2) = tuple(edge)
		if vertex1 in self.__graph_dict:
			self.__graph_dict[vertex1].append(vertex2)
		else:
			self.__graph_dict[vertex1] = [vertex2]
			
	
	def __genrate_edges(self):
		edge = []
		for node in self.__graph_dict:
			for vertex in self.__graph_dict[node]:
				if (node,vertex) not in edge:
					edge.append((node,vertex))
		return edge
		
	
	def __str__(self):
		res = "vertices: "
		for k in self.__graph_dict:
			res += str(k)+" "
		res += '\n edges: '
		for edge in self.__genrate_edges():
			res += str(edge) + " "
		return res
		
	# shortest path between some_start_vertex and end_vertex
	
	def  find_path(self,start_vertex,end_vertex,path=None):
		if path==None:
			path = []
		graph = self.__graph_dict
		path = path+[start_vertex]
		if start_vertex == end_vertex:
			return path
		if start_vertex not in graph:
			return None
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_path(vertex,end_vertex,path)
				if extended_path:
					return extended_path
		return None
		
	# All possible path between some_start_vertex and end_vertex
	
	def find_all_path(self,start_vertex,end_vertex,path=[]):
	
		graph= self.__graph_dict
		path = path + [start_vertex]
		
		if start_vertex == end_vertex:
			return [path]
		
		if start_vertex not in graph:
			return []
		paths = []
		for vertex in graph[start_vertex]:
			if vertex not in path:
				extended_path = self.find_all_path(vertex,end_vertex,path)
				
				for p in extended_path:
					paths.append(p)
		return paths
		
		
	def vertex_degree(self,vertex):
		adjcent_vertex = self.__graph_dict[vertex]
		degree = len(adjcent_vertex)+adjcent_vertex.count(vertex)
		return degree
		
	
	def find_isolated_vertex(self):
		isolated = []
		for vertex in self.__graph_dict:
			if not self.__graph_dict[vertex]:
				isolated+=vertex
		return isolated
	
	# to find Delta means max. degree and delta means min. degree vertex 
	
	def Delta(self):
		mx = 0
		for vertex in self.__graph_dict:
			vrt_degree = self.vertex_degree(vertex)
			if vrt_degree>mx:
				mx = vrt_degree
		return mx
		
	
	def delta(self):
		mn = 1000000000
		for vertex in self.__graph_dict:
			vrt_degree = self.vertex_degree(vertex)
			if vrt_degree <mn:
				mn = vrt_degree
		return mn
		
	
	def sequence(self):
		seq = []
		for vertex in self.__graph_dict:
			seq.append(self.vertex_degree(vertex))
		seq.sort(reverse=True)
		return tuple(seq)
		
		
		
	def density(self):
		g = self.__graph_dict
		v = len(g.keys())
		e = len(self.edge())
		return 2.0 * e/(v*(v-1))
	
	def is_connected(self,vertices_encountered=None,start_vertex=None):
		if vertices_encountered is None:
			vertices_encountered = set()
		gdict = self.__graph_dict
		vertices = list(gdict.keys())
		if not start_vertex:
			start_vertex = vertices[0]
		vertices_encountered.add(start_vertex)
		if len(vertices_encountered) != len(vertices):
			for vertex in gdict[start_vertex]:
				if vertex not in vertices_encountered:
					if self.is_connected(vertices_encountered,vertex):
						return True
		else:
			return True
		return False
		
	def diameter(self):
		v = self.vertices()
		pairs = [(v[i],v[j]) for i in range(len(v)-1) for j in range(i+1,len(v))]
		smallest_paths = []
		for (s,e) in pairs:
			paths = self.find_all_path(s,e)
			smallest = sorted(paths,key=len)[0]
			smallest_paths.append(smallest)
		smallest_paths.sort(key=len)
		
		diameter =  len(smallest_paths[-1])-1
		return diameter
	


if __name__ == "__main__":
	g ={'a':['d','f'],
		'b':['c'],
		'c':['b','c','d','e'],
		'd':['a','c'],
		'e':['c'],
		'f':['d']
		}		
		
	complete_graph = { 
    "a" : ["b","c"],
    "b" : ["a","c"],
    "c" : ["a","b"]
	}

	isolated_graph = { 
		"a" : [],
		"b" : [],
		"c" : []
	}
	
	g1 = {"a" : ["d"],
		  "b" : ["c"],
		  "c" : ["b", "c", "d", "e"],
		  "d" : ["a", "c"],
		  "e" : ["c"],
		  "f" : []
		}
	g2 = { "a" : ["d","f"],
		   "b" : ["c"],
		   "c" : ["b", "c", "d", "e"],
		   "d" : ["a", "c"],
		   "e" : ["c"],
		   "f" : ["a"]
		}
	
	g3 = { "a" : ["d","f"],
		   "b" : ["c","b"],
		   "c" : ["b", "c", "d", "e"],
		   "d" : ["a", "c"],
		   "e" : ["c"],
		   "f" : ["a"]
		}

	dim = { "a" : ["c"],
      "b" : ["c","e","f"],
      "c" : ["a","b","d","e"],
      "d" : ["c"],
      "e" : ["b","c","f"],
      "f" : ["b","e"]
		}


	graph = Graph(g)
	
	print("Vertices of graph:")
	print(graph.vertices())
	
	print("Edges of graph:")
	print(graph.edge())

	print("Add vertex:")
	graph.add_vertex("z")

	print("Vertices of graph:")
	print(graph.vertices())
	
	print("Add an edge:")
	graph.add_edge({"a","z"})
	
	print("Vertices of graph:")
	print(graph.vertices())
	
	print("Edges of graph:")
	print(graph.edge())
	print("after adding vertex {x,y}")
	graph.add_edge({'x','y'})
	print(graph.vertices())
	
	print('path b/w "a" and "b" is :')
	path = graph.find_path('a','b')
	print(path)
	print('path b/w "a" and "f" is :')
	path = graph.find_path('a','f')
	print(path)
	
	print('path b/w "c" and "c" is :')
	path = graph.find_path('c','c')
	print(path)

	print('all_path b/w "a" and "b" is :')
	path = graph.find_all_path('a','b')
	print(path)
	
	print('path b/w "a" and "f" is :')
	path = graph.find_all_path('a','f')
	print(path)
	
	print('degree of vertex c is :')
	print(graph.vertex_degree('c'))
	
	#print(g)
	
	print('isolated vertex of garph :')
	print(graph.find_isolated_vertex())
	
	print('maximum degree of vertex in graph')
	print(graph.Delta())
	print('minimum degree of vertex in graph')
	print(graph.delta())
	
	print('tuple of degree of each edges ')
	print(graph.sequence())
	
	print("Density of graph is : ")
	print(graph.density())
	
	print("Density of complete graph")
	cmpgraph = Graph(complete_graph)
	print(cmpgraph.density())
	
	print('Density of isolated graph')
	iso = Graph(isolated_graph)
	print(iso.density())
	
	print('is_connected graph ?',end=' ')
	gr1 = Graph(g1)
	print(gr1.is_connected())
	print(gr1)
	
	print('is_connected graph ?',end=' ')
	gr2 = Graph(g2)
	print(gr2.is_connected())
	print(gr2)
	
	print('is_connected graph ?',end=' ')
	gr3 = Graph(g3)
	print(gr3.is_connected())
	print(gr3)
	
	print('Diameter of graph ')
	diam = Graph(dim)
	print(diam.diameter())
	
	
	
