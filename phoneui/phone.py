import pyray as rl
from datetime import datetime

last_selected = None

res = (320, 480)
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


def draw_controls(left_btn_name = "Select", right_btn_name = "Menu", right_btn_offset = 240):
    rl.draw_text(left_btn_name, 5, res[1] - 30, 30, screenblack)
    rl.draw_text(right_btn_name, right_btn_offset, res[1] - 30, 30, screenblack)

class Menu:
    def __init__(self, left_btn_name = "Select", select_scene = None):
        self.options = []
        self.selected = 0
        self.left_btn_name = left_btn_name
        self.select_scene = select_scene

    def draw(self):
        for i, option in enumerate(self.options):
            if i == self.selected:
                rl.draw_rectangle(0, i * 50, 320, 50, screenblack)
                rl.draw_text(str(option), 10, i * 50 + 10, 40, screenwhite)
            else:
                rl.draw_text((str(option)), 10, i * 50 + 10, 40, screenblack)
        
        draw_controls(self.left_btn_name)
    
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

menu = Menu("Select")
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
        time = datetime.now().strftime("%H:%M")
        # time = "13:37"
        rl.draw_text(time, 60, 100, 80, screenblack)

        draw_controls("Select", "Contacts", 175)


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

contacts = Menu("Call")
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



settings = Menu("Select")
settings.options = ["Themes"]

themes = Menu("Change", "change_palette_ac")
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
    sm.change_scene(scene)
    rl.init_window(res[0], res[1], "PhoneUI")
    while not rl.window_should_close():
        sm.controls()
        rl.begin_drawing()
        rl.clear_background(screenwhite)
        sm.draw()
        rl.end_drawing()

    rl.close_window()