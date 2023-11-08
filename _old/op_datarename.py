#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy

class op(bpy.types.Operator):
    bl_idname = "mcn.datarename"
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

bpy.utils.register_class(op)  