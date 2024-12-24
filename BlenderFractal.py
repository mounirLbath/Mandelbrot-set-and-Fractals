import bpy
from math import *
import time

"""
Blender script to generate Sierpiński 3d fractal
"""

#######Deselect all objects in the scene and select obj#######
def select(objList):
    bpy.ops.object.select_all(action='DESELECT')  # Deselect all
    
    for obj in objList:
        obj.select_set(True) #Select cube
    
    bpy.context.view_layer.objects.active = objList[0]

#######Create cube at position x,y,z and side of length######
def create_cube(x,y,z,s):
    bpy.ops.mesh.primitive_cube_add(location = (x,y,z))
    diff_cube = bpy.context.object
    diff_cube.scale = (s,s,s)
    return diff_cube

####### copies obj and moves it to location ######
def create_copy(obj, location):
    select([obj])
    bpy.ops.object.duplicate(linked=0,mode='TRANSLATION')
    currObj = bpy.context.object
    currObj.location = location
    return bpy.context.object

####### creates fractal using dp #######
def fractal(n, x = 0, y = 0, z= 0):
    res = create_cube(0,0,0,1)

    a = 2/3
    for i in range(n):
        res.scale = (1/3, 1/3, 1/3) # rescal res

        newFractal = [create_copy(res,(a, a, a)),\
        create_copy(res,( 0, +a, +a)),\
        create_copy(res,(-a, +a, +a)),\
        create_copy(res,(+a, +a, -a)),\
        create_copy(res,( 0, +a, -a)),\
        create_copy(res,(-a, +a, -a)),\
        create_copy(res,(+a, +a, 0)),\
        create_copy(res,(-a, +a, 0)),\
        create_copy(res,(+a, -a, +a)),\
        create_copy(res,( 0, -a, +a)),\
        create_copy(res,(-a, -a, +a)),\
        create_copy(res,(+a, -a, -a)),\
        create_copy(res,( 0, -a, -a)),\
        create_copy(res,(-a, -a, -a)),\
        create_copy(res,(+a, -a, 0)),\
        create_copy(res,(-a, -a, 0)),\
        create_copy(res,(+a, 0, +a)),\
        create_copy(res,(-a, 0, +a)),\
        create_copy(res,(+a, 0, -a)),\
        create_copy(res,(-a, 0, -a))]

        # delete res
        select([res])
        bpy.ops.object.delete()

        select(newFractal)
        bpy.ops.object.join()
        res = bpy.context.object
        bpy.ops.object.transform_apply(scale=True)
    
    res.location = (x,y,z)

fractal(4,0,0,1)
