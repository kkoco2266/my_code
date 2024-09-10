from PIL import Image, ImageOps
import os
import sys

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif not os.path.splitext(sys.argv[1])[-1].lower() in ['.jpg', '.jpeg', '.png'] :
    sys.exit('Invalid input')
elif not os.path.splitext(sys.argv[2])[-1].lower() in ['.jpg', '.jpeg', '.png'] :
    sys.exit('Invalid input')
elif os.path.splitext(sys.argv[1])[-1] != os.path.splitext(sys.argv[2])[-1] :
    sys.exit('Input and output have different extensions')

try:
    shirt_pic = Image.open('shirt.png')
    pic = Image.open(f'{sys.argv[1]}')
    size = shirt_pic.size
    sized_pic = ImageOps.fit(pic, size)
    sized_pic.paste(shirt_pic, shirt_pic)
    sized_pic.save(f'{sys.argv[2]}')
except FileNotFoundError:
    sys.exit('Input does not exist')
