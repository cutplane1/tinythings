# plan:
"""
drawing on transparent rect on image
everything else
"""


from PIL import Image, ImageDraw

wallpaper_src = "wallhaven-rq75r7_1920x1080.png"
wallpaper = Image.open(wallpaper_src)


rect = Image.new("RGBA", (300,300), (0, 0, 0, 128))

# d = ImageDraw.Draw(rect)
# d.rectangle()

# rect.show()

out = Image.alpha_composite(wallpaper, rect)
# out.show()