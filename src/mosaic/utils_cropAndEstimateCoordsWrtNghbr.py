import pandas as pd
import networkx as nx
import sys
import numpy as np
sys.path.append('/c4/home/kchoudhary/bin/kcUtils/epitrainUtils/utils')
from utils_register import register

def cropAndEstimateCoordsWrtNghbr(images, coordEsts, cropFraction = 0.25):
	"""
	images: directory with fields (aka tiles) as keys and image as a numpy array
	coordEsts: output from filtering coordinate estimates 
	"""
	directions = {'West': 'East', 'East': 'West', 'North': 'South', 'South': 'North'}
	imageSize = coordEsts.ImageSizeX.unique()[0] #Assuming square tiles
	cropSize = round(imageSize * cropFraction)
	adjustForInfTilingByPhsCorr = {'West' : {'X': imageSize, 'Y': 0}, \
		'East': {'X': -imageSize, 'Y': 0}, 'North': {'X': 0, 'Y': imageSize}, \
		'South': {'X': 0, 'Y': -imageSize}} 
	for row in range(coordEsts.shape[0]):
		#If the field in this row has already been placed properly, skip to next iteration.
		if (not np.isnan(coordEsts.iloc[row][['locEstYWrtNghbrTo' + x for \
			x in directions]].tolist()).all()):
			continue
	
		im1Id = coordEsts.iloc[row].URL[6:9]
		for nghbrDir in directions:
			thisNghbr = coordEsts.iloc[row]['ngbrTo' + nghbrDir]
			if (np.isnan(thisNghbr)):
				continue
			
			im2Id = coordEsts[coordEsts.FieldID == thisNghbr].URL.iloc[0][6:9]
			if (nghbrDir == 'North'):
				im1 = images[im1Id][:cropSize, :]
				im2 = images[im2Id][-cropSize:, :]
			elif (nghbrDir == 'South'):
				im1 = images[im1Id][-cropSize:, :]
				im2 = images[im2Id][:cropSize, :]
			elif (nghbrDir == 'West'):
				im1 = images[im1Id][:, :cropSize]
				im2 = images[im2Id][:, -cropSize:]
			elif (nghbrDir == 'East'):
				im1 = images[im1Id][:, -cropSize:]
				im2 = images[im2Id][:, :cropSize]
			
			thisOffset = register(im1, im2)[0]
		
			#Register function returns how to translate im2 for best alignment with im1.
			coordEsts.loc[coordEsts.FieldID == int(im2Id[1:]), \
				'locEstYWrtNghbrTo' + directions[nghbrDir]] = thisOffset[0] + \
				adjustForInfTilingByPhsCorr[directions[nghbrDir]]['Y']
			coordEsts.loc[coordEsts.FieldID == int(im2Id[1:]), \
				'locEstXWrtNghbrTo' + directions[nghbrDir]] = thisOffset[1] + \
				adjustForInfTilingByPhsCorr[directions[nghbrDir]]['X']
			coordEsts.loc[coordEsts.FieldID == int(im1Id[1:]), \
				'locEstYWrtNghbrTo' + nghbrDir] = -thisOffset[0] + \
				adjustForInfTilingByPhsCorr[nghbrDir]['Y']
			coordEsts.loc[coordEsts.FieldID == int(im1Id[1:]), \
				'locEstXWrtNghbrTo' + nghbrDir] = -thisOffset[1] + \
				adjustForInfTilingByPhsCorr[nghbrDir]['X']
	
	return(coordEsts)













