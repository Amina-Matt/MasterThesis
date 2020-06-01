import bpy
import numpy as np
import sys

import argparse
# 
if '--' in sys.argv:
    argv = sys.argv[sys.argv.index('--') + 1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('-s1', '--sample_1', dest='sample_1', metavar='FILE')
    args = parser.parse_known_args(argv)[0]
    arrList = list(args.sample_1.split(','))

#this is the list of arrangement given in argument

parameter = "length"
dir = "/Users/aminamatt/Dropbox/Pdm/FarFieldSimulations/Individual-Shapes/"
i = 0



finalFileName = "Random_"+parameter+".stl"
exportPath = dir + finalFileName

#Loop on the individual shapes that forms the complete random arrangement
for length in arrList:
    #import the individual shape
    originalFileName = "KirBas_LW"+length+"0.073.stl"
    importPath = dir+originalFileName
    bpy.ops.import_mesh.stl(filepath=importPath)
    
    bpy.ops.transform.translate(value=(i*1.0,0.0,0.0))
    i = i+1

#Merge the individual shapes
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.join()
#Set the origin at the center of the final structure and the bottom of it
from mathutils import Matrix, Vector


def origin_to_bottom(ob, matrix=Matrix()):
    me = ob.data
    mw = ob.matrix_world
    local_verts = [matrix @ Vector(v[:]) for v in ob.bound_box]
    o = sum(local_verts, Vector()) / 8
    o.z = min(v.z for v in local_verts)
    o = matrix.inverted() @ o
    me.transform(Matrix.Translation(-o))

    mw.translation = mw @ o

for o in bpy.context.scene.objects:
    if o.type == 'MESH':
        origin_to_bottom(o)

final_obj = bpy.context.active_object
final_obj.name = finalFileName
#Export the final structure
bpy.ops.export_mesh.stl(filepath=exportPath)
