import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import time
from math import *

minecraft = minecraft.Minecraft.create()


def addVectors(vector1, vector2):
  vector1.x = vector1.x + vector2.x
  vector1.y = vector1.y + vector2.y
  vector1.z = vector1.z + vector2.z
  return vector1

def fireCannon(position, direction):
    position=addVectors(position,direction)
    hit = False
    while not (hit):
        time.sleep(0.1)
        minecraft.setBlock(position.x,position.y,position.z, block.AIR.id)
        position=addVectors(position,direction)
        if not (minecraft.getBlock(position.x,position.y,position.z) == block.AIR.id):
           hit = True
        minecraft.setBlock(position.x,position.y,position.z, block.IRON_BLOCK.id)
    explosion(position)
    return position

def explosion (position):
    minecraft.setBlock(position.x, position.y, position.z, block.AIR.id)
    minecraft.setBlock(position.x+1, position.y, position.z, block.AIR.id)
    minecraft.setBlock(position.x-1, position.y, position.z, block.AIR.id)
    minecraft.setBlock(position.x, position.y+1, position.z, block.AIR.id)
    minecraft.setBlock(position.x, position.y-1, position.z, block.AIR.id)
    minecraft.setBlock(position.x, position.y, position.z+1, block.AIR.id)
    minecraft.setBlock(position.x, position.y, position.z-1, block.AIR.id)

playerPos = minecraft.player.getPos()
fireCannon(playerPos, vec3.Vec3(1,0,0))
