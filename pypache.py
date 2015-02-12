#!/usr/bin/env python3.4
 
# IMPORTS
import re
import socket
from colorama import init, Fore, Back, Style
 
# VARS
regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"'
log_path = '/var/log/apache2/access.log'
previous_ip = " "
previous_host = " "
 
# FUNCTIONS
def adjust_item( str, i ):
    if len(str) < i:
        for j in range(i-len(str)):
            str = str + " "
    return str
 
def get_hostname( ip ):
    global previous_ip
    global previous_host
    if previous_ip == ip:
        return previous_host
    else:
        try:
            new_host = socket.gethostbyaddr(ip)
            previous_ip = ip
            previous_host = new_host[0]
            return new_host[0]
        except Exception:
            new_host = ip
            previous_ip = ip
            previous_host = ip
            return new_host
 
# READ FILE
with open(log_path, 'rt') as log:
    text = log.read();
 
# 185.31.48.30 - imr [12/Feb/2015:15:42:38 +0100] "GET /rt/rutorrent/plugins/diskspace/action.php?_=1423752158361 HTTP/1.1" 200 329 
# "https://jane.duckdns.org/rt/rutorrent/" "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"
#
# FOR EACH LINE
for line in text.split("\n"):
	if len(line) > 5:
		splitted = line.split("\"")
		print("First part", splitted[0])
		print("Request part", splitted[1])
		print("Code part", splitted[2])
		print("Referer part", splitted[3])
		print("Agent part", splitted[5])
	
