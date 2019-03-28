#!/usr/bin/env python
import os
import sys
import gdal
from glob import glob
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer() 
from datetime import datetime, timedelta

TARGET_DIR = os.environ.get("CAMS_DIR",'/extern/data/cams')

if not os.path.isdir(TARGET_DIR):
    os.mkdir(TARGET_DIR)
os.chdir(TARGET_DIR)

para_names = 'tcwv,gtco3,aod550,duaod550,omaod550,bcaod550,suaod550'.split(',')
starting = datetime(2019,1,20)
end = datetime.now()
days = (end - starting).days
for one_day in range(0,days):
    this_date = (starting + timedelta(days = one_day)).strftime('%Y-%m-%d')
    filename = "%s.nc"%this_date
    if not os.path.exists(filename):
        server.retrieve({
            "class": "mc",
            "dataset": "cams_nrealtime",
            "date": "%s"%this_date,
            "expver": "0001",
            "levtype": "sfc",
            "param": "137.128/206.210/207.210/209.210/210.210/211.210/212.210",
            "step": "0/3/6/9/12/15/18/21/24",
            "stream": "oper",
            "time": "00:00:00",
            "type": "fc",
            "grid": "0.35/0.35",
            "area": "90/-180/-90/180",
            "format":"netcdf",
            "target": "%s.nc"%this_date,
        })
    else:
        pass
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
