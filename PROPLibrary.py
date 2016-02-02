import maya.cmds as cmds
import sys
# 创建窗口
if cmds.window('PropWindow',ex =True):
    cmds.deleteUI('PropWindow',wnd =True)
cmds.window('PropWindow',t='PROP Library V1.0',widthHeight=(480, 200),sizeable =False)
# 定义元件库模型所在路径
configpath='\\'+'/192.168.1.100/设计部项目（2016年）/设计部元件及标准/2016年元件库/预案元件/'
def importBFSX(arg):
    # configpath='E:/00MaxProject/2016/PROP/Model/'
    fullpath= configpath+'泵房水箱/BF_SX_Yuanjian.fbx'
    cmds.file(fullpath,reference=True,ns='')
    cmds.file(fullpath,ir=True)
    cmds.namespace(mv=('BF_SX_Yuanjian',':'),force =True)
    

def importScene(arg):
	# configpath='E:/00MaxProject/2016/PROP/Model/'
    fullpath= configpath+'场景/CJ_Yuanjian.fbx'
    cmds.file(fullpath,reference=True,ns='')
    cmds.file(fullpath,ir=True)
    cmds.namespace(mv=('CJ_Yuanjian',':'),force =True)

def importfuti(arg):
    fullpath= configpath+'扶梯/Futi.fbx'
    cmds.file(fullpath,reference=True,ns='')
    cmds.file(fullpath,ir=True)
    cmds.namespace(mv=('Futi',':'),force =True)
def importindoor(arg):
    fullpath= configpath+'室内/SN_YUanjian.fbx'
    cmds.file(fullpath,reference=True,ns='')
    cmds.file(fullpath,ir=True)
    cmds.namespace(mv=('SN_YUanjian',':'),force =True)

cmds.columnLayout( adjustableColumn=True )

cmds.rowColumnLayout(numberOfColumns=5)   
cmds.button(l='泵房水箱',w =120,h=40,c=importBFSX)
cmds.button(l='场景',w =120,h=40,c=importScene)
cmds.button(l='扶梯',w =120,h=40,c=importfuti)
cmds.button(l='室内',w =120,h=40,c=importindoor)
cmds.setParent( '..' )
# cmds.setParent( '..' )
cmds.columnLayout()

version = 'Based on Maya2016 use sublime text3 yuhonglei January 19, 2016'
cmds.button(l=version,w=480,en=False)
cmds.showWindow()
