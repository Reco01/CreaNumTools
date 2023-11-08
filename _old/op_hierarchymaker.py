#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy, os

class op(bpy.types.Operator):
    bl_idname = "mcn.hierarchy_maker"
    bl_label = "Make Hierarchy"
    bl_description = "Make common hierarchy for files"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        
        folders = (
            "etc",
            "refs",
            "render",
            "blend",
            "textures"
        )

        if bpy.data.filepath == '':
            self.report({"ERROR"}, "Couldn't create folders, you should save the scene first!")
            return {"CANCELLED"}

        else:
            os.chdir(bpy.path.abspath("//"))

            for folder in folders:
                os.mkdir(folder)

            self.report({"INFO"}, "Successfully made hierarchy")       
            return {"FINISHED"}

bpy.utils.register_class(op)