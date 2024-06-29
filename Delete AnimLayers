"""The script deletes empty and muted animation layers
Phyton
by @mmariiaregiina
"""
import maya.cmds as cmds
import maya.mel as mel

mel.eval("deleteEmptyAnimLayers();")

a = cmds.ls(type='animLayer')
for i in a:    
  if cmds.animLayer(i, q=1, mute=1): 
    cmds.delete (i)
