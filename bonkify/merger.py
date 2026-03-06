import logging


class Merger(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def merge(self, layers_list):
        self.logger.debug(f"Number of layers to merge: {len(layers_list)}")
        if len(layers_list) > 0:
            background = layers_list[0]
            for foreground in layers_list[1:]:
                background.paste(foreground, (0, 0), foreground.convert("RGBA"))
        return background
