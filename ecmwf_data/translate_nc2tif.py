#!/usr/bin/env python
import os
import sys
import gdal
from glob import glob
para_names = 'tcwv,gtco3,aod550,duaod550,omaod550,bcaod550,suaod550'.split(',')
if sys.argv[1] == '-h':
   print('Avaliable parameters: ' + ' '.join(para_names))
else:
    filename = sys.argv[1]
    header = '_'.join(filename.split('.')[0].split('-'))
    if not os.path.exists(header):
        os.mkdir(header)
    exists = glob(header+'/*.tif')
    if len(sys.argv[2:])>0:
        list_para = sys.argv[2:]
    else:
        list_para = para_names
    temp = 'NETCDF:"%s":%s'
    for i in list_para:
        if header + '/'+header+'_'+i+'.tif' not in exists:
            t = 'Translating %-31s to %-23s'%(temp%(filename,i), header+'_'+i+'.tif')
            print(t)
            gdal.Translate(header + '/'+header+'_'+i+'.tif', temp%(filename,i), outputSRS='EPSG:4326', creationOptions=["TILED=YES", "COMPRESS=DEFLATE"])

