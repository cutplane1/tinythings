from PIL import Image, ImageDraw, ImageFont

"""
 _____  ___  ___  ___   
/__   \/___\/   \/___\_ 
  / /\//  // /\ //  /(_)
 / / / \_// /_// \_// _ 
 \/  \___/___,'\___/ (_)

* automatic text measure
* nice font rendering
* setting os wallpaper
* image resizing
* nicer api
* rewriting to something portable (like C)
* tty formating
* something else
"""

class Wallpaint:
    def __init__(self, image, font):
        self.wp = image
        self.font = font
        self.fl = Image.new("RGBA", image.size, (0, 0, 0, 0))
        self.ctx = ImageDraw.Draw(self.fl)
    
    def rect(self,x,y,w,h,fill):
        self.ctx.rectangle([(x,y),(x+w,y+h)], fill = fill, width=0)
    
    def out(self):
        o = Image.alpha_composite(self.wp, self.fl).convert("RGB")
        return o

def CalendarWidget(wp, x, y):
    # temp :)
    cal = """
      July 2025
Su Mo Tu We Th Fr Sa
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
"""

    wp.rect(x, y, 250, 200, (0,0,0,128))
    #ikr, font rendering sucks :{
    wp.ctx.fontmode="1"
    wp.ctx.text((x + 10, y + 10), cal, font=wp.font, fill=(255, 255, 255, 128))

def NoteWidget(wp, x, y, notes):
    wp.rect(x, y, 250, 200, (0,0,0,128))
    wp.ctx.fontmode="1"
    for i, note in enumerate(notes):
        wp.ctx.text((x + 10 , y + 10 + (i*20)), "* " + note, font=wp.font, fill=(255, 255, 255, 128))

def WeatherWidget(wp,x,y):
    aaa = R"""
Weather report: Hell

     \  /       Partly cloudy
   _ /"".-.     20 °C          
     \_(   ).   ↘ 4 km/h       
     /(___(__)  10 km          
                0.1 mm                                  
"""
    wp.rect(x, y, 520, 200, (0,0,0,128))
    #ikr, font rendering sucks :{
    wp.ctx.fontmode="1"
    wp.ctx.text((x + 10, y + 10), aaa, font=wp.font, fill=(255, 255, 255, 128))

wp = Wallpaint(Image.open("wallhaven-rq75r7_1920x1080.png"), ImageFont.truetype("consola.ttf", 20))


CalendarWidget(wp, 300, 300)
NoteWidget(wp, 600,600, ["eat cake", "sleep", "go outside"])
WeatherWidget(wp, 1000, 300)

wp.out().save("out.png")