# -*- coding: UTF-8 -*-
import time
import os

dirPath="/root/AutoConnection/log/"
delLogPath="/root/AutoConnection/log/"



timeNow=time.localtime(time.time())
timeNowYear=timeNow.tm_year
timeNowMon=timeNow.tm_mon

if(timeNowMon<=2):
    timeNowMon+=12
    timeNowYear-=1


def delLog(message):
	with open(delLogPath+"AutoConnectionDel.log", 'a+') as f:
	    DelMessage = message+"  "+'%02d' %timeNow.tm_year+"/"+'%02d' %timeNow.tm_mon+"/"+'%02d' %timeNow.tm_mday+"  "+'%02d' %timeNow.tm_hour+":"+'%02d' %timeNow.tm_min+":"+'%02d' %timeNow.tm_sec+"\n"
	    f.writelines(DelMessage)


for year in range(timeNowYear-1,timeNowYear+1):
    for mon in range(1,timeNowMon-1):
        path=dirPath+"AutoConnectionLog-"+'%02d' %year+"-"+'%02d' %mon+".log"
        if(os.path.exists(path)):
            delLog("[Delete]:"+path)
            os.remove(path)
        else:
            delLog("[Check]:"+path)


