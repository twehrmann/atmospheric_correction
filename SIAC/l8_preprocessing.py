#/usr/bin/env python
import os
from glob import glob
from SIAC.l8_angle import do_l8_angle

def l8_pre_processing(l8_dir):
    metafiles = []
    for (dirpath, dirnames, filenames)  in os.walk(l8_dir):
        if len(filenames)>0:
            temp = [dirpath + '/' + i for i in filenames]
            for j in temp:
<<<<<<< HEAD
                if 'mtl.' in j.lower():
                    metafiles.append(os.path.realpath(j))
=======
                if 'mtl.txt' in j.lower():
                    metafiles.append(j)
>>>>>>> 04896ed8853e9d859245fd38a14cbfc4c4aebae2
    l8_tiles = []
    for metafile in metafiles:
        ret = do_l8_angle(metafile)
        l8_tiles.append(ret)
    return l8_tiles
