import socket

class Translator:

	previous_ip = ""
	previous_host = ""

	def ip_to_hostname(self, ip):

		if self.previous_ip == ip:
			return self.previous_host
		else:
			try:
				new_host = socket.gethostbyaddr(ip)
				self.previous_ip = ip
				self.previous_host = new_host[0]
				return new_host[0]
			except Exception:
				new_host = ip
				self.previous_ip = ip
				self.previous_host = ip
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