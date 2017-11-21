Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
4
Woooooooooooooooooooo
PYTHON!
<3s
MInecraft
>>> print("Woooo Minecraft")
Woooo Minecraft
>>> print("Adventures")
Adventures
>>> from mcpi.minecraft import Minecraft
>>> mc = Minecraft.create()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    mc = Minecraft.create()
  File "/usr/lib/python3/dist-packages/mcpi/minecraft.py", line 171, in create
    return Minecraft(Connection(address, port))
  File "/usr/lib/python3/dist-packages/mcpi/connection.py", line 17, in __init__
    self.socket.connect((address, port))
ConnectionRefusedError: [Errno 111] Connection refused
>>> mc.player.setTilePos(0, 120, 0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mc.player.setTilePos(0, 120, 0)
NameError: name 'mc' is not defined
>>> pickaxes = 12
>>> bread = 145
>>> bread = 145
>>> bread = 145
>>> >>> bread = 145
>>> bread = 145
>>>
