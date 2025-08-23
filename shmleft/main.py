import pyray as rl
import math
import copy
import random
import sys
import os
import psutil




colors = [rl.RED, rl.GREEN, rl.BLUE, rl.YELLOW, rl.PURPLE, rl.ORANGE]

def get_polygon_vertices(
    center: rl.Vector2,
    sides: int,
    radius: float,
    rotation: float = 0.0
) -> list[rl.Vector2]:
    if sides < 3:
        sides = 3
    
    vertices = []
    rotation_rad = math.radians(rotation)
    angle_step = 2 * math.pi / sides
    
    for i in range(sides):
        angle = rotation_rad + angle_step * i
        x = center.x + math.cos(angle) * radius
        y = center.y + math.sin(angle) * radius
        vertices.append(rl.Vector2(x, y))
    
    return vertices

def get_polygon_vertices_and_normals(
    center: rl.Vector2,
    sides: int,
    radius: float,
    rotation: float = 0.0
) -> tuple[list[rl.Vector2], list[rl.Vector2]]:
    if sides < 3:
        sides = 3
    
    vertices = []
    normals = []
    rotation_rad = math.radians(rotation)
    angle_step = 2 * math.pi / sides
    
    for i in range(sides):
        angle = rotation_rad + angle_step * i
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)
        
        x = center.x + cos_angle * radius
        y = center.y + sin_angle * radius
        vertices.append(rl.Vector2(x, y))
        
        normals.append(rl.Vector2(cos_angle, sin_angle))
    
    return vertices, normals
health = 3
class Bullet:
    def __init__(self, position: rl.Vector2, direction: rl.Vector2):
        self.pos = position
        self.dir = direction
        self.speed = 3
        self.timer = 0
        self.timeout = 240
        self.color = random.choice(colors)
        self.rect = rl.Rectangle(int(self.pos.x), int(self.pos.y), 10, 10)
        self.unalive = False
    
    def draw(self):
        if self.unalive:
            return
        # rl.draw_rectangle(int(self.pos.x), int(self.pos.y), 10, 10, self.color)
        rl.draw_rectangle_rec(self.rect, self.color)
        # rl.draw_line(int(self.pos.x), int(self.pos.y), int(self.pos.x + self.dir.x*50), int(self.pos.y + self.dir.y*50), rl.BLUE)
    
    def update(self):
        if self.unalive:
            return
        # global player
        global health
        global is_getted_damage
        if rl.check_collision_recs(self.rect, player.hitbox):
            health -= 1
            self.unalive = True
            is_getted_damage = True
        self.rect.x += self.dir.x * self.speed
        self.rect.y += self.dir.y * self.speed
        self.timer += 1
        if self.timer >= self.timeout:
            bullets.remove(self)
            del self

class BulletSpawner:
    def __init__(self, position: rl.Vector2, direction: rl.Vector2):
        self.pos = position
        self.dir = direction
        self.timer = 0
        self.timeout = 10

    def update(self):
            if self.timer >= self.timeout:
                self.timer = 0
                c_pos = rl.Vector2(self.pos.x, self.pos.y)
                c_dir = rl.Vector2(self.dir.x, self.dir.y)
                bullets.append(Bullet(c_pos, c_dir))
            else:
                self.timer += 1


# class Polygon:
#     def __init__(self, position: rl.Vector2, sides: int, radius: float, rotation: float = 0.0):
#         self.pos = position
#         self.sides = sides
#         self.radius = radius
#         self.rotation = rotation
    
#     def draw(self):

class Circle:
    def __init__(self, position: rl.Vector2, sides: int, radius: float, rotation: float = 0.0):
        self.pos = position
        self.sides = sides
        self.radius = radius
        self.rotation = rotation
        self.bullet_spawners = [BulletSpawner(rl.Vector2(0,0), rl.Vector2(0, 0)) for _ in range(sides)]
    def update(self):
        whatever = get_polygon_vertices_and_normals(self.pos, self.sides, self.radius, self.rotation)

        verticles = whatever[0]
        normals = whatever[1]

        for i, bullet_spawner in enumerate(self.bullet_spawners):
            bullet_spawner.pos = rl.Vector2(verticles[i].x, verticles[i].y)
            bullet_spawner.dir = rl.Vector2(normals[i].x, normals[i].y)
            bullet_spawner.update()


class Player:
    def __init__(self, position: rl.Vector2):
        self.pos = position
        self.speed = 7
        self.rect = rl.Rectangle(int(self.pos.x), int(self.pos.y), 30, 30)
        self.hitbox = rl.Rectangle(int(self.pos.x)+11, int(self.pos.y)+11, 8, 8)
        self.shift_pressed = False
    
    def draw(self):
        rl.draw_rectangle_rec(self.rect, rl.RED)
        if self.shift_pressed:
            rl.draw_rectangle_rec(self.hitbox, rl.BLUE)

    def update(self):
        if rl.is_key_down(rl.KEY_LEFT_SHIFT):
            self.speed = 2
            self.shift_pressed = True
        if rl.is_key_up(rl.KEY_LEFT_SHIFT):
            self.speed = 7
            self.shift_pressed = False
        k = rl.Vector2(0, 0)
        if rl.is_key_down(rl.KEY_RIGHT): k.x += 1
        if rl.is_key_down(rl.KEY_LEFT): k.x -= 1
        if rl.is_key_down(rl.KEY_DOWN): k.y += 1
        if rl.is_key_down(rl.KEY_UP): k.y -= 1

        # normalization
        if k.x != 0 or k.y != 0:
            # length = sqrt((ax * ax) + (ay * ay) + (az * az)) 
            length = math.sqrt(k.x * k.x + k.y * k.y)
            self.pos.x += (k.x / length) * self.speed
            self.pos.y += (k.y / length) * self.speed
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.hitbox.x = self.rect.x + 11
        self.hitbox.y = self.rect.y + 11
        




def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss / (1024 * 1024)


# class Arc:
#     def __init__(self, position: rl.Vector2, radius: float, start_angle: float = 120, end_angle: float = 180, rotation: float = 0.0):
#         self.pos = position
#         self.radius = radius
#         self.rotation = rotation
#         self.bullet_spawner = BulletSpawner(rl.Vector2(0,0), rl.Vector2(0, 1))
#         self.shoot = True
#         self.start_angle = start_angle
#         self.end_angle = end_angle
#         self.clockwise = True
#         self.speed = 5

#     def update(self):
#         self.rotation += self.speed
#         if self.rotation >= self.start_angle:
#             self.shoot = False
#         if self.rotation >= self.end_angle:
#             self.rotation = 0
#             self.shoot = True
#         if self.shoot:
#             whatever = get_polygon_vertices_and_normals(self.pos, 3, self.radius, self.rotation)
#             rl.draw_poly_lines(self.pos, 3, self.radius, self.rotation, rl.RED)

#             verticle = whatever[0][0]
#             self.bullet_spawner.pos = rl.Vector2(verticle.x, verticle.y)
#             self.bullet_spawner.update()



bullets = []
# resolution = (600, 800)
resolution = (768, 1024)
rl.init_window(resolution[0], resolution[1], "raylib [core] example - basic window")
rl.set_target_fps(60)



player = Player(rl.Vector2((resolution[0] / 2)-30, 650))
# b = Bullet(rl.Vector2(100, 100), rl.Vector2(-1, 1))
# bs = BulletSpawner(rl.Vector2(100, 100), rl.Vector2(-1, 1))
cir = Circle(rl.Vector2((resolution[0] / 2) - 15, 300), 24, 100)
# cir2 = Circle(rl.Vector2(250, 400), 4, 100)

latch = False
titi = 0

# arc = Arc(rl.Vector2(250, 400), 100)
# arc2 = Arc(rl.Vector2(250, 400), 100)
# arc2.start_angle = 0
# arc2.end_angle = 0

is_getted_damage = False
bullet_cleanup_latch = False
hit_msg_timer = 0

you_died = False
score = 0

while not rl.window_should_close():
    if not you_died:
        score += 1
    if health <= 0:
        you_died = True
    if rl.is_key_down(rl.KEY_Q):
        bullets = []
    player.update()

    # arc.update()
    # arc2.update()
    # arc2.rotation += 3
    cir.update()
    # # cir2.update()
    # # cir2.rotation += 3


    if titi > 60:
        latch = not latch
        titi = 0
    if latch:
        cir.rotation += 2
        cir.radius += 2
    else:
        cir.rotation -= 1
        cir.radius -= 2
    titi += 1



    rl.begin_drawing()

    rl.clear_background(rl.BLACK)




    player.draw()


        
    for bullet in bullets:
        bullet.update()
        bullet.draw()
    
    rl.draw_rectangle(0, 0, 180, 60, rl.BLACK)
    #rl.draw_text("MEM: {:.2f} MB".format(process_memory()), 0, 0, 20, rl.WHITE)
    rl.draw_text("OBJS: {}".format(len(bullets)), 0, 20, 20, rl.WHITE)
    rl.draw_text("FPS: {}".format(rl.get_fps()), 0, 40, 20, rl.WHITE)
    rl.draw_text("HEALTH: {}".format(health), 0, 60, 20, rl.WHITE)

    if is_getted_damage and not you_died:
        rl.draw_rectangle(0, 200, resolution[0], 60, rl.MAROON)
        rl.draw_text("-1 HP", 50, 220, 20, rl.WHITE)
        if not bullet_cleanup_latch:
            bullet_cleanup_latch = True
            bullets = []
        hit_msg_timer += 1
        if hit_msg_timer > 60:
            hit_msg_timer = 0
            is_getted_damage = False
            bullet_cleanup_latch = False
    
    if you_died:
        if rl.is_key_down(rl.KEY_Q):
            break
        rl.draw_rectangle(0, 200, resolution[0], 60, rl.MAROON)
        rl.draw_text("YOU DIED", 50, 210, 20, rl.WHITE)
        rl.draw_text("YOUR SCORE: {}".format(score), 50, 230, 20, rl.WHITE)
        rl.draw_text("PRESS Q TO QUIT", (resolution[0] //2)-105, 400, 20, rl.WHITE)
        player.pos.x = 1000
        player.pos.y = 1000
        for sp in cir.bullet_spawners:
            sp.timeout = 99999999999999999
    rl.end_drawing()

rl.close_window()
scmsg = "YOUR SCORE: {}".format(score)
print("-"*len(scmsg))
print(scmsg)