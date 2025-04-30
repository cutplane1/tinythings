import pyray as rl
from datetime import datetime
# today is:
today_is=datetime.now().strftime("%d-%m-%y")
last_selected = None
texture = None
battery_tex = None
font = None
# res = (320, 480)
res = (176, 220)
def hex_to_rgb(hex: str) -> tuple[int, int, int]:
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))

palettes = []
palettes.append(((199, 240, 216), (67, 82, 61)))
palettes.append(((184,194,185), (56, 43, 38)))
palettes.append((hex_to_rgb("f0f6f0"),hex_to_rgb("222323")))
palettes.append((hex_to_rgb("83b07e"), hex_to_rgb("000000")))
palette = palettes[3]
screenwhite = rl.Color(palette[0][0], palette[0][1], palette[0][2], 255)
screenblack =  rl.Color(palette[1][0], palette[1][1], palette[1][2], 255)

img_something = rl.load_image("refs/theme1/3014_Natur_Pur/Navi1.png")


def draw_controls(left_btn="Select", center_btn=None, right_btn="Menu"):
    global font
    y_position = res[1] - 20
    font_size = 16

    if left_btn:
        # rl.draw_text(left_btn, 5, y_position, font_size, screenblack)
        rl.draw_text_ex(font, left_btn, (4, y_position), font_size, 0, rl.BLACK)

    if center_btn:
        # center_width = rl.measure_text(center_btn, font_size)
        center_width = rl.measure_text_ex(font, center_btn, font_size, 0).x
        center_x = (res[0] - center_width) // 2
        # rl.draw_text(center_btn, center_x, y_position, font_size, screenblack)
        rl.draw_text_ex(font, center_btn, (center_x, y_position), font_size, 0, rl.BLACK)

    if right_btn:
        # right_width = rl.measure_text(right_btn, font_size)
        right_width = rl.measure_text_ex(font, right_btn, font_size, 0).x
        right_x = res[0] - right_width - 4
        # rl.draw_text(right_btn, right_x, y_position, font_size, screenblack)
        rl.draw_text_ex(font, right_btn, (right_x, y_position), font_size, 0, rl.BLACK)


class Controls:
    def __init__(self, left_btn_name = "Select", center_btn_name = None, right_btn_name = "Menu"):
        self.left_btn_name = left_btn_name
        self.center_btn_name = center_btn_name
        self.right_btn_name = right_btn_name
    
    def draw(self):
        draw_controls(self.left_btn_name, self.center_btn_name, self.right_btn_name)

class Menu:
    def __init__(self, ctls: Controls, select_scene = None):
        self.options = []
        self.selected = 0
        self.ctls = ctls
        self.select_scene = select_scene

    def draw(self):
        for i, option in enumerate(self.options):
            if i == self.selected:
                rl.draw_rectangle(0, i * 30, 320, 30, screenblack)
                rl.draw_text(str(option), 10, i * 30 + 10, 20, screenwhite)
            else:
                rl.draw_text((str(option)), 10, i * 30 + 10, 20, screenblack)
        
        self.ctls.draw()
    
    def controls(self):
        global last_selected
        if rl.is_key_pressed(rl.KEY_LEFT):
            if self.select_scene is None:
                sm.change_scene(self.options[self.selected])
            else:
                last_selected = self.options[self.selected] 
                sm.change_scene(self.select_scene)
        if rl.is_key_pressed(rl.KEY_RIGHT):
            sm.change_scene("Start")
        if self.selected >= len(self.options):
            self.selected = 0
        if self.selected < 0:
            self.selected = len(self.options) - 1
        if rl.is_key_pressed(rl.KEY_UP):
            self.selected -= 1
        if rl.is_key_pressed(rl.KEY_DOWN):
            self.selected += 1

menu = Menu(Controls())
menu.options = ["Contacts", "Settings"]



class Start:
    def __init__(self):
        pass

    def controls(self):
        if rl.is_key_pressed(rl.KEY_LEFT):
            sm.change_scene("Menu")
        if rl.is_key_pressed(rl.KEY_RIGHT):
            sm.change_scene("Contacts")

    def draw(self):
        global texture
        global font
        rl.draw_texture(texture, 0, 0, rl.WHITE)
        rl.draw_texture(battery_tex, 145, 5, rl.Color(255, 255, 255, 255))
        # time = datetime.now().strftime("%H:%M")
        # rl.draw_text(time, 0, 0, 30, screenblack)
        # hardcoded coords. again. :>
        rl.draw_text_ex(font, "MeowTelecom", (37, 40), 18, 0, rl.BLACK)
        rl.draw_text_ex(font, "13:37", (5, 170), 18, 0, rl.BLACK)
        rl.draw_text_ex(font, today_is, (110, 170), 18, 0, rl.BLACK)

        draw_controls(left_btn="Menu", right_btn="Contacts")


st = Start()
class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.current_scene: str = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene

    def change_scene(self, name):
        if name not in self.scenes:
            return
        self.current_scene = name
    def controls(self):
        if hasattr(self.scenes[self.current_scene], "controls"):
            self.scenes[self.current_scene].controls()
    def draw(self):
        self.scenes[self.current_scene].draw()

contacts = Menu(Controls(left_btn_name=None, center_btn_name="Call", right_btn_name="Start"))
contacts.options = ["you", "your mommy", "mossad"]

class Action:
    def draw(self):
        sm.change_scene("Start")

class ChangePaletteAction(Action):
    def draw(self):
        global last_selected
        global screenwhite
        global screenblack
        screenwhite = rl.Color(last_selected[0][0], last_selected[0][1], last_selected[0][2], 255)
        screenblack = rl.Color(last_selected[1][0], last_selected[1][1], last_selected[1][2], 255)
        sm.change_scene("Themes")



settings = Menu(Controls(left_btn_name="Select", right_btn_name="Menu"))
settings.options = ["Themes"]

themes = Menu(Controls(left_btn_name=None, center_btn_name="Change", right_btn_name="Back"), "change_palette_ac")
themes.options = palettes


sm = SceneManager()
sm.add_scene("Menu", menu)
sm.add_scene("Start", st)
sm.add_scene("Contacts", contacts)
sm.add_scene("Settings", settings)
sm.add_scene("Themes", themes)
sm.add_scene("change_palette_ac", ChangePaletteAction())

# sm.change_scene("Start")

def add_app(app_name, app_scene):
    sm.add_scene(app_name, app_scene)
    menu.options.append(app_name)


def run(scene = "Start"):
    global texture
    global font
    global battery_tex
    sm.change_scene(scene)
    rl.init_window(res[0], res[1], "PhoneUI")
    texture = rl.load_texture_from_image(img_something)
    battery_img = rl.load_image("refs/batt.png")
    battery_tex = rl.load_texture_from_image(battery_img)
    rl.unload_image(battery_img)
    font = rl.load_font("arial.ttf")
    rl.unload_image(img_something)
    while not rl.window_should_close():
        sm.controls()
        rl.begin_drawing()
        rl.clear_background(screenwhite)
        sm.draw()
        rl.end_drawing()

    rl.close_window()