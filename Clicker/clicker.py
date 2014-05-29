import Xlib
from Xlib import display as d

import time


class Clicker:

    def __init__(self):
        self.display = d.Display()
        self.screen = self.display.screen()
        self.root = self.screen.root

    def mouse_click(self, x, y):
        self.root.warp_pointer(x, y)
        self.display.sync()
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonPress, 1)
        self.display.sync()
        time.sleep(0.05)
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonRelease, 1)
        self.display.sync()

    def mouse_detect(self):
        pointer = self.root.query_pointer()._data
        return (pointer["root_x"], pointer["root_y"])

def main():
    c = Clicker()
    position = c.mouse_detect()
    print(position)
    for i in range(100):
        c.mouse_click(position[0], position[1])

    
    



if __name__ == '__main__':
    main()
