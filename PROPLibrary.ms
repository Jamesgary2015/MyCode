macroScript AnXin_PROPLibrary category:"北京安信" tooltip:"PROP Library V1.0" buttontext:"PROP Library" Icon:#("Helpers",1)
(
rollout PropRollout "PROP Library V1.0" width:510 height:100
(
	button 'btn1' "泵房水箱" pos:[0,5] width:120 height:40 toolTip:"" align:#left
	button 'btn2' "场景" pos:[130,5] width:120 height:40 toolTip:"" align:#left
	button 'btn3' "扶梯" pos:[260,5] width:120 height:40 toolTip:"" align:#left
	button 'btn4' "室内" pos:[390,5] width:120 height:40 toolTip:"" align:#left	
	button 'btn100' "Based on 3ds max2016 use sublime text3 yuhonglei January 19, 2016" pos:[0,50] width:510 height:30 enabled:false align:#left
	
	
	on btn1 pressed  do
    (
		configpath = "\\\192.168.1.100\\设计部项目（2016年）\\设计部元件及标准\\2016年元件库\\预案元件\\泵房水箱\\"
		fullpath = configpath+"BF_SX_Yuanjian"+".fbx"
		
		importfile fullpath
	
	)
	
	on btn2 pressed do
	(		
		configpath = "\\\192.168.1.100\\设计部项目（2016年）\\设计部元件及标准\\2016年元件库\\预案元件\\\场景\\"
		fullpath = configpath+"CJ_Yuanjian"+".fbx"			
		importfile fullpath
		
	)

	on btn3 pressed do
	(
		configpath = "\\\192.168.1.100\\设计部项目（2016年）\\设计部元件及标准\\2016年元件库\\预案元件\\\扶梯\\"
		fullpath = configpath+"Futi"+".fbx"			
		importfile fullpath
	)

	on btn4 pressed do
	(
		configpath = "\\\192.168.1.100\\设计部项目（2016年）\\设计部元件及标准\\2016年元件库\\预案元件\\\室内\\"
		fullpath = configpath+"SN_YUanjian"+".fbx"			
		importfile fullpath
	)
)
-- 创建窗口
createDialog PropRollout
)
