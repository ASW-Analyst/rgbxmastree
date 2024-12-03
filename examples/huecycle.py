from tree import RGBXmasTree
from colorzero import Color, Hue
import time

tree = RGBXmasTree()

tree.color = Color('red')
tree.brightness = 0.05

try:
    while True:
        tree.color += Hue(deg=1)
        time.sleep(0.005)
except KeyboardInterrupt:
    tree.close()
