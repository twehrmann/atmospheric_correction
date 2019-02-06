#!/usr/bin/env python    
import os                
import sys               
import gdal              
from glob import glob    
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer() 
from datetime import datetime, timedelta
para_names = 'tcwv,gtco3,aod550,duaod550,omaod550,bcaod550,suaod550'.split(',')
def get_onedate(onedate):
    this_date = onedate.strftime('%Y-%m-%d')
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
            "grid": "0.125/0.125",
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

if __name__ == '__main__':
    dates = datetime(2015,5,12), datetime(2015,5,28), datetime(2015,6,29), datetime(2015,7,15)
    from multiprocessing import Pool
    p = Pool(4)
    p.map(get_onedate, dates)
    #get_onedate(onedate)
    p.join()
    p.close()
