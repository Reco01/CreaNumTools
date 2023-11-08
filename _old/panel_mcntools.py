#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

bl_info = {
    "name": "MCN Tools",
    "author": "B.P",
    "version": (1, 0),
    "blender": (3, 2, 0),
    "location": "VIEW 3D > UI > MCN Tools",
    "description": "Tool to move active object",
    "warning": "WIP",
    "doc_url": "",
    "category": "MCN",
}

import bpy
from bpy.props import BoolProperty, EnumProperty
from mathutils import Vector

def check_subdivision(self, context):
    selected = bpy.context.active_object
    scene = context.scene
    subdivision = scene.add_subdivision

    for modifier in selected.modifiers:
        if modifier.type == 'SUBSURF':
            subdivision.subdivision_bool == True


def add_subdivision(self, context):
    selected = bpy.context.active_object
    scene = context.scene
    subdivision = scene.add_subdivision

    if subdivision.subdivision_bool == True and selected.type == 'MESH':
        bpy.ops.object.modifier_add(type='SUBSURF')
        selected.modifiers["Subdivision"].levels = 2
    else:
        for modifier in selected.modifiers:
            if modifier.type == 'SUBSURF':
                    bpy.ops.object.modifier_remove(modifier=modifier.name)


class MCNTools_Properties(bpy.types.PropertyGroup):

    subdivision_bool: BoolProperty(
        name="Add / Remove Subdivision",
        description="Add / Remove Subdivision",
        default = False,
        update = add_subdivision
        )

    empty_option: EnumProperty(
        name="Empty Options",
        description="Options for create empty",
        items=[
            ('PLAIN_AXES', "Plain Axes", ""),
            ('ARROWS', "Arrows", ""),
            ('SINGLE_ARROW', "Single Arrow", "")
        ]
    )

class MCNTools_OT_reset_position(bpy.types.Operator):
    bl_idname = "mcn.reset_position"
    bl_label = "Move object"
    
    def execute(self, context):
        active_obj = bpy.context.active_object
        if active_obj != "" and bpy.context.selected_objects == []:
            self.report({"ERROR"}, "Please select an object first")
            return {'CANCELLED'}
        else:
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
            bpy.ops.view3D.snap_cursor_to_center()
            active_obj.location = Vector((0, 0, 0))
            self.report({"INFO"}, "That was a successful reset !")
            return {'FINISHED'}
            
class MCNTools_PT_MainPanel(bpy.types.Panel):
    bl_label = "MCN Tools"
    bl_idname = "mcn.main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'   
    bl_category = "MCN Tools"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        subdivision = scene.add_subdivision
        empty = scene.add_empty

        check_subdivision(self, context)

        selected = bpy.context.active_object
        state_subdiv = "ON" if subdivision.subdivision_bool else "OFF"

        layout.operator("mcn.reset_position", text = "Reset Position / Origin / 3D Cursor")
        layout.prop(subdivision, "subdivision_bool", toggle = True)
        layout.prop(empty, "empty_options")

        layout.separator()
        layout.label(text="Active object's name: {}".format(selected.name))
        layout.label(text="Subdivision: {}".format(state_subdiv))
