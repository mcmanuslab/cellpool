import sys
sys.path.append('/c4/home/kchoudhary/bin/kcUtils/epitrainUtils/utils')
from utils_register import register

def registerWrtRefCycleWithSimultaneousStitchAndReg(tgtImages, refImages, \
		coordEsts, layeredTileGph):
	#Assumes that each tile in tgtImages has a single neighbor in refImages
	for thisField in tgtImages:
		thisFieldNode = 'tgt_' + str(int(thisField[1:]))
		nghbr = [x for x in layeredTileGph.neighbors(thisFieldNode) \
			if x.startswith('ref_')][0]
		nghbrFieldId = int(nghbr[4:])
		thisOffset = register(refImages['f' + f"{nghbrFieldId:02}"], \
					tgtImages[thisField])[0]
		coordEsts.loc[coordEsts.FieldID == int(thisField[1:]), \
			'ngbrInRefCycle'] = nghbr
		coordEsts.loc[coordEsts.FieldID == int(thisField[1:]), \
			'locEstYWrtNghbrInRefCycle'] = thisOffset[0]
		coordEsts.loc[coordEsts.FieldID == int(thisField[1:]), \
			'locEstXWrtNghbrInRefCycle'] = thisOffset[1]
	return(coordEsts)


