import os
import sys
import argparse
import Image

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", default=os.getcwd(), help="folder path containing images to convert",)
args = parser.parse_args()
if args.folder:
    if os.path.isdir(args.folder):
        images_path = args.folder
    else:
        sys.exit("Error: Invalid folder path")

images = 0
converted = 0
for root, dirs, files in os.walk(images_path, topdown=False):
    for name in files:
        print(os.path.join(root, name))
        if os.path.splitext(os.path.join(root, name))[1].lower() == ".tif" or ".tiff":
            images += 1
            if os.path.isfile(os.path.splitext(os.path.join(root, name))[0] + ".jpg"):
                print "A jpeg file already exists for %s" % name
            else:
                outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
                try:
                    im=Image.open(os.path.join(root, name))
                    im.save(outfile, "JPEG", quality=95)
                    converted += 1
                except Exception, e:
                    print e
print(repr(converted) + " images converted on a total of " + repr(images))