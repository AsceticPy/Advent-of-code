graph = {}

def findPath(g, node, visit):
	if node == 'end':
		return 1
	if node in visit:
		return 0
	if node.islower():
		visit = visit  | {node}
	
	return sum(findPath(g, n, visit) for n in graph[node])
	
		 
with open('data.txt', 'r') as data_file:
	lines = [line.strip() for line in data_file]
	for line in lines:
		[n, e] = line.split('-')
		graph.setdefault(n, []).append(e)
		graph.setdefault(e, []).append(n)
	
	print(findPath(graph, 'start', frozenset()))
