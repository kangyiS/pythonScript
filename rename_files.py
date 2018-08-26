import os

file_dir = '/home/kangyi/data/RMinfantry/JPEGImages/'
f = os.listdir(file_dir)

new_name = 13647
n = 0
for i in f:
    oldname = file_dir + str(1 + n) + '.xml'
    newname = file_dir + str(new_name + n) + '.xml'
    os.rename(oldname, newname)
    print(oldname, '======>', newname)
    n += 1
