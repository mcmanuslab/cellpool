import networkx as nx
import pandas as pd

def buildLayeredTileGraph(tgtCycleGph, refTileCoords): 
	"""
	Currently, assuming that target and reference cycles have identical tiling. If not, 
	could use the metadata for the two cycles and allowed maxSeparation to build the 
	layered graph.
	"""

	mapping = dict(zip(tgtCycleGph.nodes, ['tgt_' + str(x) for x in tgtCycleGph.nodes]))
	layeredTileGph = nx.relabel_nodes(tgtCycleGph, mapping, copy=True)
	refTiles = [int(x) for x in refTileCoords[ \
		~refTileCoords['medX'].isnull()].fieldID.str.replace('f', '')]
	layeredTileGph.add_edge('ref_1', 'tgt_1')
	edgesToAdd = [('ref_1', 'ref_' + str(x)) for x in refTiles if x != 1]
	for x in refTiles:
		edgesToAdd.append(('ref_' + str(x), 'tgt_' + str(x)))

	layeredTileGph.add_edges_from(edgesToAdd)

	return(layeredTileGph)









