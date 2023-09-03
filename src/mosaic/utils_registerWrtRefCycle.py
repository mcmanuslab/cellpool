import sys
sys.path.append('/c4/home/kchoudhary/bin/kcUtils/epitrainUtils/utils')
from utils_register import register
import pandas as pd

def registerWrtRefCycle(tgtImages, refImages, layeredTileGph):
	#Assumes that each tile in tgtImages has a single neighbor in refImages
	regCoords = {}
	for thisField in tgtImages:
		thisFieldNode = 'tgt_' + thisField
		nghbr = [x for x in layeredTileGph.neighbors(thisFieldNode) \
			if x.startswith('ref_')][0]
		nghbrFieldId = nghbr[4:]
		thisOffset = register(refImages[nghbrFieldId], \
					tgtImages[thisField])[0]
		regCoords[thisField] = {'tgtField': thisField, \
				'refField': nghbrFieldId, \
				'locEstYWrtNghbrInRefCycle': thisOffset[0], \
				'locEstXWrtNghbrInRefCycle': thisOffset[1]}

	regCoords = pd.DataFrame.from_dict(regCoords).T
	regCoords.reset_index(drop = True, inplace = True)
	return(regCoords)


