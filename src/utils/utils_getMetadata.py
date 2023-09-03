import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np

#The function works for images exported by the Perkin Elmer's Harmony software.
#Assumes file format according to http://www.perkinelmer.com/PEHH/HarmonyV5
def getMetadata(imageIndexXmlFilePath):
	tree = ET.parse(imageIndexXmlFilePath)
	root = tree.getroot()
	
	#Get the XML namespace
	xmlns = root.tag.split('}')[0].strip('{')
	
	#Subelement of root with image descriptions per channel
	#Findall returns a list with all subelements. Hence, need to extract index 0.
	images = root.findall('{' + xmlns + '}Images')[0] 
	
	metadataTbl = []
	for child in images:
		thisImageTags = []
		thisImageTexts = []
		for gChild in child:
			thisImageTags.append(gChild.tag.split('}')[1])
			thisImageTexts.append(gChild.text)
		metadataTbl.append(dict(zip(thisImageTags, thisImageTexts)))

	metadataTbl = pd.DataFrame.from_dict(metadataTbl)
	numericCols = ['Row', 'Col', 'FieldID', 'PlaneID', 'TimepointID', 'ChannelID', \
		'FlimID', 'ImageResolutionX', 'ImageResolutionY', 'ImageSizeX', \
		'ImageSizeY', 'BinningX', 'BinningY', 'MaxIntensity', 'PositionX', \
		'PositionY', 'PositionZ', 'AbsPositionZ', 'MeasurementTimeOffset', \
		'MainExcitationWavelength', 'MainEmissionWavelength', 'ObjectiveMagnification', \
		'ObjectiveNA', 'ExposureTime']
	metadataTbl[numericCols] = metadataTbl[numericCols].apply(pd.to_numeric, errors='coerce')
	return(metadataTbl)




