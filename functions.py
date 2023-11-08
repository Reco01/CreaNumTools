#         :::   :::    ::::::::  ::::    :::           ::::::::   ::::::::               ::::::::   :::::::: 
#       :+:+: :+:+:  :+:    :+: :+:+:   :+:          :+:    :+: :+:    :+:             :+:    :+: :+:    :+: 
#     +:+ +:+:+ +:+ +:+        :+:+:+  +:+                +:+        +:+                    +:+         +:+  
#    +#+  +:+  +#+ +#+        +#+ +:+ +#+              +#+        +#+   +#++:++#++:++    +#+        +#++:    
#   +#+       +#+ +#+        +#+  +#+#+#            +#+        +#+                    +#+             +#+    
#  #+#       #+# #+#    #+# #+#   #+#+#           #+#        #+#                    #+#       #+#    #+#     
# ###       ###  ########  ###    ####          ########## ##########             ##########  ########

import bpy, os, sys

from pathlib import Path


def get_blender_path():
    """
    Get blender's executable path
    :return: string     | executable path
    """

    sys_path = sys.executable
    bin_path = os.path.abspath(sys_path + '/../../../..')
    blender_path = bin_path + '\\blender.exe'
    blender_path = blender_path.replace('\\\\', '\\')
    return blender_path


def get_optimized_settings():
    """
    Get optimized settings for optimizer
    :return: dict       | dictionaries of settings
    """

    cycles_settings = {
        'device': 'GPU',
        'samples': 256,
        'max_bounces': 2,
        'transmission_bounces': 2,
        'use_adaptive_sampling': True,
        'adaptive_threshold': 0.5,
        'use_fast_gi': True,
        'debug_use_spatial_splits': True,
        'debug_use_compact_bvh': False
    }

    render_settings = {
        'use_persistent_data': True
    }

    world_settings = {
        'sampling_method': 'MANUAL',
        'sample_map_resolution': 512
    }

    return cycles_settings, render_settings, world_settings


def get_folders():
    """
    Get folder names
    :return: tuple      | names of directories
    """

    folders = (
        "etc",
        "refs",
        "render",
        "blend",
        "textures"
    )

    return folders


def get_turnaround_filepaths():
    """
    Get various filepaths for turnaround
    :return: dict       | dictionary of filepaths
    """

    content_path = f"{Path(__file__).parent.absolute()}\\default_scenes\\turnaround"
    current_filepath = bpy.data.filepath
    parent_folder_filepath = os.path.dirname(current_filepath)
    turnaround_directory = f"{parent_folder_filepath}\\turnaround"
    turnaround_filepath = f"{turnaround_directory}\\blend\\turnaround.blend"

    filepaths = {
        'content_path': content_path,
        'current_filepath': current_filepath,
        'parent_folder_filepath': parent_folder_filepath,
        'turnaround_directory': turnaround_directory,
        'turnaround_filepath': turnaround_filepath
    }

    return filepaths
