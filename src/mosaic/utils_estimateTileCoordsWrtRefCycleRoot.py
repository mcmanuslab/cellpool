import networkx as nx

def estimateTileCoordsWrtRefCycleRoot(coordEsts, refTileCoords, layeredTileGph, \
					root = 'ref_1', maxDepth = 15, maxPaths = 10):
	centroidLocs = {}
	directions = ['ToNorth', 'ToSouth', 'ToEast', 'ToWest', 'InRefCycle']
	for toPlace in coordEsts.FieldID:
		thisPaths = []
		currDepth = 0
		while (len(thisPaths) < maxPaths) & (currDepth < maxDepth):
			thisPaths.extend(list(nx.all_simple_paths(layeredTileGph, root, \
				'tgt_' + str(toPlace), cutoff = currDepth))[:maxPaths])
			thisPaths = [list(x) for x in set(tuple(x) for x in thisPaths)]
			currDepth += 1
		thisPaths = sorted(thisPaths, key = len)[:maxPaths]
		centroidLocs[toPlace] = []
		for path in thisPaths:
			thisX, thisY = [0, 0]
			previous_node = path[0]
			thisFieldNum = int(previous_node[4:])
			thisRefCoords = refTileCoords[refTileCoords.fieldID == \
				'f' + f"{thisFieldNum:02}"]
			thisX += thisRefCoords.medX.iloc[0]
			thisY += thisRefCoords.medY.iloc[0]
			for thisNode in path[1:]:
				if (thisNode.startswith('ref_')):
					thisFieldNum = int(thisNode[4:])
					thisRefCoords = refTileCoords[refTileCoords.fieldID == \
						'f' + f"{thisFieldNum:02}"]
					thisX += thisRefCoords.medX.iloc[0]
					thisY += thisRefCoords.medY.iloc[0]
					previous_node = thisNode
					continue
				thisCoordEsts = coordEsts[coordEsts.FieldID == int(thisNode[4:])]
				thisNodeNghbrs = dict(zip(directions, \
					[thisCoordEsts['ngbr' + x].iloc[0] for x in directions]))
				prevNodeDirWrtThisNode = [x for x in thisNodeNghbrs.keys() if \
					thisNodeNghbrs[x] == previous_node][0]
				thisX += thisCoordEsts['locEstXWrtNghbr' + \
					prevNodeDirWrtThisNode].iloc[0]
				thisY += thisCoordEsts['locEstYWrtNghbr' + \
					prevNodeDirWrtThisNode].iloc[0]
				previous_node = int(thisNode[4:])
			centroidLocs[toPlace].append([path, thisX, thisY])
	return(centroidLocs)




