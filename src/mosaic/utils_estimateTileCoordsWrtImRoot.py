import networkx as nx

def estimateTileCoordsWrtImRoot(coordEsts, tileGph, root = 1, maxDepth = 15, maxPaths = 10):
	centroidLocs = {}
	directions = ['North', 'South', 'East', 'West']
	for toPlace in coordEsts.FieldID:
		thisPaths = []
		currDepth = 15 if (maxDepth > 15) else maxDepth
		if nx.has_path(tileGph, root, toPlace):
			while (len(thisPaths) < maxPaths) & (currDepth < maxDepth):
				allSimplePaths = list(nx.all_simple_paths(tileGph, root, \
					toPlace, cutoff = currDepth))
				allSimplePaths = sorted(allSimplePaths, key = len)
				thisPaths.extend(allSimplePaths[:maxPaths])
				thisPaths = [list(x) for x in set(tuple(x) for x in thisPaths)]
				currDepth += 1

		thisPaths = sorted(thisPaths, key = len)[:maxPaths]
		centroidLocs[toPlace] = []
		for path in thisPaths:
			thisX, thisY = [0, 0]
			previous_node = path[0]
			for thisNode in path[1:]:
				thisCoordEsts = coordEsts[coordEsts.FieldID == thisNode]
				thisNodeNghbrs = dict(zip(directions, \
					[thisCoordEsts['ngbrTo' + x].iloc[0] for x in directions]))
				prevNodeDirWrtThisNode = [x for x in thisNodeNghbrs.keys() if \
					thisNodeNghbrs[x] == previous_node][0]
				thisX += thisCoordEsts['locEstXWrtNghbrTo' + \
					prevNodeDirWrtThisNode].iloc[0]
				thisY += thisCoordEsts['locEstYWrtNghbrTo' + \
					prevNodeDirWrtThisNode].iloc[0]
				previous_node = thisNode
			centroidLocs[toPlace].append([path, thisX, thisY])
	return(centroidLocs)




