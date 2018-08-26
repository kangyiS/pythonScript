import os

file_dir = '/home/kangyi/data/RMinfantry/JPEGImages/'
JPEG_dir = '/home/kangyi/data/RMinfantry/JPEGImages/'
XML_dir = '/home/kangyi/data/RMinfantry/Annotations/'

start = 15997
stop = 16042
for i in range(start, stop+1):
    if os.path.isfile(file_dir + str(i) + '.jpg'):
        os.remove(file_dir + str(i) + '.jpg')

for root, dirs, files in os.walk(JPEG_dir):
    for file in files:
        file_name = os.path.splitext(file)[0]
        if not os.path.isfile(XML_dir + str(file_name) + '.xml'):
            os.remove(JPEG_dir + str(file_name) + '.jpg')
