"""
The script creates a LOC in a pivot of selected object.
Phyton.
by @mmariiaregiina
"""
import maya.cmds as cmds 

if cmds.objExists("My_LOC_parent"):
    cmds.delete("My_LOC_parent")

sel = cmds.ls(sl=1)
if len(sel) == 0:
    cmds.inViewMessage(amg='ERROR: <hl>you have to select an object</hl>.', pos='midCenter', fade=1)

pos = cmds.xform(sel, q=1, t=1)
loc = cmds.spaceLocator(n="My_LOC_parent")
cmds.setAttr ("My_LOC_parentShape.localScaleX", 15)
cmds.setAttr ("My_LOC_parentShape.localScaleY", 15)
cmds.setAttr ("My_LOC_parentShape.localScaleZ", 15)
cmds.color("My_LOC_parent", rgb=(255, 255, 0))
cmds.xform(loc, t=pos)
cmds.parentConstraint(sel, "My_LOC_parent")
