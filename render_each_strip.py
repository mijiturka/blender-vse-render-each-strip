import bpy

description = 'Render each strip to a separate file'

bl_info = {
    "name": description,
    "blender": (2, 93, 0),
    "category": "Sequencer",
}

class RenderEachStrip(bpy.types.Operator):
    f'''{description}'''
    bl_idname = 'sequencer.render_each_strip'
    bl_label = description
    bl_options = {'REGISTER'}

    def execute(self, context):
        return {'FINISHED'}

def register():
    bpy.utils.register_class(RenderEachStrip)
    print("Registered RenderEachStrip")

def unregister():
    bpy.utils.unregister_class(RenderEachStrip)
    print("Unregistered RenderEachStrip")

if __name__ == '__main__':
    register()
