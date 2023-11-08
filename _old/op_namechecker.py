#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy, re, unicodedata

class op(bpy.types.Operator):
    bl_idname = "mcn.namechecker"
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

bpy.utils.register_class(op)  