# -*- coding: utf-8 -*-
import PIL
from PIL import Image, ImageOps

# Let's set up our command line arguments
import argparse
parser = argparse.ArgumentParser(description="Image flipper")
parser.add_argument('-i', '--image', help='Filename of input image', required=True)
parser.add_argument('-o', '--output', help="Output file", default='output.jpg', required=True)
passedIn = parser.parse_args()

# Output image size
finalSize = 1024, 1024

# Input image resize
size = 512, 512

# Open our passed in image filename
im = Image.open(str(passedIn.image))

# Resize it to the size above, using a resize algorithm called LANCZOS
im = im.resize(size, PIL.Image.LANCZOS)

# Create a new blank RGB image
out = Image.new('RGB', finalSize)

# Paste in the first rescaled image at top left corner (0,0)
out.paste(im, (0,0))

# Paste second image mirror in center
out.paste(ImageOps.mirror(im), (512,0))

# Paste upside down image below first image
# Flip function mirrors vertically
out.paste(ImageOps.flip(im), (0, 512))

# Paste last mirror image below second image
# Flipped horizontally and vertically
out.paste(ImageOps.flip(ImageOps.mirror(im)), (512,512))

# Save the image out
out.save(passedIn.output)
