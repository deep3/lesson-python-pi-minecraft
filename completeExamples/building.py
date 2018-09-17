import deep3.util as util
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import time
from math import *

# spawns a line of blocks from a position
def spawnLine(position,direction,length,blockId):
    for i in range(1,length):
        time.sleep(0.1)
        print(i)
        position = util.addVectors(position,direction)
        minecraft.setBlock(position.x,position.y,position.z, blockId)
    return position

# spawns a simple flat roof on top of the building
def simpleRoof(position, length):
    for i in range(0, length):
        spawnLine(vec3.Vec3(position.x+i,position.y,position.z-1), vec3.Vec3(0,0,1), 11, block.WOOD_PLANKS.id)

# spawns a house, the two for loops allow a pupil to action
# the height of the walls
def spawnHouse(position, height, length):
# already available to them
  direction = vec3.Vec3(1,0,0)
  # allows a pupil to give the height
  for j in range (0, height):
    # number of walls to create from spawnline
    for i in range(0,4):
      position = spawnLine(position,direction,length,block.BRICK_BLOCK.id)
      direction = util.turnVectorClockwise(direction)
    # adds the height on to the next layer of the wall
    position.y += 1


# just calls the functions we want in order to build the house
#spawnLine(vec3.Vec3(30,0,0)
time.sleep(2)
spawnHouse(vec3.Vec3(0,0,0), 5, 10)
simpleRoof(vec3.Vec3(0,5,0),10)


# building advanced roof, to iterate positively and negatively
def help(height):
    if height < 0:
        print("counting down")
        return range(height, 0)
    else:
        print("counting up")
        return range(0, height)

# advanced stuff - only advanced students should consider
def spawnAdvancedRoof(position, direction, height, length):
        for i in help(height):
            newPosition = vec3.Vec3(position.x + direction.x * i, position.y + direction.y * i, position.z + direction.z * i)
            spawnLine(newPosition, util.turnVectorClockwise(vec3.Vec3(direction.x, 0, direction.z)),length, block.WOOD_PLANKS.id)

#spawnFlatRoof(vec3.Vec3(0,6,0), vec3.Vec3(1,0,0),5)
#spawnAdvancedRoof(vec3.Vec3(0,6,0), vec3.Vec3(1,1,0),5, 10)
#spawnLine(vec3.Vec3(0,11,0), vec3.Vec3(1,1,2))
#spawnLine(vec3.Vec3(0,1,0), vec3.Vec3(1,0,0), 10, block.BRICK_BLOCK.id)