import re
import pandas as pd
import string

def getImageFileInfo(filenames, pattern):
	r = re.compile(pattern)
	outDat = {}
	for ix in range(len(filenames)):
		outDat[ix] = [m.groupdict() for m in r.finditer(filenames[ix])][0]
		outDat[ix]['filename'] = filenames[ix]
	outDat = pd.DataFrame.from_dict(outDat).T
	outDat[['Row', 'Column', 'Field', 'Z', 'Channel']] = \
		outDat[['Row', 'Column', 'Field', 'Z', 'Channel']].astype('int32', copy = False)
	outDat['Well'] = outDat[['Row', 'Column']].apply( \
		lambda x: list(string.ascii_uppercase)[x[0] - 1] + \
				f"{x[1]:02d}", axis = 1)
	return outDat
