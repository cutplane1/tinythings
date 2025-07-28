# plan:
"""
drawing on transparent rect on image
everything else
"""


from PIL import Image, ImageDraw

wallpaper_src = "wallhaven-rq75r7_1920x1080.png"
wallpaper = Image.open(wallpaper_src)


fl = Image.new("RGBA", wallpaper.size, (0, 0, 0, 0))

ctx = ImageDraw.Draw(fl)

def rect(ctx,x,y,w,h,fill):
    ctx.rectangle([(x,y),(x+w,y+h)], fill = fill, width=0)

rect(ctx, 300, 300, 300, 200, (0,0,0,128))

out = Image.alpha_composite(wallpaper, fl)

out.show()