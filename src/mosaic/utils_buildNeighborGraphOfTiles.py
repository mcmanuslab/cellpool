import networkx as nx
import pandas as pd

#Receives a metadata table as read from Harmony exported XML.
#Assumes a 96-well plate.
#Outputs a graph linking neighbors.

def buildNeighborGraphOfTiles(fieldsData, maxSeparation = 1.2): 
	"""
	minProximity: maximum separation (in units of tile size) to still consider neighbors.
	"""

	#Block distance of 1 means adjacent block
	fieldsData['BlockDistanceFromField1X'] = fieldsData['PositionX'] / \
		(fieldsData['ImageResolutionX'] * fieldsData['ImageSizeX'])
	fieldsData['BlockDistanceFromField1Y'] = fieldsData['PositionY'] / \
		(fieldsData['ImageResolutionY'] * fieldsData['ImageSizeY'])

	tileGraph = nx.Graph()
	tileGraph.add_nodes_from([x for x in fieldsData.FieldID])
	for i in range(fieldsData.FieldID.min(), fieldsData.FieldID.max()):
		for j in range(i+1, fieldsData.FieldID.max() + 1):
			thisFields = fieldsData[fieldsData.FieldID.isin([i, j])]
			thisBlockDistsFromField1X = thisFields.BlockDistanceFromField1X.tolist()
			thisBlockDistsX = abs(thisBlockDistsFromField1X[0] - \
				thisBlockDistsFromField1X[1])
			thisBlockDistsFromField1Y = thisFields.BlockDistanceFromField1Y.tolist()
			thisBlockDistsY = abs(thisBlockDistsFromField1Y[0] - \
				thisBlockDistsFromField1Y[1])
			if (thisBlockDistsX + thisBlockDistsY < maxSeparation):
				tileGraph.add_edge(i, j)

	return(tileGraph)









