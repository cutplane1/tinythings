import pyray as rl
import math
from datetime import datetime

wx = 500
c_x = 500//2

def draw_line_angle(len: float, angle_deg: float, thick: float, color: rl.Color):
    c = rl.Vector2(c_x,c_x)
    angle = math.radians(angle_deg-90)
    end = rl.Vector2(c.x + len * math.cos(angle), c.y + len * math.sin(angle))
    rl.draw_line_ex(c, end, thick, color)

def tf_to_tw(x: int) -> int:
    if x <= 12: return x
    else: return x - 12

rl.init_window(wx,wx,"clock")
rl.set_target_fps(15)

while not rl.window_should_close():
    rl.begin_drawing()
    rl.clear_background(rl.WHITE)
    now = datetime.now()
    rl.draw_circle_lines(c_x,c_x, 230, rl.BLACK)
    draw_line_angle(130,tf_to_tw(now.hour)*30,3,rl.BLACK)
    draw_line_angle(170,now.minute*6,2,rl.BLACK)
    draw_line_angle(200,now.second*6,1,rl.RED)
    rl.end_drawing()

rl.close_window()