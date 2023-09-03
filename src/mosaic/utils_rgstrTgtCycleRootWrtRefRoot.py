import pandas as pd
import networkx as nx

def rgstrTgtCycleRootWrtRefRoot(regCoords, refStchCoords, tgtStchCoords, \
		root, tileGph):
	allPaths = list(nx.all_simple_paths(tileGph, 'ref_' + root, 'tgt_' + root))
	locEstsX = []
	locEstsY = []
	pathCenterFld = []
	for path in allPaths:
		if len(path) == 2:
			locEstsY.append(regCoords[regCoords.tgtField == \
				root]['locEstYWrtNghbrInRefCycle'].iloc[0])
			locEstsX.append(regCoords[regCoords.tgtField == \
				root]['locEstXWrtNghbrInRefCycle'].iloc[0])
			pathCenterFld.append(root)
			continue

		fldBtwnRoots = path[1][4:]
		thisX = refStchCoords[refStchCoords.fieldID == fldBtwnRoots]['medX'].iloc[0] + \
			regCoords[regCoords.tgtField == fldBtwnRoots][ \
				'locEstXWrtNghbrInRefCycle'].iloc[0] - \
			tgtStchCoords[tgtStchCoords.fieldID == fldBtwnRoots]['medX'].iloc[0]
		thisY = refStchCoords[refStchCoords.fieldID == fldBtwnRoots]['medY'].iloc[0] + \
			regCoords[regCoords.tgtField == fldBtwnRoots][ \
				'locEstYWrtNghbrInRefCycle'].iloc[0] - \
			tgtStchCoords[tgtStchCoords.fieldID == fldBtwnRoots]['medY'].iloc[0]
		locEstsX.append(thisX)
		locEstsY.append(thisY)
		pathCenterFld.append(fldBtwnRoots)

	locEsts = pd.DataFrame(pathCenterFld, columns = ['pathCenterField'])
	locEsts['Y'] = locEstsY
	locEsts['X'] = locEstsX
	return(locEsts)
		


	
