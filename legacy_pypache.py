#!/usr/bin/env python3.4
 
# IMPORTS
import re
import socket

 
# VARS
log_path = 'apache.log'
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

def get_agent(agent_string):
	if "Firefox/" in agent_string:
		return "Firefox"
	elif "MSIE" in agent_string:
		return "IE"
	elif "Seamonkey/" in agent_string:
		return "Seamonkey"
	elif "Chrome/" in agent_string and "Chromium" not in agent_string:
		return "Chrome"
	elif "Chromium/" in agent_string:
		return "Chromium"
	elif "Safari/" in agent_string and "Chrome" not in agent_string and "Chromium" not in agent_string:
		return "Safari"
	elif "OPR/" in agent_string or "Opera/" in agent_string:
		return "Opera"
	else:
		return "UNKNWN"

def minimal_print(text):

	# FOR EACH LINE
	for line in text.split("\n"):
		if len(line) > 5:

			try:

				# BUILDING DATA
				splitted = line.split("\"")

				first = splitted[0].split(" ")
				ip = first[0]
				user = first[2]
				date = first[3] + first[4]

				request = splitted[1]
				resp_code = splitted[2]
				ref = splitted[3]
				agent = get_agent(splitted[5])


				print(date, end="")
				print(resp_code, end="")
				print(agent, end=" ")
				print(ip, end=" ")
				print(get_hostname(ip), end=" ")
				print(user, end=" ")
				print(ref, end=" ")
				print(request, end=" ")
				print()

			except:
				pass

def print_adjusted(text):

	# FOR EACH LINE
	for line in text.split("\n"):
		if len(line) > 5:

			try:

				# BUILDING DATA
				splitted = line.split("\"")

				first = splitted[0].split(" ")
				ip = first[0]
				user = first[2]
				date = first[3] + first[4]

				request = splitted[1]
				resp_code = splitted[2]
				ref = splitted[3]
				agent = get_agent(splitted[5])

				# ADJUSTING
				agent = adjust_item(agent, 10)
				ip = adjust_item(ip, 15)
				hostname = adjust_item(get_hostname(ip), 30)
				user = adjust_item(user, 5)
				ref = adjust_item(ref, 20)
				request_list = request.split(" ")
				request_method = request_list[0]
				request_file = adjust_item(request_list[1], 30)
				request_protocol = (request_list[2]).split("/")[1]

				print(date, end=" ")
				print(ip, end=" ")
				print(hostname, end=" ")
				print(resp_code.split(" ")[1], end=" ")
				print(agent, end=" ")
				print(user, end=" ")
				print(ref[:20], end=" ")
				print(request_method[0], end=" ")
				print(request_protocol, end=" ")
				print(request_file[:30], end=" ")
				print()

			except:
				print("[ERR] Unable to process:", line)
				pass


def main():

	# READ FILE
	with open(log_path, 'rt') as log:
		text = log.read()

	# minimal_print(text)
	#print_adjusted(text)


if __name__ == "__main__":
	main()