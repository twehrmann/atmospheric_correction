#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer() 
from datetime import datetime, timedelta
'''
server.retrieve({
    "class": "mc",
    "dataset": "cams_nrealtime",
    "date": "2016-01-01/to/2016-06-31",
    "expver": "0001",
    "levtype": "sfc",
    "param": "207.210",
    "step": "0/3/6/9/12/15/18/21/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "grid": "0.125/0.125",
    "area": "90/-180/-90/180",
    "format":'netcdf',
    "target": "aod550.nc",
})'''
starting = datetime(2016,1,6)
for one_day in range(180,366):
    this_date = (starting + timedelta(days = one_day)).strftime('%Y-%m-%d')
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
