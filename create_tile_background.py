from PIL import Image, ImageDraw
r_x = 270
r_y = 680
t_width = 32



r_x = (r_x / t_width) * t_width - (r_x % t_width)
r_y = (r_y / t_width) * t_width - (r_y % t_width)

im = Image.open("absurd32.bmp")
cropped = im.crop((r_x,r_y,r_x+t_width,r_y+t_width))


nimg = Image.new('RGB',(480,360), color = 'white')
r_x = 480-32
r_y = 0

n = 108
while n > 0:
    nimg.paste(cropped,(r_x, r_y))
    r_y = r_y+32
    n = n -1
    if (n%9 == 0):
        r_x = r_x-32
        r_y = 0

nimg.save("background.png")
nimg.show()
        
