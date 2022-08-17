from PIL import Image
import logging

BACKGROUND = (0, 0, 0, 0)
BONKED_SIZE = (75, 75)


class Generator(object):

    layers = [
        {"base": "assets/0.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/1.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/2.gif", "bonk_position_x": 52, "bonk_position_y": 58},
        {"base": "assets/3.gif", "bonk_position_x": 54, "bonk_position_y": 60},
        {"base": "assets/4.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/5.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/6.gif", "bonk_position_x": 60, "bonk_position_y": 90},
        {"base": "assets/7.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/8.gif", "bonk_position_x": 50, "bonk_position_y": 70},
        {"base": "assets/9.gif", "bonk_position_x": 50, "bonk_position_y": 75},
        {"base": "assets/10.gif", "bonk_position_x": 55, "bonk_position_y": 60},
        {"base": "assets/11.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/12.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/13.gif", "bonk_position_x": 50, "bonk_position_y": 40},
        {"base": "assets/14.gif", "bonk_position_x": 60, "bonk_position_y": 60},
        {"base": "assets/15.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/16.gif", "bonk_position_x": 50, "bonk_position_y": 55},
        {"base": "assets/17.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/18.gif", "bonk_position_x": 45, "bonk_position_y": 65},
        {"base": "assets/19.gif", "bonk_position_x": 55, "bonk_position_y": 95},
        {"base": "assets/20.gif", "bonk_position_x": 50, "bonk_position_y": 50},
        {"base": "assets/21.gif", "bonk_position_x": 55, "bonk_position_y": 95},
        {"base": "assets/22.gif", "bonk_position_x": 55, "bonk_position_y": 45},
        {"base": "assets/23.gif", "bonk_position_x": 60, "bonk_position_y": 60},
        {"base": "assets/24.gif", "bonk_position_x": 63, "bonk_position_y": 79},
    ]

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def generate_frames(self, source_image):
        self.logger.info(f"Sourcing bonked object from {source_image}")
        self.logger.debug(f"Bonked Object Size: {BONKED_SIZE}")
        src = Image.open(source_image).resize(BONKED_SIZE)
        output = []
        for layer in self.layers:
            newspaper_layer = Image.open(layer['base'])
            bonked_layer = Image.new("RGBA", newspaper_layer.size, BACKGROUND)
            bpx = layer['bonk_position_x']
            bpy = layer['bonk_position_y']
            self.logger.debug(f"Bonked object position: ({bpx}, {bpy})")
            bonked_layer.paste(src, (bpx, bpy))
            output.append([bonked_layer, newspaper_layer])

        self.logger.info("Successfully generated frames.")
        return output
