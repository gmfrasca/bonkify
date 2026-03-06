from bonkify.generator import Generator
from bonkify.merger import Merger
from bonkify.animator import Animator
import logging


class Bonkifier(object):

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.generator = Generator()
        self.merger = Merger()
        self.animator = Animator()

    def bonkify(self, source_image, dest_image):
        self.logger.info(f"Generating BonkImage {dest_image} from source: {source_image}")
        self.logger.info("Generating custom bonk frames...")
        frames = self.generator.generate_frames(source_image)
        self.logger.info("Merging bonk frame groups together...")
        merged = [self.merger.merge(x) for x in frames]
        self.logger.info("Layer Merge complete.")
        self.logger.info("Creating Animated Image from merged frame groups...")
        self.animator.animate(merged, dest_image)
        self.logger.info("Successfully generated bonk image.")
