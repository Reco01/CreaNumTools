#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy
from bpy.app.translations import pgettext_iface as iface_

class op(bpy.types.Operator):
    bl_idname = "mcn.about"
    bl_label = "About"
    bl_description = "About Page"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print("Test", self)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self, width=500)

    def draw(self, context):

        layout = self.layout

        split = layout.split(factor=0.65)

        col = split.column(align=True)
        col.scale_y = 1
        col.label(text="MCN Tools", translate=False)
        col.separator(factor=2.5)
        col.label(text="Blenderer")
        col.label(text="Made with love, from: Bastien PIMENTEL")

        col = split.column(align=True)
        col.emboss = 'PULLDOWN_MENU'
        col.operator("wm.url_open", text="UPVDrive", icon='URL').url = "https://upvdrive.univ-montp3.fr/login"
        col.operator("wm.url_open", text="ENT", icon='URL').url = "https://cas.univ-montp3.fr/cas/login?service=https://monupv.univ-montp3.fr/uPortal/Login"
        col.operator("wm.url_open", text="Info Master ", icon='URL').url = "http://cinema.univ-montp3.fr/master-1-et-2-creation-numerique-images-animees-et-dispositifs-interactifs/"
        col.operator("wm.url_open", text="Pussy Records ", icon='URL').url = "https://soundcloud.com/pussyrecords-666"
        col.label(text="Don't forget about Discord too !")

bpy.utils.register_class(op)  