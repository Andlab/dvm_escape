###Poc for Dalvik Virtual Machine escape

展示了如何在android里面弹出一个计算器:smiley: 

1.install them

    adb install DvmEscape.apk	
	adb install CalcExe.apk

2.open DvmEscape.apk inside your android device
	
	python adb_type.py $(cat payload.txt)

