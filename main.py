# Imports
from microbit import *
import random

debug = False

def rnd():
    return random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ])

class pixel:

    def __init__(self, b):
        self.state = True
        self.brightness = b
    
    def set_brightness(self):
        if self.state:
            self.brightness += 1
            if self.brightness >= 9:
                self.brightness = 9
                self.state = False
        else:
            self.brightness -= 1
            if self.brightness <= 0:
                self.brightness = 0
                self.state = True
                
        return (self.brightness)
    
board = []
rows, cols = 5, 5
for i in range(rows):
	col = []
	for j in range(cols):
		col.append(pixel(rnd()))
	board.append(col)
if debug:
    print(board)

display.clear()

while True:
    for i in range(rows):
        for j in range(cols):
           display.set_pixel(i,j,board[i][j].set_brightness())

    sleep(50)
    