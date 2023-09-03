import xml.etree.ElementTree as ET
import pandas as pd
import os

#The function works for images exported by the Perkin Elmer's Harmony software.
#Assumes file format according to http://www.perkinelmer.com/PEHH/HarmonyV5
def getChannelInfo(FfcProfileXmlFileDir):
	FfcProfileXmlFilePath = os.path.join(FfcProfileXmlFileDir, \
					os.listdir(FfcProfileXmlFileDir)[0])
	tree = ET.parse(FfcProfileXmlFilePath)
	root = tree.getroot()
	
	#Get the XML namespace
	xmlns = root.tag.split('}')[0].strip('{')
	
	#Subelement of root with flat-field profiles per channel
	#Findall returns a list with all subelements named map. Hence, need to extract index 0.
	mapping = root.findall('{' + xmlns + '}Map')[0] 
	
	entries = [child[0].text for child in mapping]
	
	channelInfo = []
	for entry in entries:
		channel = entry.split('Channel: ')[1].split(',')[0]
		channelName = entry.split('ChannelName: ')[1].split(',')[0]
		dimX, dimY = [int(x) for x in \
			entry.split('Dims: ')[1].split('],')[0].strip('[').split(', ')]
		channelInfo.append({'channel': channel, 'channelName': channelName, \
			'dimX': dimX, 'dimY': dimY})
	
	channelInfo = pd.DataFrame.from_dict(channelInfo)
	return(channelInfo)




