#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ######## 

import bpy


class MCN_PG_properties(bpy.types.PropertyGroup):
    random_fact: bpy.props.StringProperty(
        name='Useless Fact',
        default='Get a random fact !',
        description='Useless fact, just for fun'
    )

    fact_url: bpy.props.StringProperty(
        name='URL for useless fact',
        default='https://uselessfacts.jsph.pl/api/v2/facts/random',
        description='URL for useless fact'
    )

    turnaround_linked: bpy.props.BoolProperty(
        name='Is already linked',
        default=False,
        description='Bool for linked object'
    )

    turnaround_linked_filepath: bpy.props.StringProperty(
        name='Linked turnaround filepath',
        default='',
        description='Filepath for linked turnaround of current file'
    )
