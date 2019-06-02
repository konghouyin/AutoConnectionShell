#!/bin/sh
ret=$(ps T|grep python|grep -E 'AutoConnectShel')
echo $ret
if [ -n "$ret" ];then
	echo "Shell online";
else
	/usr/bin/python /root/AutoConnection/AutoConnectShell.py &
	echo "startShell";
fi
