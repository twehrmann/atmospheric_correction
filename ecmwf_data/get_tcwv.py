#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
    "class": "mc",
    "dataset": "cams_nrealtime",
    "date": "2016-01-01/to/2016-06-31",
    "expver": "0001",
    "levtype": "sfc",
    "param": "137.128",
    "step": "0/3/6/9/12/15/18/21/24",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    "grid": "0.125/0.125",
    "area": "90/-180/-90/180",
    "format": "netcdf",
    "target": "tcwv.nc",
})
