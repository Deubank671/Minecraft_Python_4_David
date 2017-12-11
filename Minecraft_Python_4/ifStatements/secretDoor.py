from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 24.5
y = 1.0
z = 39.7

gift = mc.getBlock(x, y, z)
if gift != 0:
    if gift == 57:
        x = 23.5
        y = 0.0
        z = 40.7
        blockType = 0
        mc.setBlock(x, y, z, blockType)
        x = 23.5
        y = 0.0
        z = 40.7
        blockType = 0
        mc.setBlock(x, y + 1, z, blockType)
    if gift != 57:
        mc.player.getPos()
        mc.setBlock(x, y - 1, z, 10)
        


else:
    mc.postToChat("Place an offering on the pedestal.")
