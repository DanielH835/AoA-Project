import copy
import sys


num_nodes = 20 #number of vertices in graph
num_pairs = 4

result_path = {}

def graph(num_nodes, num_pairs, samplein):
	
	with open(samplein) as f:
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
		return res

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
					result_path[key_list[index]] = path
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
				result_path[key_list[index]] = path #adding path for the last pair of nodes
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
	pre_visited = []

	for start, end in se:
		if end in adj[start]:
			all_paths[(start, end)] = [[start, end]]
			pre_visited.append(start)
			pre_visited.append(end)
		else:
			all_paths[(start, end)] = allPaths(start, end, adj, pre_visited)
		#all_paths[(start, end)] = allPaths(start, end, adj)

	return all_paths


def allPaths(start, end, adj, pre_visited):


	visited = [False for i in range(num_nodes)]
	for node in pre_visited:
		visited[int(node)] = True

	path = [] #current path to check
	paths = []
	counter = 1
	allPathsHelper(start, end, adj, visited, path, paths,counter)
	#print(paths)
	return paths 

	
def allPathsHelper(start, end, adj, visited, path, paths,counter):

	visited[int(start)-1] = True
	path.append(int(start))
	#check = False

	if start == end:
		if len(path) == counter:
			#paths = [[start, end]]
			print("path:", path)
			paths.append(copy.deepcopy(path))
			return
		else:
			print("path:", path)
			paths.append(copy.deepcopy(path))
		#print("path:", path)
		#paths.append(copy.deepcopy(path))
		
	else:
		if end in adj[start]:
			a = adj[start]
			temp = adj[start].index(end)
			a[0],a[temp]  =  a[temp],a[0]
			#check = True
		counter+=1
		for neighbor in adj[start]:
			if visited[int(neighbor)-1] == False:
				allPathsHelper(neighbor, end, adj, visited, path, paths,counter)
	#if len(path) == 2:
	#	return
	path.pop()
	#if check:
	#	path.pop()
	#else:
	#	visited[int(start)-1] = False
	visited[int(start)-1] = False



def main(*argv):
	samplein = sys.argv[1]
	
	res = graph(num_nodes, num_pairs, samplein)
	if res:
		sorted_tup = sorted(result_path.keys())
		print(sorted_tup)
		f = open("sampleout.txt", "w")

		print("We found", len(sorted_tup), "distinct paths:")

		for tup in sorted_tup:
			f.write(tup[0])
			f.write(" ")
			print(tup[0], end=" ")
			edges = result_path[tup]
			for i in range(1, len(edges)):
				f.write(str(edges[i]))
				f.write(" ")
				print(edges[i], end=" ")
			f.write("\n")
			print(" ")

		f.close()

	else:
		print("Cannot find any path, do better next time!")

if __name__ == "__main__":
	main()
