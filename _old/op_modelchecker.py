#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy

class op(bpy.types.Operator):
    bl_idname = "mcn.model_checker"
    bl_label = "Check Model"
    bl_description = "Sanity check for self-grading models"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        pass
        return {"FINISHED"}

bpy.utils.register_class(op)  