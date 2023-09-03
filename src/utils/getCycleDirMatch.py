import pandas as pd
import os
import numpy as np
from datetime import datetime
from filterList import filterList

def getCycleDirMatch(rawDataDir, delims = None, idFormat = None, \
	keepIfPrefix = [], keepIfSuffix = [], keepIfContains = [], \
	throwIfPrefix = [], throwIfSuffix = [], throwIfContains = []):
	"""
	keep and throw arguments must of type list. Example: ["Tom", "U2OS"]
	"""
	dirs = os.listdir(rawDataDir)
	
	for x in keepIfPrefix:
		dirs = filterList(dirs, keepIfPrefix = x)
	for x in keepIfSuffix:
		dirs = filterList(dirs, keepIfSuffix = x)
	for x in keepIfContains:
		dirs = filterList(dirs, keepIfContains = x)
	for x in throwIfPrefix:
		dirs = filterList(dirs, throwIfPrefix = x)
	for x in throwIfSuffix:
		dirs = filterList(dirs, throwIfSuffix = x)
	for x in throwIfContains:
		dirs = filterList(dirs, throwIfContains = x)
	
	cycleInformation = pd.DataFrame(dirs, columns = ['dirs'])	

	#Extract the string with date and time
	dates = [x.split(delims[0])[1].split(delims[1])[0] for x in cycleInformation['dirs']]
	dirAcquisitionOrder = np.argsort([datetime.strptime(x, idFormat) for x in dates])
	
	cycleInformation = cycleInformation.reindex(dirAcquisitionOrder)
	cycleInformation.reset_index(drop = True, inplace = True)
	cycleInformation['cycle'] = np.arange(1, 1 + cycleInformation.shape[0]) 
	return(cycleInformation)




