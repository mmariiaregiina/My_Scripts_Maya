"""
The script creates a Motion trail for only one selected object, covering 4 frames before and after the current Timeline position. 
The script can be assigned to a hotkey and used to create or delete the previous motion trail.

Скрипт создаёт Motion trail только для одного выбранного объекта, визуализируя 4 кадра до и после текущего положения.
Скрипт может быть назначен на Hotkey и использован для создания и удаления предыдущего Motion trail.

Phyton
by @mmariiaregiina
"""

import maya.cmds as cmds

def Create_Motion_Trail():
    startTime = cmds.playbackOptions(query=1, minTime=1)
    endTime = cmds.playbackOptions(query=1, maxTime=1)
    
    my_trail = cmds.snapshot(motionTrail=1, increment=1, startTime=startTime, endTime=endTime, name="My_Motion_Trail_")
    
    cmds.setAttr(my_trail[0] + "Shape.trailColor", 0.49, 0, 0.0337529, type='double3')
    cmds.setAttr(my_trail[0] + "Shape.trailColor", 1, 0, 0.0688834, type='double3')
    cmds.setAttr(my_trail[0] + "Shape.extraTrailColor", 0.0337529, 0, 0.49, type='double3')
    cmds.setAttr(my_trail[0] + "Shape.extraTrailColor", 0.0688834, 0, 1, type='double3')
    cmds.setAttr(my_trail[0] + "Shape.fadeInoutFrames", 1)
    cmds.setAttr(my_trail[0] + "Shape.preFrame", 4) 
    cmds.setAttr(my_trail[0] + "Shape.postFrame", 4) 


sel = cmds.ls(selection=1)
if len(sel) == 0: 
    cmds.inViewMessage(amg='ERROR: <hl>PLEASE, SELECT AN OBJECT</hl>', pos='midCenter', fade=1) 

if len(sel) > 1: 
    cmds.inViewMessage(amg='ERROR: <hl>PLEASE, SELECT ONLY ONE OBJECT</hl>', pos='midCenter', fade=1) 

if cmds.objExists("My_Motion_Trail_Handle"):
    cmds.delete("My_Motion_Trail_Handle")
else:
    Create_Motion_Trail()

