from PIL import Image, ImageDraw
import sys

if len(sys.argv) != 4:
    print("Wrong number of parameters - expected X Y filename")
    sys.exit()
    

r_x = int(sys.argv[1])
r_y = int(sys.argv[2])
t_width = 32


r_x = (r_x / t_width) * t_width - (r_x % t_width)
r_y = (r_y / t_width) * t_width - (r_y % t_width)

im = Image.open("absurd32.bmp")
cropped = im.crop((r_x,r_y,r_x+t_width,r_y+t_width))
cropped.save(sys.argv[3])
cropped.show()
