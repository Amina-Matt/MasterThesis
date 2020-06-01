import bpy
import numpy as np
for distance in np.arange(0.1,0.3, 0.1):
    baseWidth=0.2
    distanceString=str(distance)
    x=baseWidth+(distance/2)
    originalFileName="KirBas_LW1.550.073.stl"
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
