from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time 

x = 10
y = 110
z = 12

mc.player.setTilePos(x, y, z)

time.sleep(10)

x = 55
y = 115
z = 20

mc.player.setTilePos(x, y, z)
