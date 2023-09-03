import pandas as pd
import numpy as np
import networkx as nx

def pruneTileGph(tileGph, coordEsts):
	"""
		coordEsts: dataframe with estimated locations of tiles based on phase correlation.
	"""
	
	edges_to_remove = []
	for row in range(coordEsts.shape[0]):
		thisField = coordEsts.FieldID.iloc[row]
		badNghbr = [coordEsts['ngbrTo' + x].iloc[row] for x in \
			['North', 'South', 'East', 'West'] if \
			np.isnan(coordEsts['locEstXWrtNghbrTo' + x].iloc[row])]
		badNghbr = [x for x in badNghbr if not np.isnan(x)]
		edges_to_remove.append([(thisField, int(x)) for x in badNghbr])
	
	#Flatten edges_to_remove which is a list of lists.
	edges_to_remove = [edge for sublist in edges_to_remove for edge in sublist]

	tileGph.remove_edges_from(edges_to_remove)
	return(tileGph)








