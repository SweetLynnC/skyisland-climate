# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# smooth_raster.py
# Created on: 2016-06-05 22:05:39.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
elevnad83 = "elevnad83"
elevnad83__2_ = "C:\\Users\\hmpou\\Documents\\TXDEM051915\\grids\\std_exents\\elevnad83"
FocalSt_elev1 = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_elev1"
Output_raster__2_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca2"
Output_raster__3_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca3"
Output_raster__4_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca4"
Output_raster__5_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca5"
Output_raster__6_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca6"
Output_raster__7_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca7"
Output_raster__8_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca8"
Output_raster__9_ = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\FocalSt_Foca9"
smoothed = "C:\\Users\\hmpou\\Documents\\ArcGIS\\Default.gdb\\smoothed"

# Process: Focal Statistics
arcpy.gp.FocalStatistics_sa(elevnad83__2_, FocalSt_elev1, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (2)
arcpy.gp.FocalStatistics_sa(FocalSt_elev1, Output_raster__2_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (3)
arcpy.gp.FocalStatistics_sa(Output_raster__2_, Output_raster__3_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (4)
arcpy.gp.FocalStatistics_sa(Output_raster__3_, Output_raster__4_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (5)
arcpy.gp.FocalStatistics_sa(Output_raster__4_, Output_raster__5_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (6)
arcpy.gp.FocalStatistics_sa(Output_raster__5_, Output_raster__6_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (7)
arcpy.gp.FocalStatistics_sa(Output_raster__6_, Output_raster__7_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (8)
arcpy.gp.FocalStatistics_sa(Output_raster__7_, Output_raster__8_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (9)
arcpy.gp.FocalStatistics_sa(Output_raster__8_, Output_raster__9_, "Rectangle 3 3 CELL", "MEAN", "DATA")

# Process: Focal Statistics (10)
arcpy.gp.FocalStatistics_sa(Output_raster__9_, smoothed, "Rectangle 3 3 CELL", "MEAN", "DATA")
