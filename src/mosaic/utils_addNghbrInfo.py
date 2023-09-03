import pandas as pd
import networkx as nx
import sys
sys.path.append('/c4/home/kchoudhary/bin/kcUtils/epitrainUtils/utils')
from utils_register import register

def addNghbrInfo(fieldsData, tileGph):
	"""
	fieldsData: metadata about images with these columns: 
		['id', 'Row', 'Col', 'FieldID', 'ImageResolutionX', 'URL', 
		'ImageResolutionY', 'ImageSizeX', 'ImageSizeY', 'PositionX', 'PositionY', 'AbsTime']
	tileGph: networkx object with graph of tile connections.
	"""
	dirOpposites = {'West': 'East', 'East': 'West', 'North': 'South', 'South': 'North'}  
	for nghbrs in tileGph.edges:
		im1Id = fieldsData[fieldsData.FieldID == nghbrs[0]].URL.iloc[0][6:9]
		im2Id = fieldsData[fieldsData.FieldID == nghbrs[1]].URL.iloc[0][6:9]
		if (fieldsData[fieldsData.FieldID == nghbrs[1]].PositionX.iloc[0] == \
			fieldsData[fieldsData.FieldID == nghbrs[0]].PositionX.iloc[0]):
			if (fieldsData[fieldsData.FieldID == nghbrs[1]].PositionY.iloc[0] < \
				fieldsData[fieldsData.FieldID == nghbrs[0]].PositionY.iloc[0]):
				im2LocWrtIm1 = 'South'
			else:
				im2LocWrtIm1 = 'North'
		else: #if PositionX is not equal then, PositionY must be. 
			if (fieldsData[fieldsData.FieldID == nghbrs[1]].PositionX.iloc[0] < \
				fieldsData[fieldsData.FieldID == nghbrs[0]].PositionX.iloc[0]):
				im2LocWrtIm1 = 'West'
			else:
				im2LocWrtIm1 = 'East'
		fieldsData.loc[fieldsData.FieldID == nghbrs[1], \
			'ngbrTo' + dirOpposites[im2LocWrtIm1]] = int(im1Id[1:])
		fieldsData.loc[fieldsData.FieldID == nghbrs[0], \
			'ngbrTo' + im2LocWrtIm1] = int(im2Id[1:])
	
	return(fieldsData)













