import copy
def graph():
	
	with open('test.txt') as f:
		#reads title "edges"
		line = f.readline()

		#creating a dictionary - adj list
		adj_list = {}

		#read line of adjacency list
		for i in range(6):
			line = f.readline()
			adj = line.split()

			#node number
			node = adj[0]
			node = node[:len(node)-1] 
			
			outgoing = []
			for i in range(1, len(adj)):
				outgoing.append(adj[i])

			#if len(outgoing) != 0:
			adj_list[node] = outgoing

		#read title "pairs"
		line = f.readline()

		#list of tuples - start/end points
		s_e = []

		#read line of (s,t) points
		for i in range(2):
			line = f.readline()
			tup = tuple(line.split())
			s_e.append(tup)	

		#print(adj_list)
		#print("---------------")
		#print(s_e)

		res = constructPaths(adj_list, s_e)
		print(res)

def constructPaths(adj, se):

	all_paths = {}
	for start, end in se:
		all_paths[(start, end)] = allPaths(start, end, adj)

	return all_paths

V = 7 #number of vertices in graph

def allPaths(start, end, adj):

	#visited = [False] * V
	visited = [False for i in range(V)]
	path = [] #current path to check
	paths = []
	allPathsHelper(start, end, adj, visited, path, paths)
	#print(paths)
	return paths 

	
def allPathsHelper(start, end, adj, visited, path, paths):

	visited[int(start)] = True
	path.append(int(start))

	if start == end:
		#print("path:", path)
		paths.append(copy.deepcopy(path))
		#print("paths:", paths)
		
	else:
		for neighbor in adj[start]:
			if visited[int(neighbor)] == False:
				allPathsHelper(neighbor, end, adj, visited, path, paths)

	path.pop()
	visited[int(start)] = False
	


if __name__ == "__main__":
	graph()
