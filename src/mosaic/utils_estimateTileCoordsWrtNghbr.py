import pandas as pd
import networkx as nx
import sys
sys.path.append('/c4/home/kchoudhary/bin/kcUtils/epitrainUtils/utils')
from utils_register import register

def estimateTileCoordsWrtNghbr(images, fieldsData, tileGph):
	"""
	images: directory with fields (aka tiles) as keys and image as a numpy array
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
		thisOffset = register(images[im1Id], images[im2Id])[0]
		#Register function returns how to translate im2 so it is best aligned with im1.
		fieldsData.loc[fieldsData.FieldID == nghbrs[1], \
			'locEstYWrtNghbrTo' + dirOpposites[im2LocWrtIm1]] = thisOffset[0]
		fieldsData.loc[fieldsData.FieldID == nghbrs[1], \
			'locEstXWrtNghbrTo' + dirOpposites[im2LocWrtIm1]] = thisOffset[1]
		fieldsData.loc[fieldsData.FieldID == nghbrs[1], \
			'ngbrTo' + dirOpposites[im2LocWrtIm1]] = int(im1Id[1:])
		fieldsData.loc[fieldsData.FieldID == nghbrs[0], \
			'locEstYWrtNghbrTo' + im2LocWrtIm1] = -thisOffset[0]
		fieldsData.loc[fieldsData.FieldID == nghbrs[0], \
			'locEstXWrtNghbrTo' + im2LocWrtIm1] = -thisOffset[1]
		fieldsData.loc[fieldsData.FieldID == nghbrs[0], \
			'ngbrTo' + im2LocWrtIm1] = int(im2Id[1:])
	
	imageSizeX = fieldsData.ImageSizeX.unique()[0]
	imageSizeY = fieldsData.ImageSizeY.unique()[0]

	#Register function returns the minimum offset assuming infinitely repeated tiling of im1.
	fieldsData.locEstXWrtNghbrToWest += imageSizeX
	fieldsData.locEstXWrtNghbrToEast -= imageSizeX
	fieldsData.locEstYWrtNghbrToNorth += imageSizeY
	fieldsData.locEstYWrtNghbrToSouth -= imageSizeY
	return(fieldsData)













