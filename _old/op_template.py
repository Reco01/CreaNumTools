#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

# THIS SCRIPT SHOULD ONLY BE COPIED FIRST > your_file.py
# YOU SHOULD DELETE THESE TWO LINES BEFORE SCRIPTING

import bpy

class op(bpy.types.Operator):
    bl_idname = "mcn."
    bl_label = ""
    bl_description = ""
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        pass
        return {'FINISHED'}

bpy.utils.register_class(op)  