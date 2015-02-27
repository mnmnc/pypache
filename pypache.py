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
 
# FOR EACH LINE
for line in text.split("\n"):
    if len(line) > 5:
 
        # PARSE LINE AND ADJUST FIELD LENGTH
        ip      = adjust_item( re.match( regex, line ).group( 1 ), 15 )
        hostname    = adjust_item( str(get_hostname(ip.strip())), 30 )
        date        = (re.match( regex, line ).group( 2 )).split(" ")[0]
        request     = adjust_item( re.match( regex, line ).group( 3 ), 40 )
        code        = adjust_item( re.match( regex, line ).group( 4 ), 4 )
        size        = adjust_item( re.match( regex, line ).group( 5 ), 8 )
        ref     = adjust_item( re.match( regex, line ).group( 6 ), 30 )
        agent       = adjust_item( re.match( regex, line ).group( 7 ), 3 )
 
        # HTTP 200 OK
        if code.strip()[0] == "2":
 
            print( date + " " , end="")
            print( Fore.GREEN + Style.BRIGHT + code[:4] + Fore.RESET + Style.NORMAL, end="" )
            print( ip[:15] + " " , end="")
            print( hostname[:30] + " " , end="")
            print( size[:8] + " " , end="")
 
            # CHECK IF METHOD USED IS GET | POST
            if request[0] == "G" or request[0] == "P" :
                print( request[:40] + " " , end="")
            else:
                # OTHER METHODS PRINT IN COLOR
                print( Back.BLACK + Fore.RED + Style.DIM + request[:40] + Fore.RESET + Back.RESET + Style.NORMAL + " ", end="" )
 
            print( ref[:30] + " ", end="")
            print( agent[:3])
 
        # HTTP 300
        elif code.strip()[0] == "3":
            print( date + " " , end="")
            print( Fore.YELLOW + Style.BRIGHT + code[:4] + Fore.RESET + Style.NORMAL,  end="" )
            print( ip[:15] + " " , end="")
            print( hostname[:30] + " " , end="")
            print( size[:8] + " " , end="")
            print( request[:40] + " " , end="")
            print( ref[:30] + " ", end="")
            print( agent[:3])
 
        # HTTP 400
        elif code.strip()[0] == "4":
            print( date + " " , end="")
            print( Fore.BLUE + Style.BRIGHT + code[:4] + Fore.RESET + Style.NORMAL,  end="" )
            print( ip[:15] + " " , end="")
            print( hostname[:30] + " " , end="")
            print( size[:8] + " " , end="")
 
            # CHECK IF METHOD USED IS GET | POST
            if request[0] == "G" or request[0] == "P" :
                print( request[:40] + " " , end="")
            else:
                # OTHER METHODS PRINT IN COLOR
                new_request=Fore.RED + request[:40] + Fore.RESET
                print( new_request + " " , end="")
            print( ref[:30] + " ", end="")
            print( agent[:3])
 
        # HTTP 500
        elif code.strip()[0] == "5":
            print( date+ " " , end="")
            print( Fore.MAGENTA + Style.BRIGHT + code[:4] + Fore.RESET + Style.NORMAL ,  end="" )
            print( ip[:15] + " " , end="")
            print( hostname[:30] + " " , end="")
            print( size[:8] + " " , end="")
            print( request[:40] + " " , end="")
            print( ref[:30] + " ", end="")
            print( agent[:3])
 
        # OTHER
        else:
            print( date + " " , end="")
            print( code[:4],  end="" )
            print( ip[:15] + " " , end="")
            print( hostname[:30] + " " , end="")
            print( size[:8] + " " , end="")
            print( request[:40] + " " , end="")
            print( ref[:30] + " ", end="")
            print( agent[:3])
            
