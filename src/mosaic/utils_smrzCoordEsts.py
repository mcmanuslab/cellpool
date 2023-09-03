import numpy as np
import pandas as pd

def smrzCoordEsts(centroidLocs, coordEsts, root): 
	smryCntrdLocs = {}
	for thisField in coordEsts.FieldID:
		thisFieldImId = coordEsts[coordEsts['FieldID'] == thisField].URL.iloc[0][6:9]
		if (thisField == root):
			smryCntrdLocs[thisField] = {'fieldID' : thisFieldImId, \
				'medX' : 0, 'medY' : 0, 'stdX' : 0, 'stdY' : 0, 'nPaths' : 0}
			continue
		if (len(centroidLocs[thisField]) == 0):
			smryCntrdLocs[thisField] = {'fieldID' : thisFieldImId, \
					'medX' : np.nan, 'medY' : np.nan, \
					'stdX' : np.nan, 'stdY' : np.nan, 'nPaths' : 0}
			continue
		thisMedianX = np.nanmedian([round(x[1], 1) for x in centroidLocs[thisField]])
		thisMedianY = np.nanmedian([round(x[2], 1) for x in centroidLocs[thisField]])
		if (len(centroidLocs[thisField]) == 1):
			thisStdX, thisStdY = [np.nan, np.nan]
		else:
			thisStdX = np.nanstd([round(x[1], 1) for x in centroidLocs[thisField]])
			thisStdY = np.nanstd([round(x[2], 1) for x in centroidLocs[thisField]])
		smryCntrdLocs[thisField] = {'fieldID' : thisFieldImId, \
					'medX' : round(thisMedianX, 1), \
					'medY' : round(thisMedianY, 1), \
					'stdX' : round(thisStdX, 1), \
					'stdY' : round(thisStdY, 1), \
					'nPaths' : len(centroidLocs[thisField])}
	
	smryCntrdLocs = pd.DataFrame.from_dict(smryCntrdLocs).T
	return(smryCntrdLocs)






