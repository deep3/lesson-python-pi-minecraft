import sys
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    for hit in hits:
        block = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z)
        block.data = (block.data + 1) & 0xf;
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.id, block.data)
        mc.postToChat("Block data is now " + str(block.data))
    time.sleep(0.1)
