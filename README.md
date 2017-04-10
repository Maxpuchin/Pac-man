# Pac-man
from tkinter import *
import time
__author__ = 'max'


root = Tk()
canv = Canvas(root, width=470, height=460, bg='white')
canv.pack()

class field:
    def __init__(self, canv, h, w, col, colour, balls_lst, grid=15, lst=[]):
        self.canv = canv
        self.h = h
        self.w = w
        self.col = col
        self.grid = grid
        self.holecol = colour
        self.holes = lst
        self.balls_lst = balls_lst
    def draw_field(self):
        
        f1 = self.canv.create_rectangle(15, 15, 45 + self.h,45 + self.w, fill='blue')
        f = self.canv.create_rectangle(30, 30, 30 + self.h, 30 + self.w, fill=self.col)
    def create_holes(self):
        a = self.canv.create_oval(30, 30, 30 + self.grid * 2, 30 + self.grid * 2, fill=self.holecol)
        b = self.canv.create_oval(210, 30, 210 + self.grid * 2, 30 + self.grid * 2, fill=self.holecol)
        c = self.canv.create_oval(400, 30, 400 + self.grid * 2, 30 + self.grid * 2, fill=self.holecol)
        d = self.canv.create_oval(210, 400, 210 + self.grid * 2, 400 + self.grid * 2, fill=self.holecol)
        e = self.canv.create_oval(30, 400, 30 + self.grid * 2, 400 + self.grid * 2, fill=self.holecol)
        f = self.canv.create_oval(400, 400, 400 + self.grid * 2, 400 + self.grid * 2, fill=self.holecol)
        self.holes.append(a)
        self.holes.append(b)
        self.holes.append(c)
        self.holes.append(d)
        self.holes.append(e)
        self.holes.append(f)
        return self.holes
    
    def balls_move(self):
        for i in self.balls_lst:
            i[0] += i[2]
            i[1] += i[3]
class balls:
    def __init__(self, canv, x, y, t, grid=15):
        self.grid = grid
        self.canv = canv
        self.x = x
        self.y = y
        self.t = t
    def create_balls(self):
        self.canv.create_oval(self.x, self.y, self.x + self.grid * 2, self.y + self.grid * 2, fill='white', tag='b')
    def move(self):
        canv.delete('b')
        vx = 1
        vy = 1
        while vx != 0 and vy != 0:
            
            self.x += 1
            self.y += 1
            vx -= 0.01
            vy -= 0.01
f = field(canv, 400, 400, 'green', 'black', [])
f.draw_field()
f.create_holes()
b = balls(canv, 60, 60, [])

while 1:
    b.move()
    b.create_balls()
    canv.update()
    time.sleep(0.01)
root.mainloop()
