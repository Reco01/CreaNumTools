#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy


class MCN_PT_main(bpy.types.Panel):
    bl_label = "MCN Tools"
    bl_idname = "MCN_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"

    def draw(self, context):
        pass


class MCN_PT_modeling(bpy.types.Panel):
    bl_label = "Modeling"
    bl_idname = "MCN_PT_modeling"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_main"

    def draw(self, context):
        layout = self.layout
        selected = bpy.context.active_object

        if selected and selected.type == 'MESH':
            n_tris = 0
            n_ngons = 0
            n_invalids = 0

            if selected:
                for poly in selected.data.polygons:
                    if len(poly.vertices) == 4:
                        continue
                    elif len(poly.vertices) > 4:
                        n_ngons += 1
                    elif len(poly.vertices) == 3:
                        n_tris += 1
                    else:
                        n_invalids += 1

            spl = layout.split(align=True)
            spl.operator("mcn.reset_position", text="Reset Position / Origin / 3D Cursor", icon='RECOVER_LAST')
            spl.operator("mcn.move_pivot", text="Move Pivot Point", icon='CON_PIVOT')
            spl = layout.split(align=True)
            spl.scale_y = 2.0
            spl.operator("mcn.add_subdivision", text="Add Subdivision", icon='ADD')
            spl.operator("mcn.remove_subdivision", text="Remove Subdivision", icon='REMOVE')
            col = layout.column()
            box2 = col.box()
            box2.prop(context.active_object, "name", text="Stats of")
            spl = col.split(align=True)
            box = spl.box()
            box.label(text=f"Vertices: {len(selected.data.vertices)}")
            box = spl.box()
            box.label(text=f"Faces: {len(selected.data.polygons)}")
            box = spl.box()
            box.label(text=f"Polygons: {len(selected.data.edges)}")
            box = spl.box()
            box.label(text=f"N-Gons: {n_ngons}")
            box = spl.box()
            box.label(text=f"Triangles: {n_tris}")

            spl = layout.split(align=True)
            if n_tris != 0:
                spl.operator("mcn.select_by_faces", text="Select Triangle(s)", icon='VIS_SEL_11').do_ngons = False
            if n_ngons != 0:
                spl.operator("mcn.select_by_faces", text="Select N-Gon(s)", icon='VIS_SEL_11').do_ngons = True
            if n_invalids != 0:
                spl.label(text="Object has " + str(n_invalids) + " invalid faces")
        else:
            box = layout.box()
            box.label(text='Please select an object', icon='ERROR')


class MCN_PT_file_operations(bpy.types.Panel):
    bl_label = "File Operations"
    bl_idname = "MCN_PT_file_operations"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_main"

    def draw(self, context):
        layout = self.layout
        layout.operator("mcn.open_folder", text="Open working directory", icon='FILE_FOLDER')


class MCN_PT_rendering(bpy.types.Panel):
    bl_label = "Rendering"
    bl_idname = "MCN_PT_rendering"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_main"

    def draw(self, context):
        pass


class MCN_PT_optimizer(bpy.types.Panel):
    bl_label = "Optimizer"
    bl_idname = "MCN_PT_optimizer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_rendering"

    def draw(self, context):
        layout = self.layout

        layout.prop(bpy.context.scene.render, 'engine', text='Current Engine')
        layout.operator("mcn.optimize_rendering", text="Optimize Rendering Options", icon='ZOOM_IN')


class MCN_PT_renderer(bpy.types.Panel):
    bl_label = "Renderer"
    bl_idname = "MCN_PT_renderer"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_rendering"

    def draw(self, context):
        layout = self.layout
        layout.operator("mcn.commandline_render", text="Silent Animation Render", icon='RENDER_ANIMATION')


class MCN_PT_turnaround(bpy.types.Panel):
    bl_label = "Turnaround"
    bl_idname = "MCN_PT_turnaround"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_rendering"

    def draw(self, context):
        layout = self.layout
        layout.operator("mcn.open_linked_object", text="Open scene of linked object", icon='FILE_FOLDER')
        if not context.scene.mcn.turnaround_linked:
            layout.operator("mcn.link_turnaround", text="Link to turnaround default scene", icon='LINKED')
        else:
            layout.operator("mcn.open_turnaround", text="Open linked turnaround scene", icon='FILE_FOLDER')
            layout.operator("mcn.reset_turnaround", text="Reset turnaround links", icon='UNLINKED')


class MCN_PT_random(bpy.types.Panel):
    bl_label = "Random"
    bl_idname = "MCN_PT_random"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"
    bl_parent_id = "MCN_PT_main"

    def draw(self, context):
        layout = self.layout
        layout.operator("mcn.random_fact", text=context.scene.mcn.random_fact, icon='SOLO_ON')
