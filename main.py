from tkinter import *
import time
__author__ = 'max'

root = Tk()
canv = Canvas(root, width=630, height=630, bg='white')
canv.pack()

f = open('input.txt').readlines()

globalx = 135
globaly = 165


class Pacman:

    def __init__(self, canv):
        self.canv = canv


    def draw(self, x, y, grid, turn):
        self.canv.delete('pac')
        if turn == 4:
            self.canv.create_arc((x + grid // 2, y + grid // 2, x - grid // 2, y - grid // 2), style=PIESLICE, start=30,
                            extent=300, fill="yellow", tag='pac')
        elif turn == 3:
            self.canv.create_arc((x + grid // 2, y + grid // 2, x - grid // 2, y - grid // 2), style=PIESLICE, start=210,
                            extent=300, fill="yellow", tag='pac')
        elif turn == 2:
            self.canv.create_arc((x + grid // 2, y + grid // 2, x - grid // 2, y - grid // 2), style=PIESLICE, start=300,
                            extent=300, fill="yellow", tag='pac')
        elif turn == 1:
            self.canv.create_arc((x + grid // 2, y + grid // 2, x - grid // 2, y - grid // 2), style=PIESLICE, start=120,
                            extent=300, fill="yellow", tag='pac')
        self.canv.update()


class Field:

    def __init__(self, f, canv, grid=30):
        self.canv = canv
        self.f = f
        self.j = -1
        self.impossible = []
        self.grid = grid

    def draw_field(self):
        for line in self.f:
            self.j += 1
            i = -1
            Z = list(map(int, line.split()))
            for elem in Z:
                i += 1
                if elem == 0:
                    canv.create_rectangle(i * self.grid, self.j * self.grid, self.grid * (i + 1), self.grid * (self.j + 1), fill="blue",
                                          outline="black")
                    self.impossible.append([((self.f.index(line)) * self.grid + self.grid // 2) // self.grid,
                                       (((i) * self.grid + self.grid // 2) // self.grid)])  # numeration by null!
                elif elem == 1:
                    canv.create_rectangle(i * self.grid, self.j * self.grid, self.grid * (i + 1), self.grid * (self.j + 1), fill="gray",
                                         outline="gray")
        return self.impossible


class Event_manager:
    def __init__(self,turn, impossible):
        self.direction = 'stop'
        self.grid = 30
        self.impossible = impossible
        self.vx = 0
        self.vy = 0
        self.turn = turn
        self.var_list = [0, 0, 0, 0, 0]

    def go_left(self, event):
        self.direction = 'left'
        print('left')

    def go_right(self, event):
        self.direction = 'right'
        print('right')

    def go_up(self, event):
        self.direction = 'up'
        print('up')

    def go_down(self, event):
        self.direction = 'down'
        print('down')

    def go_stop(self, event):
        self.direction = 'stop'
        print('stop')

    def iliketomoveit(self, x):

        if self.direction == 'left':
            self.vy = 0
            self.vx = -1
            self.turn = 3

        elif self.direction == 'right':
            self.vx = 1
            self.vy = 0
            self.turn = 4

        elif self.direction == 'up':
            self.vy = -1
            self.vx = 0
            self.turn = 1

        elif self.direction == 'down':
            self.vy = 1
            self.vx = 0
            self.turn = 2

        elif self.direction == 'stop':
            self.vy = 0
            self.vx = 0
        self.var_list[2] = self.vx
        self.var_list[3] = self.vy
        self.var_list[1] = self.vy
        self.var_list[4] = self.turn

    def collisions(self, x, y):

        pax = x // self.grid
        pay = y // self.grid

        if self.direction == 'left' and [pay, pax - 1] in self.impossible:
            self.direction = 'stop'

        elif self.direction == 'right' and [pay, pax + 1] in self.impossible:
            self.direction = 'stop'

        elif self.direction == 'up' and [pay - 1, pax] in self.impossible:
            self.direction = 'stop'

        elif self.direction == 'down' and [pay + 1, pax] in self.impossible:
            self.direction = 'stop'

    def binds(self, root):
        # _________________bindings______________________

        root.bind('<Left>', event_manager.go_left)
        root.bind('<Right>', event_manager.go_right)
        root.bind('<Up>', event_manager.go_up)
        root.bind('<Down>', event_manager.go_down)
        root.bind("<space>", event_manager.go_stop)

    def withdrow(self):
        return self.var_list

field = Field(f, canv)
imp = field.draw_field()

event_manager = Event_manager(1, imp)
pac = Pacman(canv)
event_manager.binds(root)

while True:

    if (not (globalx + 15) % 30) and not ((globaly + 15) % 30):
        event_manager.collisions(globalx, globaly)
        event_manager.iliketomoveit(globalx)

    utlst = event_manager.withdrow()

    pac.draw(globalx, globaly, 30, utlst[4])
    globalx += utlst[2]
    globaly += utlst[3]

    time.sleep(0.01)

f.close()
if __name__ == '__main__':
    root.mainloop()
