# plan:
"""
drawing on transparent rect on image
everything else
"""
cal = """
      July 2025
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
"""

# print(cal)

from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("consola.ttf", 20)

wallpaper_src = "wallhaven-rq75r7_1920x1080.png"
wallpaper = Image.open(wallpaper_src)


fl = Image.new("RGBA", wallpaper.size, (0, 0, 0, 0))

ctx = ImageDraw.Draw(fl)


def rect(ctx,x,y,w,h,fill):
    ctx.rectangle([(x,y),(x+w,y+h)], fill = fill, width=0)

rect(ctx, 300, 300, 250, 200, (0,0,0,128))

#ikr, font rendering sucks :{
ctx.fontmode="1"
ctx.text((310, 310), cal, font=font, fill=(255, 255, 255, 128))

out = Image.alpha_composite(wallpaper, fl).convert("RGB")
out.show()