import sys
import os

# Open source spatial libraries
import shapely
import numpy
from osgeo import gdal
import math
import random

# SpaPy libraries
from SpaPy import SpaBase
from SpaPy import SpaPlot
from SpaPy import SpaVectors
from SpaPy import SpaView
from SpaPy import SpaReferencing
from SpaPy import SpaDensify
from SpaPy import SpaView
from SpaPy import SpaRasters
from SpaPy import SpaTopo
from SpaPy import SpaRasterVectors

# File Paths

CountriesFilePath="SpaPyTests/Data/NaturalEarth/ne_110m_admin_0_countries.shp"

OverlayFile="SpaPyTests/Data/Overlay/Box.shp"

HumbRiverPath="SpaPyTests/Data/HumboldtCounty/hydrography/nhd24kst_l_ca023.shp"

HumbZoningPath="SpaPyTests/Data/HumboldtCounty/Humboldt_Zoning_ClippedToEelRiver2.shp"

Zoning_Bay="SpaPyTests/Data/HumboldtCounty/Zoning_Bay.shp"

OutputFolderPath="SpaPyTests/Temp/"

cur_dir=os.getcwd()
second_dir=os.path.join(cur_dir,'NH3H2O')
date_dir=os.path.join(second_dir,'06-18-2007')
spa_dir=os.path.join(date_dir,'H2O0001.spa')


SpaView.Show('0min-1-97C.spa')