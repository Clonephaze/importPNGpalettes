bl_info = {
    "name": "Import PNG Palette",
    "blender": (4, 0, 0),
    "category": "Image",
    "author": "Ruuubick",
    "description": "Import PNG images as color palettes",
}

import bpy
from bpy.types import Operator
from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy_extras.io_utils import ImportHelper
import math
import os


def rgb_dist(c1, c2):
    return math.sqrt(sum((a - b)**2 for a, b in zip(c1, c2)))


class IMPORT_OT_png_palette(Operator, ImportHelper):
    """Import PNG as Color Palette"""
    bl_idname = "import_image.png_palette"
    bl_label = "Import PNG as Palette"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ".png"
    filter_glob: StringProperty(default="*.png", options={'HIDDEN'})
    color_limit: IntProperty(name="Max Colors", default=256, min=1, max=4096)
    deduplicate: BoolProperty(name="Merge Similar Colors", default=True)
    tolerance: IntProperty(name="Color Similarity Tolerance", default=5, min=1, max=50)
    ignore_alpha: BoolProperty(name="Ignore Transparent Pixels", default=True)

    def execute(self, context):
        path = self.filepath
        name = os.path.splitext(os.path.basename(path))[0]

        try:
            img = bpy.data.images.load(path)
        except Exception as e:
            self.report({'ERROR'}, f"Could not load image: {e}")
            return {'CANCELLED'}

        w, h = img.size
        pixels = list(img.pixels)

        colors = []
        for i in range(0, len(pixels), 4):
            r, g, b, a = pixels[i:i+4]
            if self.ignore_alpha and a < 0.5:
                continue
            color = (r, g, b)
            if self.deduplicate:
                if not any(rgb_dist(color, c) < (self.tolerance / 255) for c in colors):
                    colors.append(color)
            else:
                colors.append(color)
            if len(colors) >= self.color_limit:
                break

        if not colors:
            self.report({'WARNING'}, "No valid colors found in image.")
            return {'CANCELLED'}

        pal = bpy.data.palettes.new(name)
        for c in colors:
            col = pal.colors.new()
            col.color = c

        self.report({'INFO'}, f"Created palette '{name}' with {len(colors)} colors.")
        return {'FINISHED'}


def menu_func(self, context):
    self.layout.operator(IMPORT_OT_png_palette.bl_idname, text="Import PNG as Palette")


def register():
    bpy.utils.register_class(IMPORT_OT_png_palette)
    bpy.types.TOPBAR_MT_file_import.append(menu_func)


def unregister():
    bpy.utils.unregister_class(IMPORT_OT_png_palette)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func)


if __name__ == "__main__":
    register()
