from PIL import Image, ImageDraw
import numpy as np

class Renderer:
    def __init__(self, writer):
        self.writer = writer
        self.color_mode = "RGB"

    def setup(self, width, height, background_color):
        self.image = Image.new(self.color_mode, (width, height), (background_color[0], background_color[1], background_color[2]))
        self.draw = ImageDraw.Draw(self.image)

    def render_disk(self, disk):
        ellipse_center = np.array([disk.position[0], disk.position[1]])
        ellipse_center_with_offset = ellipse_center + self.offset_screen_origin_at_center()
        translation = np.array([disk.radius, disk.radius])
        ellipse_lower_left = ellipse_center_with_offset - translation
        ellipse_upper_right = ellipse_center_with_offset + translation
        self.draw.ellipse(
            [(ellipse_lower_left[0], ellipse_lower_left[1]), (ellipse_upper_right[0], ellipse_upper_right[1])], 
            fill=(disk.color[0], disk.color[1], disk.color[2]), 
            outline=(0, 0, 0)
            )

    def offset_screen_origin_at_center(self):
        return np.array([self.half_width_image(), self.half_height_image()])

    def half_width_image(self):
        return self.image.width * 0.5

    def half_height_image(self):
        return self.image.height * 0.5

    def done(self):
        self.writer.write(self.image)