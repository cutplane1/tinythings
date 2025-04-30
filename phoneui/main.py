from phone import *

class Clicker:
    def __init__(self):
        self.clicks = 0

    def controls(self):
        if rl.is_key_pressed(rl.KEY_LEFT):
            self.clicks += 1
        if rl.is_key_pressed(rl.KEY_RIGHT):
            sm.change_scene("Menu")
    
    def draw(self):
        rl.draw_text("Clicks: " + str(self.clicks), 0, 0, 40, screenblack)
        draw_controls(center_btn="Click", left_btn=None)

add_app("Clicker", Clicker())
run()