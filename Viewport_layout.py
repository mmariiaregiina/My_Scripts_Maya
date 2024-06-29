"""
The script turns off visiability of some objects left only
nurbs curves and pollygons
Phyton
by @mmariiaregiina
"""
import maya.cmds as cmds

cmds.modelEditor('modelPanel4', e=1, allObjects=0)
cmds.modelEditor('modelPanel4', e=1, controllers=1)
cmds.modelEditor('modelPanel4', e=1, nurbsCurves=1)
cmds.modelEditor('modelPanel4', e=1, polymeshes=1)
