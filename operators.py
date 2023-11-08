#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ########

import bpy, os, re, unicodedata, random, requests, shutil, sys

# Useful for future packages releases
# parent_dir = os.path.abspath(os.path.dirname(__file__))
# packages_dir = os.path.join(parent_dir, 'packages')
# sys.path.append(packages_dir)

from . import functions
from mathutils import Vector


class MCN_OT_about(bpy.types.Operator):
    bl_idname = "mcn.about"
    bl_label = "About"
    bl_description = "About Page"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self, width=600)

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'EXEC_DEFAULT'

        split = layout.split(factor=0.65)

        col = split.column(align=True)
        col.scale_y = 1
        col.label(text="MCN Tools", translate=False)
        col.separator(factor=2.5)
        col.label(text="Made with love, from: Bastien Pimentel")

        col = split.column(align=True)
        col.emboss = 'PULLDOWN_MENU'
        col.operator("wm.url_open", text="UPVDrive", icon='URL').url = "https://upvdrive.univ-montp3.fr/login"
        col.operator("wm.url_open", text="ENT",
                     icon='URL').url = ("https://cas.univ-montp3.fr/cas/login?service=https://monupv.univ-montp3.fr"
                                        "/uPortal/Login")
        col.operator("wm.url_open", text="Info Master ",
                     icon='URL').url = ("http://cinema.univ-montp3.fr/master-1-et-2-creation-numerique-images-animees"
                                        "-et-dispositifs-interactifs/")
        col.operator("wm.url_open", text="Pussy Records ", icon='URL').url = "https://soundcloud.com/pussyrecords-666"
        col.label(text="Don't forget about Discord too !")


class MCN_OT_data_rename(bpy.types.Operator):
    bl_idname = "mcn.data_rename"
    bl_label = "Rename"
    bl_description = "Rename object in scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        assets = bpy.data.objects
        nb_objects = 0

        for obj in assets:
            if obj.type != 'EMPTY':
                if obj.data.name != obj.name:
                    obj.data.name = obj.name
                    nb_objects += 1

        self.report({"INFO"}, "Renamed %d objects" % nb_objects)
        return {"FINISHED"}


class MCN_OT_name_checker(bpy.types.Operator):
    bl_idname = "mcn.name_checker"
    bl_label = "Check Object(s) Name"
    bl_description = "Check object(s) name for special characters"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        nb_objects = 0
        assets = bpy.data.objects

        for obj in assets:
            print('Old name: ', obj.name)
            old_name = obj.name
            new_name = unicodedata.normalize('NFKD', old_name).encode('ASCII', 'ignore').decode('utf-8', 'ignore')
            new_name = re.sub('[^a-zA-Z0-9\n\.\_]', '', new_name)
            obj.name = new_name
            print('New name: ', obj.name)
            nb_objects += 1

        self.report({"INFO"}, "Checked name of %d object(s), please beware of your formatting too" % nb_objects)
        return {"FINISHED"}


class MCN_OT_model_checker(bpy.types.Operator):
    bl_idname = "mcn.model_checker"
    bl_label = "Check Model"
    bl_description = "Sanity check for self-grading models"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'WARNING'}, "Not yet implemented, sorry :(")
        return {"FINISHED"}


class MCN_OT_hierarchy_maker(bpy.types.Operator):
    bl_idname = "mcn.hierarchy_maker"
    bl_label = "Make Hierarchy"
    bl_description = "Make common hierarchy for files"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        folders = functions.get_folders()

        if bpy.data.filepath == '':
            self.report({"ERROR"}, "Couldn't create folders, you should save the scene first!")
            return {"CANCELLED"}

        else:
            os.chdir(bpy.path.abspath("//"))
            for folder in folders:
                os.mkdir(folder)

            self.report({"INFO"}, "Successfully made hierarchy")
            return {"FINISHED"}


class MCN_OT_select_by_faces(bpy.types.Operator):
    bl_idname = "mcn.select_by_faces"
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


class MCN_OT_reset_position(bpy.types.Operator):
    bl_idname = "mcn.reset_position"
    bl_label = "Move object"
    bl_description = "Reset position to world center of active object"

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


class MCN_OT_add_subdivision(bpy.types.Operator):
    bl_idname = "mcn.add_subdivision"
    bl_label = "Add Subdivision"
    bl_description = "Add Subdivision modifier of level"

    @classmethod
    def poll(cls, context):
        if 'Subdivision' not in context.active_object.modifiers:
            return True

    def execute(self, context):
        active_obj = bpy.context.active_object
        if active_obj.type == 'MESH' and 'Subdivision' not in active_obj.modifiers:
            bpy.ops.object.modifier_add(type='SUBSURF')
            active_obj.modifiers["Subdivision"].levels = 2
            bpy.ops.object.shade_smooth()
            self.report({'INFO'}, "Successfully added Subdivision modifier")
            return {'FINISHED'}
        else:
            self.report({'ERROR'},
                        f"Couldn't add Subdivision ! Object is of type {active_obj.type}, check for subdivision")
            return {'CANCELLED'}


class MCN_OT_remove_subdivisions(bpy.types.Operator):
    bl_idname = "mcn.remove_subdivision"
    bl_label = "Remove Subdivision"
    bl_description = "Remove Subdivision modifiers"

    @classmethod
    def poll(cls, context):
        if 'Subdivision' in context.active_object.modifiers:
            return True

    def execute(self, context):
        active_obj = bpy.context.active_object
        for modifier in active_obj.modifiers:
            if modifier.type == 'SUBSURF':
                bpy.ops.object.modifier_remove(modifier=modifier.name)
                bpy.ops.object.shade_flat()
        self.report({'INFO'}, "Successfully removed Subdivision modifier(s)")
        return {'FINISHED'}


class MCN_OT_optimize_rendering(bpy.types.Operator):
    bl_idname = "mcn.optimize_rendering"
    bl_label = "Optimize Rendering"
    bl_description = "Optimize Rendering Settings for Cycles Engine"

    @classmethod
    def poll(cls, context):
        if bpy.context.scene.render.engine != 'CYCLES':
            return False
        else:
            return True

    def execute(self, context):
        cycles_settings, render_settings, world_settings = functions.get_optimized_settings()

        cycles = bpy.context.scene.cycles
        render = bpy.context.scene.render
        world = bpy.context.scene.world.cycles
        skipped_attr = []

        for setting in cycles_settings:
            if getattr(cycles, setting, None) != cycles_settings.get(setting):
                setattr(cycles, setting, cycles_settings.get(setting))
            else:
                skipped_attr.append(f'Cycles Setting: {setting}')

        for setting in render_settings:
            if getattr(render, setting, None) != render_settings.get(setting):
                setattr(render, setting, render_settings.get(setting))
            else:
                skipped_attr.append(f'Render Setting: {setting}')

        for setting in world_settings:
            if getattr(world, setting, None) != world_settings.get(setting):
                setattr(world, setting, world_settings.get(setting))
            else:
                skipped_attr.append(f'World Setting: {setting}')

        if len(skipped_attr) == (len(cycles_settings) + len(render_settings) + len(world_settings)):
            self.report({'INFO'}, 'All settings are already optimized !')
            return {'FINISHED'}
        elif len(skipped_attr) > 0:
            self.report({'WARNING'}, f'Found {len(skipped_attr)} settings matching, these were skipped: {skipped_attr}')
            return {'FINISHED'}
        else:
            self.report({'INFO'}, 'Successfully optimized rendering settings !')
            return {'FINISHED'}


class MCN_OT_open_folder(bpy.types.Operator):
    bl_idname = "mcn.open_folder"
    bl_label = "Open Working Folder"
    bl_description = "Open working folder in filepath"

    @classmethod
    def poll(cls, context):
        return not bpy.path.abspath("//") == ''

    def execute(self, context):
        filepath = bpy.path.abspath("//")
        if bpy.path.abspath("//") == '':
            self.report({'ERROR'}, "Couldn't open working directory, have you saved the scene?")
            return {'CANCELLED'}
        else:
            os.startfile(filepath)  # Only Works on Windows
            return {'FINISHED'}


class MCN_OT_make_collections(bpy.types.Operator):
    bl_idname = "mcn.collection_maker"
    bl_label = "Make Collections"
    bl_description = "Make Collections by type of objects"

    def execute(self, context):
        type_list = []
        objects_scene = []

        for obj in bpy.data.objects:
            if obj.type not in type_list:
                type_list.append(obj.type)

        for collection in type_list:
            random_color = random.randint(1, 8)
            if collection not in bpy.data.collections:
                bpy.data.collections.new(collection)
                bpy.data.collections[collection].color_tag = f'COLOR_0{random_color}'
                bpy.context.scene.collection.children.link(bpy.data.collections[collection])
            if 'Collection' in bpy.data.collections:
                bpy.data.collections.remove(bpy.data.collections['Collection'])

        for obj in bpy.data.objects:
            for collection in obj.users_collection:
                collection.objects.unlink(obj)
            if obj.type in bpy.data.collections:
                bpy.data.collections[obj.type].objects.link(obj)

        return {'FINISHED'}


class MCN_OT_random_fact(bpy.types.Operator):
    bl_idname = "mcn.random_fact"
    bl_label = "Get a random fact"
    bl_description = "Get a true useless fact from around the world !"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        response = requests.get(context.scene.mcn.fact_url)
        if response.status_code == 200:
            response_json = response.json()
            text_to_show = response_json['text']

            context.scene.mcn.random_fact = text_to_show
            self.report({'INFO'}, f'Useless fact: {text_to_show}')
        else:
            self.report({'ERROR'}, f'URL returned following code: {response.status_code}')
        return {'FINISHED'}


class MCN_OT_link_turnaround(bpy.types.Operator):
    bl_idname = "mcn.link_turnaround"
    bl_label = "Link scene to default turnaround"
    bl_description = "Link current scene objects to turnaround scene for rendering purposes"

    @classmethod
    def poll(cls, context):
        return not bpy.path.abspath("//") == '' and not 'turnaround' in bpy.data.filepath

    def execute(self, context):
        filepaths = functions.get_turnaround_filepaths()

        if not os.path.isdir(filepaths.get('turnaround_directory')):
            shutil.copytree(filepaths.get('content_path'), filepaths.get('turnaround_directory'))

        if not context.scene.mcn.turnaround_linked:
            context.scene.mcn.turnaround_linked = True
            context.scene.mcn.turnaround_linked_filepath = filepaths.get('turnaround_filepath')

        bpy.ops.wm.save_mainfile()
        bpy.ops.wm.open_mainfile(filepath=filepaths.get('turnaround_filepath'))

        linked = False

        for library in bpy.data.libraries:
            if library.filepath == filepaths.get('current_filepath'):
                linked = True

        if not linked:
            collection_name = "LINKED_OBJECTS"
            collection = bpy.data.collections.new(collection_name)
            bpy.context.scene.collection.children.link(collection)

            with bpy.data.libraries.load(filepaths.get('current_filepath'), link=True) as (data_from, data_to):
                data_to.objects = data_from.objects

            for obj in data_to.objects:
                if obj.type == 'MESH':
                    bpy.data.collections[collection_name].objects.link(bpy.data.objects[obj.name])
                else:
                    bpy.ops.object.delete()

        return {'FINISHED'}


class MCN_OT_open_turnaround(bpy.types.Operator):
    bl_idname = "mcn.open_turnaround"
    bl_label = "Open linked turnaround"
    bl_description = "Open linked turnaround blender scene"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.ops.wm.save_mainfile()
        bpy.ops.wm.open_mainfile(filepath=context.scene.mcn.turnaround_linked_filepath)
        return {'FINISHED'}


class MCN_OT_open_linked_object(bpy.types.Operator):
    bl_idname = "mcn.open_linked_object"
    bl_label = "Open Linked Object"
    bl_description = "Open Linked Object"

    @classmethod
    def poll(cls, context):
        return context.active_object.library is not None

    def execute(self, context):
        bpy.ops.wm.save_mainfile()
        bpy.ops.wm.open_mainfile(filepath=context.active_object.library.filepath)
        return {'FINISHED'}


class MCN_OT_reset_turnaround(bpy.types.Operator):
    bl_idname = "mcn.reset_turnaround"
    bl_label = "Reset Turnaround Link"
    bl_description = "Reset Turnaround's link and enable re-link"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        context.scene.mcn.turnaround_linked = False
        context.scene.mcn.turnaround_linked_filepath = ''
        return {'FINISHED'}


class MCN_OT_move_pivot(bpy.types.Operator):
    bl_idname = "mcn.move_pivot"
    bl_label = "Move Pivot Point"
    bl_description = "Move Pivot Point to selected vertex"

    @classmethod
    def poll(cls, context):
        return bpy.context.object.mode == 'EDIT'

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
        bpy.ops.view3D.snap_cursor_to_center()
        bpy.ops.object.mode_set(mode='EDIT')
        self.report({'INFO'}, "Successfully moved Pivot Point to selected vertex")
        return {'FINISHED'}


class MCN_OT_commandline_render(bpy.types.Operator):
    bl_idname = "mcn.commandline_render"
    bl_label = "Silent rendering in CMD"
    bl_description = "Generate commandline for silent rendering"

    directory: bpy.props.StringProperty(
        name="Outdir Path",
        description="Rendering directory"
        )

    filter_folder: bpy.props.BoolProperty(
        default=True,
        options={"HIDDEN"}
        )

    @classmethod
    def poll(cls, context):
        return not bpy.path.abspath("//") == ''

    def execute(self, context):
        blender_exec = functions.get_blender_path()
        self.report({'WARNING'}, self.directory)
        self.report({'WARNING'}, blender_exec)
        filepath = bpy.data.filepath.replace('\\\\', '\\')
        bpy.ops.wm.save_mainfile()
        bpy.ops.wm.quit_blender()
        command = f'start cmd /k \"\"{blender_exec}\" -b \"{filepath}\" -o \"{self.directory}/frame_#####\"\" -a'
        os.system(command)
        print(command)
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
