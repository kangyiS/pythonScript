import xml.etree.ElementTree as ET
import os

xml_dir = '/home/kangyi/data/RMinfantry/Annotations'
for root, dirs, files in os.walk(xml_dir):
    for file in files:
        if os.path.splitext(file)[1] == '.xml':
            updateTree = ET.parse(xml_dir+'/'+str(file))
            root = updateTree.getroot()
            xmin = root.find("object/bndbox/xmin")
            if int(xmin.text) <= 0:
                xmin.text = '1'
            ymin = root.find("object/bndbox/ymin")
            if int(ymin.text) <= 0:
                ymin.text = '1'
            xmax = root.find("object/bndbox/xmax")
            if int(xmax.text) >= 640:
                xmax.text = '639'
            ymax = root.find("object/bndbox/ymax")
            if int(ymax.text) >= 480:
                ymax.text = '479'
            #xmin.text = '0'
            updateTree.write(xml_dir+'/'+str(file))
