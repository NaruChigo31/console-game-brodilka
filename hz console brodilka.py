import keyboard
import time
import os
import math

map = [
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
    ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
]
# print(len(map[0]))
# def create_map(height,width):
#     global map
#     for i in range(0,height):
#         map.append([])
#         for j in range(0,width):
#             map[i].append("0")
#     print(map)

# create_map(10,15)

def print_map():
    global map
    for i in range(0,len(map)):
        row = ""
        for j in range(0,len(map[i])):
            if map[i][j] == "1":
                row += "▮"
            elif map[i][j] == "X":
                row += "X"
            else:
                row += " "*1
        print(f"{row}")


game = True

# def check_move_input():

#  symbol - in map
#  image - in console
class Object:
    def __init__(self, x, y, symbol: str, image: str, tangible: bool):
        self.x = x
        self.y = y
        self.symbol = symbol
        self.image = image
        self.tangible = tangible

class Camera(Object):
    def __init__(self, x, y, symbol="C"):
        super().__init__(x, y, symbol, image=None, tangible=False)
        self.x = x
        self.y = y
    
    def set_on_map(self):
        global map
        global player
        self.y = player.y
        self.x = player.x

    def draw(self):
        camera_range = {
            "x": 20,
            "y": 5
        }
        box_range = {
            "x": 10,
            "y": 2
        }
        if abs(player.x) > self.x-camera_range['x'] or abs(player.y) > self.y-camera_range['y']:
            if player.y > self.y+box_range['y']:
                self.y += 1
            elif player.y < self.y-box_range['y']:
                self.y -= 1

            if player.x > self.x+box_range['x']:  
                self.x += 1
            elif player.x < self.x-box_range['x']:
                self.x -= 1

        shown_map = ""
        for y in range(self.y-camera_range['y'], self.y+camera_range['y']+1):
            if y >= 0 and y < len(map):
                row = ""
                for x in range(self.x-camera_range['x'], self.x+camera_range['x']+1):
                    if x >= 0 and x < len(map[0]):
                        if map[y][x] == "1":
                            row += "▮"
                        elif map[y][x] == "X":
                            row += "X"
                        else:
                            row += " "*1
                    else:
                        row += "."
                shown_map += (row+"\n")
            else:
                shown_map += "."*(camera_range['x']*2+1)+"\n"
        print(shown_map)
            

class Player(Object):
    def __init__(self, x, y, symbol="X", image="X"):
        super().__init__(x, y, symbol, image, tangible=True)
        self.x = x
        self.y = y
    
    def set_on_map(self):
        global map
        global game
        if map[self.y][self.x] == "0":
            map[self.y][self.x] = self.symbol
        else:
            print("Player can't be placed here")
            game = False

    def move(self):
        prev_y_x = (self.y, self.x)
        global map
        if keyboard.is_pressed("w"):
            if self.y-1 >= 0 and map[self.y-1][self.x] == "0" :
                self.y -= 1
                map[self.y][self.x], map[prev_y_x[0]][prev_y_x[1]] = self.symbol, "0"
        elif keyboard.is_pressed("s"):
            if self.y+1 < len(map) and map[self.y+1][self.x] == "0":
                self.y += 1
                map[self.y][self.x], map[prev_y_x[0]][prev_y_x[1]] = self.symbol, "0"
        elif keyboard.is_pressed("a"):
            if self.x-1 >= 0 and map[self.y][self.x-1] == "0":
                self.x -= 1
                map[self.y][self.x], map[prev_y_x[0]][prev_y_x[1]] = self.symbol, "0"
        elif keyboard.is_pressed("d"):
            if self.x+1 < len(map[0]) and map[self.y][self.x+1] == "0":
                self.x += 1
                map[self.y][self.x], map[prev_y_x[0]][prev_y_x[1]] = self.symbol, "0"
        print(f"prev_y_x: {prev_y_x}")


player = Player(x=10,y=10)
player.set_on_map()
camera = Camera(x=0,y=1)
camera.set_on_map()
is_pressing = False

while game == True:
    camera.draw()

    if keyboard.is_pressed('q'):
        game = False
        os.system('cls')
    if keyboard.is_pressed("w") or keyboard.is_pressed("a") or keyboard.is_pressed("s") or keyboard.is_pressed("d"):
        player.move()
    print(f"Player x: {player.x}, y: {player.y}")

    time.sleep(0.1)
    os.system('cls')
