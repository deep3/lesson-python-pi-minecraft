import mcpi.minecraft as minecraft
import mcpi.block as block
from math import *

colors = [14, 1, 4, 5, 3, 11, 10]

mc = minecraft.Minecraft.create()
height = 40

mc.setBlocks(-64,0,0,64,height + len(colors),0,0)
for x in range(0, 128):
        for colourindex in range(0, len(colors)):
                y = sin((x / 128.0) * pi) * height + colourindex
                mc.setBlock(x - 64, y, 0, block.WOOL.id, colors[len(colors) - 1 - colourindex])