"""
The script creates locators in a pivot of selected object.
Possible to create several locs simultaneously.
Phyton.
by @mmariiaregiina
"""
import maya.cmds as cmds 

sel = cmds.ls(sl=1)
if len(sel) == 0:
    cmds.inViewMessage(amg='ERROR: <hl>you have to select an object</hl>.', pos='midCenter', fade=1)

pos = cmds.xform(sel, q=1, t=1)
loc = cmds.spaceLocator(n='my_yellow_parent_LOC')
cmds.setAttr (".localScaleX", 15)
cmds.setAttr (".localScaleY", 15)
cmds.setAttr (".localScaleZ", 15)
cmds.color(loc, rgb=(255, 255, 0))
cmds.xform(loc, t=pos)
cmds.parentConstraint(sel, loc)
