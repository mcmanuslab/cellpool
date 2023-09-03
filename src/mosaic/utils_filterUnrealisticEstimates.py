import pandas as pd
import numpy as np
import networkx as nx

def filterUnrealisticEstimates(coordEsts, maxDevFromMedTranslation = 3, filterWrtRefCycle = False, \
				maxTranslation = 20, expectedDispOfNgbrs = 'NA'):
	"""
		coordEsts: dataframe with estimated locations of tiles based on phase correlation.
	"""
	#Remove neighbors with excessive estimated translation.
	#Assumes that there are minor mechanical errors from a calibrated camera movement.
	if (filterWrtRefCycle):
		coordEsts.loc[(abs(coordEsts.locEstXWrtNghbrInRefCycle - \
			np.nanmedian(coordEsts.locEstXWrtNghbrInRefCycle)) > \
			maxDevFromMedTranslation) | (abs(coordEsts.locEstYWrtNghbrInRefCycle - \
			np.nanmedian(coordEsts.locEstYWrtNghbrInRefCycle)) > \
			maxDevFromMedTranslation), ['locEstXWrtNghbrInRefCycle', \
			'locEstYWrtNghbrInRefCycle']] = np.nan
		coordEsts.loc[(abs(coordEsts.locEstXWrtNghbrInRefCycle) > maxTranslation) | \
			(abs(coordEsts.locEstYWrtNghbrInRefCycle) > maxTranslation), \
			['locEstXWrtNghbrInRefCycle', 'locEstYWrtNghbrInRefCycle']] = np.nan
		return(coordEsts)

	if expectedDispOfNgbrs == 'NA':
		coordEsts.loc[(abs(coordEsts.locEstXWrtNghbrToWest - \
			np.nanmedian(coordEsts.locEstXWrtNghbrToWest)) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstYWrtNghbrToWest) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToWest', 'locEstYWrtNghbrToWest']] = np.nan
		coordEsts.loc[(abs(coordEsts.locEstXWrtNghbrToEast - \
			np.nanmedian(coordEsts.locEstXWrtNghbrToEast)) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstYWrtNghbrToEast) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToEast', 'locEstYWrtNghbrToEast']] = np.nan
		coordEsts.loc[(abs(coordEsts.locEstYWrtNghbrToNorth - \
			np.nanmedian(coordEsts.locEstYWrtNghbrToNorth)) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstXWrtNghbrToNorth) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToNorth', 'locEstYWrtNghbrToNorth']] = np.nan
		coordEsts.loc[(abs(coordEsts.locEstYWrtNghbrToSouth - \
			np.nanmedian(coordEsts.locEstYWrtNghbrToSouth)) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstXWrtNghbrToSouth) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToSouth', 'locEstYWrtNghbrToSouth']] = np.nan
	else:
		coordEsts.loc[(abs(abs(coordEsts.locEstXWrtNghbrToWest) - expectedDispOfNgbrs) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstYWrtNghbrToWest) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToWest', 'locEstYWrtNghbrToWest']] = np.nan
		coordEsts.loc[(abs(abs(coordEsts.locEstXWrtNghbrToEast) - expectedDispOfNgbrs) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstYWrtNghbrToEast) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToEast', 'locEstYWrtNghbrToEast']] = np.nan
		coordEsts.loc[(abs(abs(coordEsts.locEstYWrtNghbrToNorth) - expectedDispOfNgbrs) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstXWrtNghbrToNorth) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToNorth', 'locEstYWrtNghbrToNorth']] = np.nan
		coordEsts.loc[(abs(abs(coordEsts.locEstYWrtNghbrToSouth) - expectedDispOfNgbrs) > \
			maxDevFromMedTranslation) | \
			(abs(coordEsts.locEstXWrtNghbrToSouth) > maxDevFromMedTranslation), \
			['locEstXWrtNghbrToSouth', 'locEstYWrtNghbrToSouth']] = np.nan

	return(coordEsts)








