import maya.cmds as cmds
import sys
# 创建窗口
if cmds.window('NamespaceWindow',ex =True):
    cmds.deleteUI('NamespaceWindow',wnd =True)
cmds.window('NamespaceWindow',t='RemoveNameSpace',widthHeight=(480, 100),sizeable =False)
def note(arg):
	print "Hello World"
	value=cmds.textField('input',q=True,tx=True)
	cmds.namespace(mv=(value,':'),force =True)
cmds.columnLayout(adj=True)
cmds.text(l='请输入NameSpace',fn='fixedWidthFont')
cmds.textField('input',tx='',fn='fixedWidthFont',bgc=(0,0,0))
cmds.button(l='确定',c=note)
cmds.showWindow()
