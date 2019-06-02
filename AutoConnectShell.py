#coding:utf-8

import requests
import time

username="wujie427"
password="xiyou3gfz155"
testurl = "https://baidu.com"
reurl = "http://172.18.0.3/a.htm"


i = time.localtime(time.time())
str="/root/AutoConnection/log/AutoConnectionLog-"+'%02d' %i.tm_year+"-"+'%02d' %i.tm_mon+".log"
with open(str, 'a+') as f:
    ErrMessage = "[Start] "+'%02d' %i.tm_year+"/"+'%02d' %i.tm_mon+"/"+'%02d' %i.tm_mday+"  "+'%02d' %i.tm_hour+":"+'%02d' %i.tm_min+":"+'%02d' %i.tm_sec+"  AutoConnectionShell start!\n"
    print(ErrMessage)
    f.writelines(ErrMessage)




headers = {
	'User-Agent': "PostmanRuntime/7.13.0",
	'Accept': "*/*",
	'Cache-Control': "no-cache",
	'accept-encoding': "gzip, deflate",
	'referer': "https://baidu.com/",
	'Connection': "keep-alive",
	'cache-control': "no-cache"
}

reheaders = {
    'Host': "172.18.0.3",
    'Connection': "keep-alive",
    'Content-Length': "140",
    'Cache-Control': "max-age=0",
    'Origin': "http://172.18.0.3",
    'Upgrade-Insecure-Requests': "1",
    'Content-Type': "application/x-www-form-urlencoded",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    'Referer': "http://172.18.0.3/a70.htm",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cookie': "program=xupt-20171115; vlan=0; ip=222.24.34.98; username="+username+"; md5_login2="+username+"%7C"+password,
    'cache-control': "no-cache"
}
payload = "DDDDD="+username+"&upass="+password+"&R1=0&R2=&R6=0&para=00&0MKKey=123456&buttonClicked=&redirect_url=&err_flag=&username=&password=&user=&cmd=&Login="


def reconnectionlog():
	i = time.localtime(time.time())
	str="/root/AutoConnection/log/AutoConnectionLog-"+'%02d' %i.tm_year+"-"+'%02d' %i.tm_mon+".log"
	with open(str, 'a+') as f:
	    ErrMessage = "[ReConnect] "+'%02d' %i.tm_year+"/"+'%02d' %i.tm_mon+"/"+'%02d' %i.tm_mday+"  "+'%02d' %i.tm_hour+":"+'%02d' %i.tm_min+":"+'%02d' %i.tm_sec+"  AutoConnectionShell Successful reconnection!\n"
	    print(ErrMessage)
	    f.writelines(ErrMessage)

def drop():
	i = time.localtime(time.time())
	str="/root/AutoConnection/log/AutoConnectionLog-"+'%02d' %i.tm_year+"-"+'%02d' %i.tm_mon+".log"
	with open(str, 'a+') as f:
	    ErrMessage = "[Error] "+'%02d' %i.tm_year+"/"+'%02d' %i.tm_mon+"/"+'%02d' %i.tm_mday+"  "+'%02d' %i.tm_hour+":"+'%02d' %i.tm_min+":"+'%02d' %i.tm_sec+"  AutoConnectionShell Link disconnect!\n"
	    print(ErrMessage)
	    f.writelines(ErrMessage)


def reconnection():
	while True:
		time.sleep(1)
		try:
			response = requests.request("POST", reurl, data=payload, headers=reheaders)
			try:
				testresponse = requests.request("GET", testurl, headers=headers)
				body_data = response.status_code
				if(body_data==200):
					reconnectionlog()
					break
				else:
					continue
			except:
				continue
		except:
			continue
	
while(1):
	try:
		response = requests.request("GET", testurl, headers=headers)
		body_data = response.status_code
		if(body_data==200):
			pass
		else:
			drop()
			reconnection()	
	except:
		drop()
		reconnection()
	time.sleep(5)

