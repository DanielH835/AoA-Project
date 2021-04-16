import copy


num_nodes = 6 #number of vertices in graph
num_pairs = 2


def graph(num_nodes,num_pairs):
	
	with open('test.txt') as f:
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

		all_possible_paths = constructPaths(adj_list, s_e)
		#print(res)
		res = check_distinct(all_possible_paths)
		#return res,s_e

def mark_unvisited_for_backtracking(path, visited):
	for node in path:
		visited[int(node)-1] = False


def reject_path(path, visited):
	for node in path:
		if visited[int(node)-1]:
			return True
	for node in path:
		visited[int(node)-1] = True
	return False

def check_path_with_backtracking(path_dict, key_list, index, visited):
	possible_paths = path_dict[key_list[index]]
	for path in possible_paths:
		if reject_path(path, visited):
			continue
		else:
			if index+1 < len(key_list):
				if check_path_with_backtracking(path_dict, key_list, index+1, visited):
					return True
				else:
					#although path was accepted but for the later nodes, this creates some common
					#intersecting node, hence skip this path, check another.
					#mark nodes of this path as unvisited and go to the next path
					mark_unvisited_for_backtracking(path, visited)
					continue
				#something to return here
			else:
				#all keys have been checked for the paths
				#we have found the k distinct paths 
				return True
	#reach here if all possible paths for a particular pair of start and ending
	#vertices cannot be selected, i.e., have a common intermediate node with
	#previously selected paths. Backtrack now.
	return False

def check_distinct(path_dict):
	#fixing first pair of nodes to get the path
	visited = [False] * num_nodes
	index = 0
	key_list = list(path_dict.keys())
	paths = path_dict[key_list[0]]
	if check_path_with_backtracking(path_dict, key_list, index, visited):
		return True

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
	res = graph(num_nodes,num_pairs)
