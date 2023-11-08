#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

#
#
# This addon has tools to ease your journey into the 3D Realm, brace yourselves, you're gonna need it :)
#
# 

bl_info = {
    "name": "MCN Tools",
    "author": "GODBLESS",
    "version": (1, 0, 0),
    "blender": (3, 6, 2),
    "location": "Topbar",
    "description": "Collection of tools useful for MCN",
    "warning": "WIP",
    "doc_url": "",
    "category": "MCN",
}

import bpy, addon_utils, os, re
from bpy.types import Header, Menu, Panel
from bpy.utils import register_class, unregister_class

from . import operators, panel, properties


class TOPBAR_MT_tools_menu(Menu):
    bl_idname = "TOPBAR_MT_tools_menu"
    bl_label = "MCN Tools c[_]"
    bl_description = "MCN Tools Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_DEFAULT'

        layout.label(text=f"{re.sub(r'[()]', '', str(bl_info.get('version'))).replace(',', '.')} | {os.getlogin()}")
        layout.separator()
        layout.menu("TOPBAR_MT_scene", icon='MODIFIER_DATA')
        layout.separator()
        layout.menu("TOPBAR_MT_misc", icon='COLLAPSEMENU')
        layout.separator()
        layout.operator("mcn.about", text='About')


class TOPBAR_MT_scene(Menu):
    bl_label = "Scene Tools"
    bl_description = "Scene Tools"

    def draw(self, context):
        layout = self.layout

        layout.operator("mcn.model_checker", text="Check Model", icon='MODIFIER_DATA')
        layout.separator()
        layout.operator("mcn.data_rename", text="Data Rename", icon='OBJECT_DATAMODE')
        layout.separator()
        layout.operator("mcn.name_checker", text="Check Object(s) Name", icon='SMALL_CAPS')
        layout.separator()
        layout.operator("mcn.collection_maker", text="Make Collections", icon='COLLECTION_NEW')

class TOPBAR_MT_misc(Menu):
    bl_label = "Misc."
    bl_description = "More tools"

    def draw(self, context):
        layout = self.layout

        layout.operator("mcn.hierarchy_maker", text="Make Hierarchy", icon='NEWFOLDER')
        layout.separator()
        layout.operator("wm.url_open", text="Cheat Sheet", icon='TEXT').url = (
            "https://markoze.com/wp-content/uploads/2022/10/blender33-infographic-SM-2500.png"
        )


classes = (
    TOPBAR_MT_tools_menu,
    TOPBAR_MT_scene,
    TOPBAR_MT_misc,
    properties.MCN_PG_properties,
    panel.MCN_PT_main,
    panel.MCN_PT_modeling,
    panel.MCN_PT_file_operations,
    panel.MCN_PT_rendering,
    panel.MCN_PT_optimizer,
    panel.MCN_PT_renderer,
    panel.MCN_PT_turnaround,
    panel.MCN_PT_random,
    operators.MCN_OT_about,
    operators.MCN_OT_data_rename,
    operators.MCN_OT_name_checker,
    operators.MCN_OT_model_checker,
    operators.MCN_OT_hierarchy_maker,
    operators.MCN_OT_select_by_faces,
    operators.MCN_OT_reset_position,
    operators.MCN_OT_add_subdivision,
    operators.MCN_OT_remove_subdivisions,
    operators.MCN_OT_optimize_rendering,
    operators.MCN_OT_open_folder,
    operators.MCN_OT_make_collections,
    operators.MCN_OT_random_fact,
    operators.MCN_OT_link_turnaround,
    operators.MCN_OT_open_turnaround,
    operators.MCN_OT_open_linked_object,
    operators.MCN_OT_reset_turnaround,
    operators.MCN_OT_move_pivot,
    operators.MCN_OT_commandline_render
)


def draw_item(self, context):
    layout = self.layout
    layout.menu(TOPBAR_MT_tools_menu.bl_idname)


def register():
    for cls in classes:
        register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(draw_item)
    bpy.types.Scene.mcn = bpy.props.PointerProperty(type=properties.MCN_PG_properties)


def unregister():
    for cls in classes:
        unregister_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_item)
    del bpy.types.Scene.mcn


if __name__ == "__main__":  # only for live edit.
    register()
