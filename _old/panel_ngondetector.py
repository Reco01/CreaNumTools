bl_info = {
    "name": "Geo Detector Detector",
    "author": "Damien Picard",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "",
    "description": "Various tools in a custom interface",
    "warning": "WIP",
    "doc_url": "",
    "category": "MCN",
}

import bpy

class MCNTools_OT_select_by_faces(bpy.types.Operator):
    bl_idname = "damien.select_by_faces"
    bl_label = "Select Polygons by Sides"

    do_ngons: bpy.props.BoolProperty()

    def execute(self, context):
        bpy.ops.object.mode_set(mode="OBJECT")
        
        for poly in context.object.data.polygons:
            
            if self.do_ngons and len(poly.vertices) > 4:
                poly.select = True
                bpy.ops.view3d.view_selected(use_all_regions=False)
            elif not self.do_ngons and len(poly.vertices) == 3:
                poly.select = True
                bpy.ops.view3d.view_selected(use_all_regions=False)
            else:
                poly.select = False

        bpy.ops.object.mode_set(mode="EDIT")

        return {'FINISHED'}

class MCNTools_PT_GeoDetector(bpy.types.Panel):
    bl_label = "Geo Detector"
    bl_idname = "mcn.damien_geodetector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "MCN Tools"

    def draw(self, context):
        layout = self.layout

        # For each selected object, display its name and parent
        for obj in context.selected_objects:
            
            box = layout.box()    
            col = box.column()
            
            row = col.row()
            row.prop(obj, "name")
            row.prop(obj, "parent")
            
            if obj.type != 'MESH':
                continue
            
            n_tris = 0
            n_ngons = 0
            n_invalids = 0
            
            for poly in obj.data.polygons:
                if len(poly.vertices) == 4:
                    continue
                elif len(poly.vertices) > 4:
                    n_ngons += 1
                elif len(poly.vertices) == 3:
                    n_tris += 1
                else:
                    n_invalids += 1
            
            if n_tris != 0:
                row = col.row()
                row.label(text="Object has " + str(n_tris) + " triangles")
                row.operator("damien.select_by_faces", text="Select Triangles").do_ngons = False
            
            if n_ngons != 0:
                row = col.row()
                row.label(text=f"Object has {n_ngons} ngons")
                row.operator("damien.select_by_faces", text="Select Ngons").do_ngons = True
                
            if n_invalids != 0:
                row = col.row()
                row.label(text="Object has " + str(n_invalids) + " invalid faces")

        row = layout.row()
        row.operator("mesh.remove_doubles")
