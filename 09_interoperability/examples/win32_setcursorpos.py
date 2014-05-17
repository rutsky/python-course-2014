import ctypes
import math
import time

set_cursor_pos_func = ctypes.windll.user32.SetCursorPos

while True:
    t = time.clock()
    x = 300 + 300 * math.sin(5 * t)
    y = 200 + 200 * math.cos(6 * t)
    set_cursor_pos_func(int(x), int(y))
