import maya.cmds as cmds

selected = cmds.ls(sl=1,sn=True)
selVerts = cmds.ls(sl=True)
clst = cmds.cluster()
pos = cmds.xform(clst[1], q=True, ws=True, rp=True)
loc = cmds.spaceLocator(n = 'Center' )
cmds.move(pos[0], pos[1], pos[2])
cmds.delete(clst[1])

Center = "Center"

#maya.cmds.connectAttr('Center.translate','body_mesh2.translate')
#maya.cmds.connectAttr('Center.translate','body_mesh2.translate') 

maya.cmds.parent(selected,'elbow1')  