import logging


FRAME_DELAY = 60
DISPOSAL = 2


class Animator(object):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def animate(self, frames_list, dest_image, duration=FRAME_DELAY, loop=0):
        self.logger.info(f"Writing new animated image to {dest_image}")
        self.logger.debug(f"Frame Delay: {duration}")
        self.logger.debug(f"Disposal Value: {DISPOSAL}")
        frames_list[0].save(dest_image,
                            save_all=True,
                            append_images=frames_list,
                            optimize=True,
                            duration=duration,
                            loop=loop,
                            disposal=DISPOSAL)
