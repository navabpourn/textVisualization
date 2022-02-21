# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:36:42 2022
@author: Nafiseh Navabpour
This code will read a colormap and illustrates colors.
"""

from PIL import Image
import numpy as np

from xml.dom import minidom
#from HafezHelper2 import readColorMap

'''
This function read the XML file contains color maps,
return a list of [x,r,g,b]
'''
def readColorMap(colorMapFile, colorMapName):
    try:
        colorMapFile = open(colorMapFile)
        xmldoc = minidom.parse(colorMapFile)   #color map xml 
        itemlist = xmldoc.getElementsByTagName('ColorMap')
        rgbCodes = []
        colormapNameExist = False
        for s in itemlist:   #find color map
            if (s.attributes['name'].value == colorMapName):
                colormapNameExist = True 
                colorList = s.getElementsByTagName('Point')                
                for col in colorList:  #collect color id relates to numbers 
                    #input ('')
                    rgbCode = []              
                    xv = "%.4f" % float(col.attributes['x'].value)  #"%.2f"
                    rgbCode.append(xv)
                    rcode = round(float(col.attributes['r'].value))
                    gcode = round(float(col.attributes['g'].value))
                    bcode = round(float(col.attributes['b'].value))            
                    rgbCode.append(rcode)
                    rgbCode.append(gcode)
                    rgbCode.append(bcode)
                    rgbCodes.append(rgbCode)
        if (colormapNameExist == False):
            print ('The color map name does not exist.')
    except:
        print ('The color map file does not exist.')
    return (rgbCodes)

print ("Start!")
colorMapFile = 'C:/RainbowComplete.xml' #color maps
colorMapName = 'RainbowComplete'              #Color map name

rgbCodes = readColorMap(colorMapFile, colorMapName)
data = np.zeros((2041, 10, 3), dtype=np.uint8)

i = 0
for line in rgbCodes:    
    color = line[1:]
    #print ('color: ', color)
    #input ('')    
    for j in range (0,10):
       data[i, j] = color
       img = Image.fromarray(data, 'RGB')    
    i += 1

img.save('ColorComplete.png')
img.show()         

print ("The End!")