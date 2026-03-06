# bonkify
Generates a bonk_XYZ meme gif from a source static image

## Installation
Simply run the following command:

```bash
pipenv install
```

to create a virtual environment with all dependencies installed.

If you do not have pipenv installed, install it via:
```bash
pip install --user pipenv
```

## Usage
To run the script, simply provide an input file and a output destination, and invoke the script,
from the root directory of this repository, via:

```bash
pipenv shell
python -m bonkify src_image dest_image_name [-v]
```

For example, to create a `bar.gif` from a `foo.png` file, you would run:
```bash
python -m bonkify foo.png bar.gif
```

which will generate a `bar.gif` animated gif in this directory.

## Recommendations
bonkify automatically resizes the input image to appropriate dimensions, but to avoid issues
try to use a source image that is approximately a 75px by 75px square, in .gif or .png format (with transparent background)
