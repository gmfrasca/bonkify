from bonkify.bonkifier import Bonkifier
import argparse
import logging


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--debug', action='store_true')
    parser.add_argument('src', type=str)
    parser.add_argument('dest', type=str)
    return parser.parse_args()


def setup_logging(debug):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level)


def main():
    args = parse_args()
    setup_logging(args.debug)
    bonkifier = Bonkifier()
    bonkifier.bonkify(args.src, args.dest)


if __name__ == '__main__':
    main()
