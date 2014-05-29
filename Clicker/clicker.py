import Xlib
from Xlib import display as d

import time


class Clicker:

    def __init__(self):
        self.display = d.Display()
        self.screen = self.display.screen()
        self.root = self.screen.root

    def mouseClick(self, x, y):
        self.root.warp_pointer(x, y)
        self.display.sync()
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonPress, 1)
        self.display.sync()
        time.sleep(0.05)
        Xlib.ext.xtest.fake_input(self.display, Xlib.X.ButtonRelease, 1)
        self.display.sync()


def main():
    c = Clicker()
    for i in range(100):
        c.mouseClick(100, 100)


if __name__ == '__main__':
    main()
