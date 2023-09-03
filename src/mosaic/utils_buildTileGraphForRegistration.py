import networkx as nx
import pandas as pd

def buildTileGraphForRegistration(tgtTileCoords, refTileCoords): 
	"""
	Currently, assuming that target and reference cycles have identical tiling. If not, 
	could use the metadata for the two cycles and allowed maxSeparation to build the 
	layered graph.
	"""
	G = nx.Graph()
	refTiles = ['ref_' + x for x in refTileCoords[~refTileCoords['medX'].isnull()].fieldID]
	tgtTiles = ['tgt_' + x for x in tgtTileCoords[~tgtTileCoords['medX'].isnull()].fieldID]
	
	edgesToAdd = [('ref_f01', x) for x in refTiles if x != 'ref_f01'] + \
		[('tgt_f01', x) for x in tgtTiles if x != 'tgt_f01'] + \
		[(x, 'tgt_' + x[4:]) for x in refTiles]

	G.add_edges_from(edgesToAdd)

	return(G)









