"""
The script creates LOCs for aim constraint mostly applying for head
Phyton
by @mmariiaregiina
"""
import maya.cmds as cmds 

selection = cmds.ls(sl=1) 
if len(selection) == 0:
    cmds.inViewMessage(amg='ERROR: <hl>you have to select an object</hl>', pos='midCenter', fade=1)

# Creating locators in a pivot using Match transform:
loc_up = cmds.spaceLocator(n='LOC_UP') 
loc_front = cmds.spaceLocator(n='LOC_FRONT')
cmds.matchTransform(loc_up, selection, pos=1, rot=1, scl=1)
cmds.matchTransform(loc_front, selection, pos=1, rot=1, scl=1)

cmds.color(loc_up, rgb=(149, 0, 179))
cmds.color(loc_front, rgb=(149, 0, 179))

cmds.setAttr ("LOC_FRONTShape.localScaleX", 12)
cmds.setAttr ("LOC_FRONTShape.localScaleY", 12)
cmds.setAttr ("LOC_FRONTShape.localScaleZ", 12)

cmds.setAttr ("LOC_UPShape.localScaleX", 12)
cmds.setAttr ("LOC_UPShape.localScaleY", 12)
cmds.setAttr ("LOC_UPShape.localScaleZ", 12)

# Moving locators:
cmds.move(0, 50, 0, loc_up, wd=1, r=1, os=1)
cmds.move(0, 0, 40, loc_front, wd=1, r=1, os=1)

# Constraint aim:
cmds.parentConstraint(selection, loc_up, mo=1)
cmds.parentConstraint(selection, loc_front, mo=1)

minTime = cmds.playbackOptions(query=1, minTime=1)
maxTime = cmds.playbackOptions(query=1, maxTime=1)

cmds.bakeResults(loc_up, t=(minTime, maxTime))
cmds.bakeResults(loc_front, t=(minTime, maxTime))

cmds.delete("LOC_UP_parentConstraint1")
cmds.delete("LOC_FRONT_parentConstraint1")

cmds.aimConstraint(loc_front, selection, worldUpType='object', worldUpObject="LOC_UP", aimVector=[0, 0, 1], upVector=[0, 1, 0])

# Put in a group and freeze:
cmds.group(loc_up, loc_front, n="my_sys_for_head")
cmds.setAttr("my_sys_for_head.tx", lock=1)
cmds.setAttr("my_sys_for_head.ty", lock=1)
cmds.setAttr("my_sys_for_head.tz", lock=1)
cmds.setAttr("my_sys_for_head.rx", lock=1)
cmds.setAttr("my_sys_for_head.ry", lock=1)
cmds.setAttr("my_sys_for_head.rz", lock=1)
cmds.setAttr("my_sys_for_head.sx", lock=1)
cmds.setAttr("my_sys_for_head.sy", lock=1)
cmds.setAttr("my_sys_for_head.sz", lock=1)
cmds.setAttr("my_sys_for_head.v", lock=1)
