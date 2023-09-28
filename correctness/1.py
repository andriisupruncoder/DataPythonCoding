import bpy

# Get the active scene
scene = bpy.context.scene

# Get all objects in the scene
objects = scene.objects

# Print the names of all objects
for object in objects:
    print(object.name)