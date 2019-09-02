# -*- coding: utf-8 -*-
#!/usr/bin/python

"""
Created on Thu Jun 28 14:46:41 2018

@author: gag

Documento donde se encuentran las funciones para requeridas para la apertura de las imagenes SAR.

"""

import numpy as np
from osgeo import gdal, ogr, gdalconst
import peakutils
from matplotlib import pyplot as plt


#### --------------------------------------------------------------------------------------

def openFileHDF(file, nroBand):
    """
    Función que abre archivo HDF y carga la banda que recibe como trabajo
    Retorna: el objeto fuente, la banda, la georeferenciación y la proyección
    """
    #print "Open File"
    # file = path+nameFile
    #print file
    try:
        src_ds = gdal.Open(file)
    except (RuntimeError, e):
        print('Unable to open File')
        print(e)
        sys.exit(1)

#    cols = src_ds.RasterXSize
#    rows = src_ds.RasterYSize
#    print(cols)
#    print(rows)
    bands = src_ds.RasterCount
#    print(bands)

    # se obtienen las caracteristicas de las imagen HDR
    GeoT = src_ds.GetGeoTransform()
    #print GeoT
    Project = src_ds.GetProjection()

    try:
        srcband = src_ds.GetRasterBand(nroBand)
    except(RuntimeError, e):
        # for example, try GetRasterBand(10)
        print('Band ( %i ) not found' % band_num)
        print(e)
        sys.exit(1)
    band = srcband.ReadAsArray()
#    print(band.shape)
    return src_ds, band, GeoT, Project




#### --------------------------------------------------------------------------------------

