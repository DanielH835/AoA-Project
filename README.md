# AoA-Project
### to-do job before trying to find mutually avoid paths among res

Use 'res,s_e = graph(num_nodes,num_pairs)' to generate res on the test1.txt instance.
'res[s_e[3]]' gives all the paths with respect to the 4th pair of nodes.

Part of the result is shown below,


 [31, 34, 35, 32],
 [31, 34, 35, 33, 32],
 [31, 34, 35, 33, 37, 32],
 [31, 34, 35, 33, 37, 40, 38, 32],
 [31, 34, 35, 33, 37, 40, 38, 36, 39, 32],
 [31, 34, 35, 33, 37, 40, 39, 32],
 [31, 34, 35, 33, 37, 40, 39, 38, 32],
 [31, 34, 35, 33, 39, 32],
 [31, 34, 35, 33, 39, 37, 32],

 
 It's obvious that, if we have the first path, all other paths shown above are redundant(except for nodes 31, 34, 35, they used unecessary nodes and increase the possibility of overlapping). The helper function match() is to identify whether we need to remove some paths from the resolution.
 
