import copy


num_nodes = 100 #number of vertices in graph
num_pairs = 10


def graph(num_nodes,num_pairs):
	
	with open('test1.txt') as f:
		#reads title "edges"
		line = f.readline()

		#creating a dictionary - adj list
		adj_list = {}

		#read line of adjacency list
		for i in range(num_nodes):
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
		for i in range(num_pairs):
			line = f.readline()
			tup = tuple(line.split())
			s_e.append(tup)	

		#print(adj_list)
		#print("---------------")
		#print(s_e)

		res = constructPaths(adj_list, s_e)
		#print(res)
		return res,s_e

def constructPaths(adj, se):

	all_paths = {}
	for start, end in se:
		all_paths[(start, end)] = allPaths(start, end, adj)

	return all_paths


def allPaths(start, end, adj):


	visited = [False for i in range(num_nodes)]
	path = [] #current path to check
	paths = []
	allPathsHelper(start, end, adj, visited, path, paths)
	#print(paths)
	return paths 

	
def allPathsHelper(start, end, adj, visited, path, paths):

	visited[int(start)-1] = True
	path.append(int(start))

	if start == end:
		#print("path:", path)
		paths.append(copy.deepcopy(path))
		#print("paths:", paths)
		
	else:
		for neighbor in adj[start]:
			if visited[int(neighbor)-1] == False:
				allPathsHelper(neighbor, end, adj, visited, path, paths)

	path.pop()
	visited[int(start)-1] = False
	
	
def match(list1, list2): #a function to help remove the redundant paths from a solution
    for i in range(len(list1[:-1])):
        if list1[i] != list2[i]:
            return False
    return True	


if __name__ == "__main__":
	res,s_e = graph(num_nodes,num_pairs)
