import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as vec3
import time

minecraft = minecraft.Minecraft.create()

# Sets the world to an immutable sandbox
def setup():
  print("resetting the map")
  
  minecraft.setBlocks(-128,0,-128,128,64,128,block.AIR.id)

  minecraft.setBlocks(-128,-1,-128,128,-1,128,block.SANDSTONE.id)

  minecraft.player.setPos(15,20,15)

  minecraft.setting("world_immutable", True)

def addVectors(vector1, vector2):
  vector1.x = vector1.x + vector2.x
  vector1.y = vector1.y + vector2.y
  vector1.z = vector1.z + vector2.z
  return vector1

def turnVectorClockwise(vector):
  vector = vec3.Vec3(-vector.z,vector.y,vector.x)
  return vector

def drawAxis():
    print("Drawing Axis on Map")
    
    colour = 13
    drawX(vec3.Vec3(19,3,0),block.WOOL.id,colour)
    spawnLine(vec3.Vec3(-6,0,0),vec3.Vec3(1,0,0),21,colour,block.GOLD_BLOCK.id)
    
    colour = 3
    drawY(vec3.Vec3(0,17,0),block.WOOL.id,colour)
    spawnLine(vec3.Vec3(0,-6,0),vec3.Vec3(0,1,0),21,colour,block.GOLD_BLOCK.id)
    
    colour = 2
    drawZ(vec3.Vec3(0,5,17),block.WOOL.id, colour)
    spawnLine(vec3.Vec3(0,0,-6),vec3.Vec3(0,0,1),21,colour,block.GOLD_BLOCK.id)
    
    minecraft.setBlock(0,0,0, block.GOLD_BLOCK.id)

# spawns a line of blocks from a position
def spawnLine(position, direction, length, blockData, blockId2):
    for i in range(0,length):
        time.sleep(0.05)
        position = addVectors(position,direction)
        if (i % 5 == 0):
            minecraft.setBlock(position.x,position.y,position.z, blockId2)  
        else:
            minecraft.setBlock(position.x,position.y,position.z, 35, blockData)
    return position

def drawX(position,blockId,blockData):
    minecraft.setBlock(position.x,position.y,position.z,blockId,blockData)
    minecraft.setBlock(position.x+1,position.y+1,position.z,blockId,blockData)
    minecraft.setBlock(position.x+1,position.y-1,position.z,blockId,blockData)
    minecraft.setBlock(position.x+2,position.y+2,position.z,blockId,blockData)
    minecraft.setBlock(position.x+2,position.y-2,position.z,blockId,blockData)
    minecraft.setBlock(position.x-1,position.y+1,position.z,blockId,blockData)
    minecraft.setBlock(position.x-1,position.y-1,position.z,blockId,blockData)
    minecraft.setBlock(position.x-2,position.y+2,position.z,blockId,blockData)
    minecraft.setBlock(position.x-2,position.y-2,position.z,blockId,blockData)

def drawY(position,blockId,blockData):
    minecraft.setBlock(position.x,position.y,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y+1,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y+2,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y+3,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y+4,position.z+1,blockId,blockData)
    minecraft.setBlock(position.x,position.y+4,position.z-1,blockId,blockData)
    minecraft.setBlock(position.x,position.y+5,position.z+2,blockId,blockData)
    minecraft.setBlock(position.x,position.y+5,position.z-2,blockId,blockData)

def drawZ(position,blockId,blockData):
    minecraft.setBlock(position.x,position.y,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y,position.z+1,blockId,blockData)
    minecraft.setBlock(position.x,position.y,position.z+2,blockId,blockData)
    minecraft.setBlock(position.x,position.y,position.z+3,blockId,blockData)
    minecraft.setBlock(position.x,position.y,position.z+4,blockId,blockData)
    minecraft.setBlock(position.x,position.y-3,position.z+3,blockId,blockData)
    minecraft.setBlock(position.x,position.y-2,position.z+2,blockId,blockData)
    minecraft.setBlock(position.x,position.y-1,position.z+1,blockId,blockData)
    minecraft.setBlock(position.x,position.y-4,position.z,blockId,blockData)
    minecraft.setBlock(position.x,position.y-4,position.z+1,blockId,blockData)
    minecraft.setBlock(position.x,position.y-4,position.z+2,blockId,blockData)
    minecraft.setBlock(position.x,position.y-4,position.z+3,blockId,blockData)
    minecraft.setBlock(position.x,position.y-4,position.z+4,blockId,blockData)


setup()