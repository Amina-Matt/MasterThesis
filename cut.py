import bpy
import numpy as np
distance=0.2

#for length in (1.5,1.525,1.55,1.575,1.6,1.625,1.65,1.675,1.7,1.725,1.75,1.75,1.8,1.825,1.85,1.9,1.925,1.95,1.975,2.,2.025,2.05,2.075,2.1,2.125,2.150,2.175,2.2,2.25,2.275,2.3,2.325,2.35,2.375,2.4,2.425,2.45
#for length in (2.5,2.525,2.55,2.575,2.6,2.625,2.65,2.675,
#for length in (2.7,2.725,2.75,2.8,2.825,2.85,2.875,2.9,2.925,3.,3.025,3.05,3.075,3.1,3.125,3.15,3.175,3.2,3.225,3.25,3.275,3.3,3.325,3.35,3.375,3.4,3.425,3.45,3.475,3.5,3.525,3.55,3.575,3.6,3.625,3.65,3.675,3.7,3.725,3.75,2.975,3.05):
for length in (2.75,3.5):    
    baseWidth=0.3
    distanceString=str(distance)
    x=baseWidth+(distance/2.0)
    originalFileName="KirigamiBasisLW"+str(length)+"0.073.stl"
    finalFileName="Cut_"+distanceString+"_"+originalFileName
    dir="/Users/aminamatt/Dropbox/Pdm/FarFieldSimulations/Individual-Shapes/"
    importPath=dir+originalFileName
    exportPath=dir+finalFileName


    bpy.ops.import_mesh.stl(filepath=importPath)

    # Get the ribbon object and rename it.
    ribbon = bpy.context.object
    ribbon.name = 'ribbon'
    # 
    # Center the origin
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN')

    # Use the mesh to edit
    bpy.ops.object.convert(target='MESH', keep_original=False)

    #Edit mode
    bpy.ops.object.mode_set(mode='EDIT')

    #Cut the base vertically on both sides
    bpy.ops.mesh.bisect(plane_co=(x, 0.0, 0.0), plane_no=(4.0, 0.0, 0.0),clear_outer=True)
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.bisect(plane_co=(-x, 0.0, 0.0), plane_no=(4.0, 0.0, 0.0),clear_inner=True)

    #Export the final object
    #bpy.ops.object.mode_set(mode='OBJECT')


    bpy.ops.export_mesh.stl(filepath=exportPath)
