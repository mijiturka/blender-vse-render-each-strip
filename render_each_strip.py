import bpy

description = 'Render each strip to a separate file'

bl_info = {
    "name": 'You gotta be joking',
    "blender": (2, 93, 0),
    "category": "Sequencer",
}

addon_keymaps = []

class RenderEachStrip(bpy.types.Operator):
    '''You gotta be joking'''
    bl_idname = 'sequencer.render_each_strip'
    bl_label = 'You gotta be joking'
    bl_options = {'REGISTER'}

    def execute(self, context):
        print('Executing RenderEachStrip')
        sequences = context.sequences
        print(len(sequences))

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RenderEachStrip.bl_idname)

def add_shorcut():
    window_manager = bpy.context.window_manager
    if window_manager.keyconfigs.addon:
        keymap = window_manager.keyconfigs.addon.keymaps.new(
            name='Idk',
            space_type='SEQUENCE_EDITOR'
        )
        # Set shortcut for executing this to Alt+Shift+E
        keymap_items = keymap.keymap_items.new(
            idname=RenderEachStrip.bl_idname,
            value='NOTHING',
            alt=True, shift=True,
            type='E',
        )
        addon_keymaps.append((keymap, keymap_items))

def remove_shortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

def register():
    bpy.utils.register_class(RenderEachStrip)

    bpy.types.SEQUENCER_MT_context_menu.append(menu_func)

    add_shorcut()

    print("Registered RenderEachStrip")

def unregister():
    remove_shortcut()

    bpy.types.SEQUENCER_MT_context_menu.remove(menu_func)

    bpy.utils.unregister_class(RenderEachStrip)

    print("Unregistered RenderEachStrip")

if __name__ == '__main__':
    register()
